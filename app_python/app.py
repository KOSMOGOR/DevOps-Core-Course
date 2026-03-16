"""
DevOps Info Service
Main application module
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import dotenv
import platform
import os
import socket
from datetime import datetime, timezone
import logging
import json
from prometheus_client import CollectorRegistry, Counter, Histogram, Gauge, make_asgi_app

# Configuration
dotenv.load_dotenv()
HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 8000))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Application
app = FastAPI()

# Start time
start_time = datetime.now()

# Define metrics
registry = CollectorRegistry()
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status'],
    registry=registry
)
http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration',
    ['method', 'endpoint'],
    registry=registry
)
http_requests_in_progress = Gauge(
    'http_requests_in_progress',
    'HTTP requests currently being processed',
    registry=registry
)
system_info_duration = Histogram(
    'devops_info_system_collection_seconds',
    'System info collection time',
    registry=registry
)

# Logging setup
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "message": record.getMessage(),
            "level": record.levelname,
            "logger": record.name
        }
        fields = ["method", "path", "status_code", "client_ip"]
        for field in fields:
            if hasattr(record, field):
                value = getattr(record, field, None)
                log[field] = value
        return json.dumps(log)


handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logging.root.handlers = [handler]
logging.root.setLevel(logging.INFO)

logger = logging.getLogger(__name__)


def get_time_info():
    """Return info about current time and application uptime"""
    now = datetime.now()
    delta = now - start_time
    return {
        "uptime_seconds": delta.seconds,
        "uptime_human": f"{delta.seconds // 3600} hour,\
{delta.seconds % 3600 // 60} minutes",
        "current_time": datetime.now(timezone.utc).isoformat(),
        "timezone": "UTC"
    }


@app.middleware("http")
async def log_request_info(request: Request, call_next):
    endpoint = request.url.path
    method = request.method
    logger.info("Request", extra={
        "method": method,
        "path": endpoint,
        "client_ip": request.client.host,
    })
    http_requests_in_progress.inc()
    with http_request_duration_seconds.labels(method=method, endpoint=request.url.path).time():
        response = await call_next(request)
    status_code = response.status_code
    level = logging.ERROR if status_code >= 500 else logging.WARNING if status_code >= 400 else logging.INFO
    logger.log(level, "Response", extra={
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host,
        "status_code": status_code
    })
    http_requests_total.labels(method=method, status=status_code, endpoint=endpoint).inc()
    http_requests_in_progress.dec()
    return response


@app.get("/")
def app_root(request: Request):
    """Main endpoint - service and system information"""
    with system_info_duration.time():
        time_info = get_time_info()
        info = {
            "service": {
                "name": "devops-info-service",
                "version": "1.0.0",
                "description": "DevOps course info service",
                "framework": "FastAPI"
            },
            "system": {
                "hostname": socket.gethostname(),
                "platform": platform.system(),
                "platform_version": platform.version(),
                "architecture": platform.machine(),
                "cpu_count": os.cpu_count(),
                "python_version": platform.python_version()
            },
            "runtime": time_info,
            "request": {
                "client_ip": request.client.host,
                "user_agent": request.headers.get("user-agent"),
                "method": request.method,
                "path": request.url.path
            },
            "endpoints": [
                {"path": "/", "method": "GET",
                "description": "Service information"},
                {"path": "/health", "method": "GET", "description": "Health check"}
            ]
        }
    return info


@app.get("/health")
def app_health():
    """Health endpoint - for checking application health"""
    time_info = get_time_info()
    return {
        "status": "healthy",
        "timestamp": time_info["current_time"],
        "uptime_seconds": time_info["uptime_seconds"]
    }


metrics_app = make_asgi_app(registry)
app.mount("/metrics", metrics_app)


@app.exception_handler(404)
def not_found(request: Request, exception: Exception):
    return JSONResponse(
        {
            "error": "Not Found",
            "message": "Endpoint does not exist"
        },
        status_code=404
    )


@app.exception_handler(500)
def internal_server_error(request: Request, exception: Exception):
    return JSONResponse(
        {
            "error": "Internal Server Error",
            "message": "An unexpected error ocured"
        },
        status_code=500
    )


if __name__ == "__main__":
    import uvicorn
    logger.info(f"Application starting on http://{HOST}:{PORT}/")
    uvicorn.run("app:app", host=HOST, port=PORT, reload=DEBUG)
