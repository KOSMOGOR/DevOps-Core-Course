"""
DevOps Info Service
Main application module
"""
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import dotenv
import platform
import os
import socket
from datetime import datetime, timezone
import logging
import json

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
    logger.info("Request", extra={
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host,
    })
    response = await call_next(request)
    status_code = response.status_code
    level = logging.ERROR if status_code >= 500 else logging.WARNING if status_code >= 400 else logging.INFO
    logger.log(level, "Response", extra={
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host,
        "status_code": status_code
    })
    return response


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
    logger.info(f"Application starting on http://{HOST}:{PORT}/")
    uvicorn.run("app:app", host=HOST, port=PORT, reload=DEBUG)
