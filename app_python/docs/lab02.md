# Lab 02

## Best Practices Applied

- Using non-root user (to increase security)
- Layer caching (installing depenencies before copying whole app to reduce time spend on rebuilds)
- Using .dockerignore (exluding useless files to reduce image size)
- Using slim version of python (to reduce image size)

## Image Information & Decisions

- Base image chosen - `python:3.14-slim`, because it is much less, than `python:3.14`
- Image size - 305 MB
- Layers consist of:
  - Updated pip
  - Installed requirements
  - Copied app
  - Added user
- As optimizations: version of python with lesser size was selected, layers was separated

## Build & Run Process

- Terminal output after building:

```bash
$ docker build -t devops .
[+] Building 14.8s (13/13) FINISHED docker:desktop-linux
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 370B
 => [internal] load metadata for docker.io/library/python:3.14-slim 
 => [auth] library/python:pull token for registry-1.docker.io
 => [internal] load .dockerignore
 => => transferring context: 152B
 => [1/7] FROM docker.io/library/python:3.14-slim@sha256:9b81fe9acff79e61affb44aaf3b6ff234392e8ca477cb86c9f7fd11732ce9b6a
 => => resolve docker.io/library/python:3.14-slim@sha256:9b81fe9acff79e61affb44aaf3b6ff234392e8ca477cb86c9f7fd11732ce9b6a
 => [internal] load build context
 => => transferring context: 214B
 => CACHED [2/7] WORKDIR /app
 => CACHED [3/7] RUN pip install --upgrade pip
 => CACHED [4/7] COPY requirements.txt .
 => CACHED [5/7] RUN pip install --no-cache-dir -r requirements.txt
 => CACHED [6/7] COPY . .
 => CACHED [7/7] RUN groupadd -r python && useradd --no-log-init -r -g python python
 => exporting to image
 => => exporting layers
 => => exporting manifest sha256:c7850188d3142e34ad3e3b985952640a14d3ccde4c99829768a2dfc76181bbbb
 => => exporting config sha256:31eafc1aadfa9740a3572f805ea6d9a1d308bff5f1d83c1a692360a5e3008830
 => => exporting attestation manifest sha256:b22eb31e41372e15b322ed88e9e1c2897ff292ba805d5d47e412466f3a1e31e3
 => => exporting manifest list sha256:81c00de18c3e957fb3d23c8d5878042844517e890940c52129ca5efaa7dc2493
 => => naming to docker.io/library/devops:latest
 => => unpacking to docker.io/library/devops:latest
```

- Terminal output of running container:

```bash
2026-01-30 19:18:18,908 - __main__ - INFO - Application starting...
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

- Terminal output after accessing enpoints:

```bash
INFO:     172.17.0.1:55036 - "GET / HTTP/1.1" 200 OK
INFO:     172.17.0.1:55038 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```

```bash
INFO:     172.17.0.1:46772 - "GET /health HTTP/1.1" 200 OK
INFO:     172.17.0.1:46778 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```

- Docker Hub repository URL - <https://hub.docker.com/r/kosmogor/devops>

## Technical Analysis

- Why does your Dockerfile work the way it does? - Because Docker interprets this file this way
- What would happen if you changed the layer order? - Most likely that image will have to be built more times
- What security considerations did you implement? - I changed user from `root` to `python`, that doesn't allow hacker, who get access to this user, get access to whole system (since user `python` don't have elevated privileges)
- How does .dockerignore improve your build?

## Challenges & Solutions

I had some problems of not knowing some command for Dockerfile (especially how to create new user and how to expose port). I solved it by looking into Docker documentation and stackoverflow.com.
