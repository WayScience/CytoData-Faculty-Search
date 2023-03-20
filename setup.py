"""
script: setup.py

installs this package into python environment.
"""
from setuptools import find_packages, setup

setup(
    name="NIH-faculty-search",
    author="Erik Serrano",
    version="0.0.1",
    author_email="erik.serrano@cuanschutz.edu",
    packages=find_packages(),
)
