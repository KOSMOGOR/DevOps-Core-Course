# Lab 03 Bonus Task

## Workflow Implementation

Rust workflow uses:

- `actions/cache` for caching dependencies
- `cargo build` for building
- `cargo clippy` for linting
- `cargo test` for testing
- and same workflow for building and pushing image as `app_python/` (same version strategy using current date)

## Path Config

Both workflows checks their directory (`app_pytho/` or `app_rust/`) and exludes changes made to `docs/**` or `README.md`

This makes workflow better, since it won't trigger pointlessly, if not important file to workflow will be changed.
