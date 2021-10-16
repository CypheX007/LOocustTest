# Locust Test Example

## Warning !

Run the test inside the virtual environment.



## Installation

##### Locust
```bash
pip install locust
```

##### Virtual Environment
```bash
pip install virtualenv
virtualenv 'your virtualenv name'
```

##### FastApi

```bash
pip install fastapi
```

##### Pydantic

```bash
pip install pydantic
```

## Usage

```bash
uvicorn 'Your Api File Name':'Your FastApi() name' --reload        #For Start Api
locust -f 'Your Locust file name'.py        #For Start Locust
```