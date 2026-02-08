# Lab 03

## Choosing Test Framework

I chose pytest as test framework for some reasons:

- It supports different kind of tests
- It has simple syntax
- It supports powerfull fixtures
- It has rich plugin architecture

## Tests Structure

File `test_endpoints.py` consists of 3 test functions:

- `test_root()` verifies status code, structure, and fields of request to `/`
- `test_health()` verifies status code, structure and fields of request to `/health`
- `test_404()` verifies status code of request to not existing path

## Tests Terminal Output

```bash
$ pytest tests/
========================= test session starts =========================
platform win32 -- Python 3.14.0, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\DevOps\app_python
plugins: anyio-4.12.1
collected 3 items

tests\test_endpoints.py ...                                      [100%]

========================== 3 passed in 0.54s ==========================
```
