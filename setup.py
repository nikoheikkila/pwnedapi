"""setup module"""
from setuptools import setup
from pwnedapi.version import VERSION

with open("README.md") as f:
    readme = f.read()

setup(
    name="pwnedapi",
    version=VERSION,
    description="Library for easily interfacing with Have I Been Pwned API v2",
    url="http://github.com/nikoheikkila/pwnedapi",
    author="Niko Heikkilä",
    author_email="yo@nikoheikkila.fi",
    license="MIT",
    packages=["pwnedapi"],
    include_package_data=True,
    python_requires='>=3.6',
    zip_safe=False,
    keywords=["passwords", "pwned", "security"],
    project_urls={
        "Source Code": "http://github.com/nikoheikkila/pwnedapi",
    },
    install_requires=["requests"],
    long_description=readme
)
