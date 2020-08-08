# Reproduction

## Create venv


```bash
python -m venv venv
source ./venv/activate
```

## Requirements 

```python
pip install fastapi Cython
```

## Build cython module

```bash
python setup.py build_ext --inplace
```

## Run uvicorn

```bash
uvicorn main:app
```