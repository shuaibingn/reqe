#!/usr/bin/env python3
import sys
from setuptools import setup

if sys.version_info < (2, 5):
    sys.exit("Python 3.5 or greater is required.")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

VERSION = "1.0.3"

LICENSE = "apache"

setup(
    name="reqe",
    version=VERSION,
    description=(
        "A python network request library that will not throw exceptions"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="ophlr",
    author_email="niushuaibing@foxmail.com",
    maintainer="Eric",
    maintainer_email="niushuaibing@foxmail.com",
    license=LICENSE,
    packages=[
        "reqe"
    ],
    platforms=["all"],
    url="https://github.com/ophlr/reqe",
    install_requires=[
        "requests",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
)
