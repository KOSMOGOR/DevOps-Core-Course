# Rust Web Server

## Overview

This is a web application providing detailed information about itself and its runtime environment

## Prerequisites

- Rust 1.89.0
- Cargo 1.89.0

## Installation

```bash
cargo build
```

## Running the Application

You can create `.env` file storing all enviroment values. To run application simply type:

```bash
cargo run --release
```

## API Endpoints

- `GET /` - Service and system information
- `GET /health` - Health check

## Configuration

Supported enviroment values:

- `HOST` - address for running app
- `PORT` - port for running app
- `DEBUG` - `[true/false]` enable debug features or not
