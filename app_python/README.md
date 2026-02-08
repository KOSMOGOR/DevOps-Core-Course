# Python Web Server

## Overview

This is a web application providing detailed information about itself and its runtime environment

## Prerequisites

- Python 3.14.0

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

You can create `.env` file storing all enviroment values. To run application simply type:

```bash
python app.py
```

## Docker

You can also build, pull, and run this app using Docker.

To build simply run:

```bash
docker build -t devops .
```

To pull simply run:

```bash
docker pull docker.io/kosmogor/devops
```

To run simply run:

```bash
docker run devops:latest
```

## Testing

App can be easily tested after installation by simply running:

```bash
pytest /tests
```

## API Endpoints

- `GET /` - Service and system information
- `GET /health` - Health check

## Configuration

Supported enviroment values:

- `HOST` - address for running app
- `PORT` - port for running app
- `DEBUG` - `[true/false]` enable debug features or not
