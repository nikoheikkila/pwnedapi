#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from shutil import rmtree
from setuptools import find_packages, setup, Command

# Meta-data
NAME = "pwnedapi"
DESCRIPTION = "Library for easily interfacing with Have I Been Pwned API v2."
URL = "https://github.com/nikoheikkila/pwnedapi"
EMAIL = "yo@nikoheikkila.fi"
AUTHOR = "Niko Heikkilä"
REQUIRES_PYTHON = ">=3.5.0"
VERSION = None

# Required packages
REQUIRED = ["requests", "tablib"]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding="utf-8") as f:
    long_description = "\n" + f.read()

about = {}

if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload"""

    description = "Builds and publishes the package."
    user_options = []

    @staticmethod
    def status(s):
        """Bolds given text"""
        print("\033[1m{}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building source and wheel (universal) distribution")
        os.system("{} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{}".format(about['version']))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    cmdclass={"upload": UploadCommand},
)
