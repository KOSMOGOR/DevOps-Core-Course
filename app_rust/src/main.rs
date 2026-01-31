use std::{env, sync::Mutex, thread};
use actix_web::{App, HttpRequest, HttpServer, Responder, get, middleware::Logger, web::Json};
use chrono::{DateTime, Utc};
use log::info;
use serde::Serialize;

#[derive(Serialize)]
struct ServiceInfo {
    name: String,
    version: String,
    description: String,
    framework: String
}

#[derive(Serialize)]
struct SystemInfo {
    hostname: String,
    platform: String,
    platform_version: String,
    architecture: String,
    cpu_count: usize,
    rust_version: String
}

#[derive(Serialize)]
struct RuntimeInfo {
    uptime_seconds: i64,
    uptime_human: String,
    current_time: String,
    timezone: String
}

#[derive(Serialize)]
struct RequestInfo {
    client_ip: String,
    user_agent: String,
    method: String,
    path: String
}

#[derive(Serialize)]
struct EndpointInfo {
    path: String,
    method: String,
    description: String,
}

#[derive(Serialize)]
struct RootResponse {
    service: ServiceInfo,
    system: SystemInfo,
    runtime: RuntimeInfo,
    request: RequestInfo,
    endpoints: Vec<EndpointInfo>
}

#[get("/")]
async fn app_root(req: HttpRequest) -> impl Responder {
    let os_info_got = os_info::get();
    let current_time = Utc::now();
    let time_delta = current_time - *STARTING_TIME.lock().unwrap();
    let data = RootResponse {
        service: ServiceInfo {
            name: "devops-info-service".to_string(),
            version: "1.0.0".to_string(),
            description: "DevOps course info service".to_string(),
            framework: "Actix Web".to_string()
        },
        system: SystemInfo {
            hostname: gethostname::gethostname().into_string().unwrap(),
            platform: os_info_got.os_type().to_string(),
            platform_version: os_info_got.version().to_string(),
            architecture: os_info_got.architecture().unwrap().to_string(),
            cpu_count: thread::available_parallelism().unwrap().get(),
            rust_version: env::var("RUST_VERSION").unwrap_or("Unknown".to_string())
        },
        runtime: RuntimeInfo {
            uptime_seconds: time_delta.num_seconds(),
            uptime_human: format!("{} hour, {} minutes", time_delta.num_seconds() / 3600, time_delta.num_seconds() % 3600 / 60),
            current_time: current_time.to_rfc3339(),
            timezone: "UTC".to_string()
        },
        request: RequestInfo {
            client_ip: req.connection_info().host().to_string(),
            user_agent: req.headers().get("user-agent").unwrap().to_str().unwrap().to_string(),
            method: req.method().to_string(),
            path: req.path().to_string()
        },
        endpoints: vec![
            EndpointInfo { path: "/".to_string(), method: "GET".to_string(), description: "Service information".to_string() },
            EndpointInfo { path: "/health".to_string(), method: "GET".to_string(), description: "Health check".to_string() }
        ]
    };
    Json(data)
}

#[derive(Serialize)]
struct HealthResponse {
    status: String,
    timestamp: String,
    uptime_seconds: i64
}

#[get("/health")]
async fn app_health() -> impl Responder {
    let current_time = Utc::now();
    let time_delta = current_time - *STARTING_TIME.lock().unwrap();
    let data = HealthResponse {
        status: "healthy".to_string(),
        uptime_seconds: time_delta.num_seconds(),
        timestamp: current_time.to_rfc3339(),
    };
    Json(data)
}

static STARTING_TIME: Mutex<DateTime<Utc>> = Mutex::new(DateTime::from_timestamp(0, 0).unwrap());

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // loading and setting env variables
    dotenvy::dotenv().unwrap();
    let debug = env::var("DEBUG").is_ok();
    unsafe {
        std::env::set_var("RUST_LOG", if debug { "debug" } else { "info" });
        std::env::set_var("RUST_BACKTRACE", "1");
    }
    // initializing logger
    env_logger::init();

    // storing starting time
    { *STARTING_TIME.lock().unwrap() = Utc::now(); }

    // getting host and port
    let host = env::var("HOST").unwrap_or("127.0.0.1".to_string());
    let port = if let Ok(s) = env::var("PORT") { s.parse().unwrap() } else { 8080 };
    info!("Starting server at http://{host}:{port}");
    // building and starting server
    HttpServer::new(|| {
        let logger = Logger::default();

        App::new()
            .wrap(logger)
            .service(app_root)
            .service(app_health)
    })
    .bind((host, port))?
    .run()
    .await
}
