from setuptools import setup
from Cython.Build import cythonize

# import distutils.core
# import Cython.Build

setup(
    ext_modules = cythonize("test_cython.pyx")
)

# distutils.core.setup(
#     ext_modules = Cython.Build.cythonize(
#         "test_cython.pyx"
#     )
# )

from setuptools import setup, find_packages
setup(name='cythonizing_scripts', version='1.0', packages=find_packages())