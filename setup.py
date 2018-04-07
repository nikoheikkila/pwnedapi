"""setup module"""
from setuptools import setup, find_packages
import os

from pwnedapi.version import VERSION

setup(
    name="pwnedapi",
    version=VERSION,
    description="Library for easily interfacing with Have I Been Pwned API v2",
    url="http://github.com/nikoheikkila/pwnedapi",
    author="Niko Heikkilä",
    author_email="yo@nikoheikkila.fi",
    license="MIT",
    scripts=[
        "pwnedapi/Password.py"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    zip_safe=False,
    keywords=["passwords", "pwned", "security"],
    project_urls={
        "Source Code": "http://github.com/nikoheikkila/pwnedapi",
    }
)
