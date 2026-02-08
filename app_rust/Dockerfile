FROM rust:1.89-alpine AS builder

RUN apk add --no-cache libc-dev

RUN cd / && \
    cargo new app
WORKDIR /app

COPY Cargo.toml Cargo.lock ./
RUN cargo build --release
RUN rm -r src/

COPY src ./src
RUN cargo build --release

FROM alpine:3.23.3
WORKDIR /app

COPY --from=builder /app/target/release/app_rust .

RUN adduser --no-create-home --disabled-password appuser
USER appuser

ENV RUST_VERSION=1.89
ENV HOST=0.0.0.0
ENV PORT=8080
EXPOSE 8080

ENTRYPOINT ["./app_rust"]