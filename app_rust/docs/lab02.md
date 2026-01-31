# Lab 01 Bonus Task

## Multi-Stage Build Strategy

I used rust:1.89-alpine for building app and alpine:3.23.3 for running it.

## Size Comparison

rust:1.89-alpine's size is around 311 Mb and `target` folder size is almost 1.8 Gb (at least on Windows), but final image size (that uses alpine:3.23.3) is only 14 Mb!

## Why Multi-Stage Builds Matter for Compiled Languages

Previous section showed that final image size is sinficantly less if done using multi-stage, which makes it mush easy to pull and store. Also final image will have less vulnarabilities, since it has less installed things.

## Terminal Output

- Building process:

```bash
[+] Building 4.1s (19/19) FINISHED                                                                                                                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 518B 
 => [internal] load metadata for docker.io/library/alpine:3.23.3
 => [internal] load metadata for docker.io/library/rust:1.89-alpine
 => [internal] load .dockerignore
 => => transferring context: 398B
 => [builder 1/9] FROM docker.io/library/rust:1.89-alpine@sha256:4b800f2e72e04be908e5f634c504c741bd943b763d1d8ad7b096cc340e1b5b46
 => => resolve docker.io/library/rust:1.89-alpine@sha256:4b800f2e72e04be908e5f634c504c741bd943b763d1d8ad7b096cc340e1b5b46
 => [internal] load build context    
 => => transferring context: 117B
 => [stage-1 1/4] FROM docker.io/library/alpine:3.23.3@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659
 => => resolve docker.io/library/alpine:3.23.3@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659
 => [builder 2/9] RUN apk add --no-cache libc-dev
 => [builder 3/9] RUN cd / &&     cargo new app
 => [builder 4/9] WORKDIR /app
 => [builder 5/9] COPY Cargo.toml Cargo.lock ./
 => [builder 6/9] RUN cargo build --release
 => [builder 7/9] RUN rm -r src/
 => [builder 8/9] COPY src ./src
 => [builder 9/9] RUN cargo build --release
 => [stage-1 2/4] WORKDIR /app
 => [stage-1 3/4] COPY --from=builder /app/target/release/app_rust .
 => [stage-1 4/4] RUN adduser --no-create-home --disabled-password appuser
 => exporting to image
 => => exporting layers
 => => exporting manifest sha256:74cdc2c192f3b5a3f5af7df59744cdbcd4954d898fd299c78c8f8c8a6e15eca9
 => => exporting config sha256:72f09ab3ec5d82fa30351331824d1b324f84b49d0bbfedb0f01e269fbd689d28
 => => exporting attestation manifest sha256:3ee7704cbaa1ff9f183bcf4bef4530f9c8b79e7b6ad070a16563d74bb8145b19
 => => exporting manifest list sha256:80fc8b4b9ffa8149a8c158eb2bb5e0c1dfd206f0b3c42a38dd80d91c7acde6d9
 => => naming to docker.io/library/devops_rust:latest
 => => unpacking to docker.io/library/devops_rust:latest
```

- Image size:

```bash
$ docker images

IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
devops_rust:latest   3fc8f0d0abda       13.8MB         4.12MB
```

## Stage Explanations

- `FROM rust:1.89-alpine AS builder`:
  - `apk add --no-cache libc-dev` - install essential dependencies for building
  - from `RUN cd /` to `RUN rm -r src/` - creates blank app with dependencies like in `app_rust`, it is used for caching builded dependecies, which reduces time for rebuilding app from around 7 minutes to less than 20 seconds (this is the only method to cache dependencies I know of)
  - `COPY src ./src` and `RUN cargo build --release`
- `FROM alpine:3.23.3`:
  - from `WORKDIR /app` to `EXPOSE 8080` - copying binary from builder, adding new non-root user (to increase security), setting enviroment values, and exposing port
  - `ENTRYPOINT ["./app_rust"]` - starting app
