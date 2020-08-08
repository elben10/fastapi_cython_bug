from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("fastapi_cython_bug/module.pyx")
)