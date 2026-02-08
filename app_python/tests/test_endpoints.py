from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    res_json: dict = response.json()
    assert "service" in res_json
    assert all(x in res_json["service"] for x in
               ["name", "version", "description", "framework"])
    assert "system" in res_json
    assert all(x in res_json["system"] for x in
               ["hostname", "platform", "platform_version",
                "architecture", "cpu_count", "python_version"])
    assert "runtime" in res_json
    assert all(x in res_json["runtime"] for x in
               ["uptime_seconds", "uptime_human", "current_time", "timezone"])
    assert "request" in res_json
    assert all(x in res_json["request"] for x in
               ["client_ip", "user_agent", "method", "path"])
    assert "endpoints" in res_json
    assert type(res_json["endpoints"]) is list


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    res_json: dict = response.json()
    assert all(x in res_json for x in
               ["status", "timestamp", "uptime_seconds"])


def test_404():
    response = client.get("/definitely/wrong/path")
    assert response.status_code == 404
