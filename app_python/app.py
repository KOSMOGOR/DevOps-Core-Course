"""
DevOps Info Service
Main application module
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import dotenv
import platform
import os
import socket
from datetime import datetime, timezone
import logging

# Configuration
dotenv.load_dotenv()
HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 8000))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Application
app = FastAPI()

# Start time
start_time = datetime.now()

# Logging setup
logging.basicConfig(
    level=logging.INFO if not DEBUG else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
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
def log_request_info(request: Request, call_next):
    logger.debug(f'Request: {request.method} {request.url}')
    return call_next(request)


@app.get("/")
def app_root(request: Request):
    """Main endpoint - service and system information"""
    time = get_time_info()
    return {
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
        "runtime": time,
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


@app.get("/health")
def app_health():
    """Health endpoint - for checking application health"""
    time = get_time_info()
    return {
        "status": "healthy",
        "timestamp": time["current_time"],
        "uptime_seconds": time["uptime_seconds"]
    }


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
    logger.info("Application starting...")
    uvicorn.run("app:app", host=HOST, port=PORT, reload=DEBUG)
