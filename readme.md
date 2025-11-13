# Instructions

## Prerequisites

Python 3.10+
Mac, Linux, or WSL

## Set up environment

Option 1: pip

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Option 2: poetry

```shell
poetry install
eval $(poetry env activate)
```

Option 3: uv

```shell
uv install
source .venv/bin/activate
```

## Exercises

### 1 - Code Review (10 minutes)

Look at the code in `1_code_review/fetch_user_data.py`

Review this code that fetches user data from an API. Identify at least 4 issues and explain how you would fix them.

You may edit the file and add your answers as comments.

### 2 - Unit Testing (10 minutes)

Look at the code in `2_unit_tests/products.py`

Write unit tests for this function using pytest and pytest-asyncio. Include tests for:

- Successful API response
- HTTP error handling
- Invalid JSON response

### 3 - Async Function (10 minutes)

Look at the code in `3_async_function/weather.py`

Implement the function that fetches weather data for multiple cities concurrently. Use `httpx.AsyncClient` and ensure requests run in parallel.
