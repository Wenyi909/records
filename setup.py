#!/usr/bin/env python

from setuptools import setup, find_packages

# parse version string from the __init__ file
with open("records/__init__.py", "r") as initfile:
    lines = initfile.readlines()
    for line in lines:
        if "__version__" in line:
            # get version line and strip white space and quotations
            version = line.strip().split()[-1].strip("'").strip('"')

# build command
setup(
    name="records",
    version=version,
    packages=find_packages(),
    author="Wenyi Zhang",
    author_email="wz2306@columbia.edu",
    license="GPLv3",
    descrption="A package for querying GBIF",
    Classifiers=["Programming Language :: Python :: 3"])
