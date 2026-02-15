# Lab 03

## Testing

### Choosing Test Framework

I chose pytest as test framework for some reasons:

- It supports different kind of tests
- It has simple syntax
- It supports powerfull fixtures
- It has rich plugin architecture

### Tests Structure

File `test_endpoints.py` consists of 3 test functions:

- `test_root()` verifies status code, structure, and fields of request to `/`
- `test_health()` verifies status code, structure and fields of request to `/health`
- `test_404()` verifies status code of request to not existing path

### Tests Terminal Output

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

## Actions Workflow

### Workflow Trigger Strategy

Workflow triggers on opening (or reopening) pull requests to master, since we need to check code before merging.

### Action Choice

I chose official GitHub and Docker actions, since they are trustworthy.

### Docker Tagging Strategy

Fro tagging I have used current date, since it is enough for version tracking.

### Proofs

Link to successful workflow: <https://github.com/KOSMOGOR/DevOps-Core-Course/actions/runs/21801589090>

Screenshot:

![Workflow](./screenshots/lab03/successful-actions-workflow.png)

## Continious Integration

### Successful working badge

![badge](/docs/screenshots/lab03/successful-actions-badge.png)

### Caching Implemantation

Caching was implemented using `cache: pip`

### Best Practices

I used practices like:

- Optimize pipeline stages - I optimized pipeline stages
- Use failures to improve processes - tasks can fail due to not compliting some requirements
- Use secrets - I used GitHub secrets for tokens in workflow

### Snyk Integration Results

Snyk found vulnarability in package `python-multipart` and suggested upgrading it, and I have done it.
