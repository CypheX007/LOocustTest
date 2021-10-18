# Locust Test Example

## Warning !

Run the test inside the virtual environment.

## Installation

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Start API Server

```bash
uvicorn src.api:app
```

### Start Locust Server

```bash
locust \
    -f src/locust_example.py \
    --autostart \
    --autoquit 3 \
    --users 10 \
    --spawn-rate 50 \
    --run-time 30s
```
