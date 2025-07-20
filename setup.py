from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Julia set calculation',
    ext_modules=cythonize('src/julia_set_cython.pyx')
)

