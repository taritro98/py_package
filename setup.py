from gettext import install
from setuptools import setup, find_packages
import os

VERSION = '0.0.0'
DESCRIPTION = 'A basic hello world package'

setup(
    name="helloworld",
    version=VERSION,
    description=DESCRIPTION,
    author="Taritro",
    packages=["helloworld"],
    install_requires=[]
)