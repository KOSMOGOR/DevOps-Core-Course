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

## API Endpoints

- `GET /` - Service and system information
- `GET /health` - Health check

## Configuration

Supported enviroment values:

- `HOST` - address for running app
- `PORT` - port for running app
- `DEBUG` - `[true/false]` enable debug features or not
