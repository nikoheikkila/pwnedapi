"""setup module"""
import pwnedapi.meta as meta

from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name=meta.name,
    version=meta.version,
    description=meta.description,
    url=meta.github,
    author=meta.author["name"],
    author_email=meta.author["email"],
    license=meta.license,
    packages=[meta.name],
    include_package_data=True,
    python_requires='>=3.6',
    zip_safe=True,
    keywords=["passwords", "pwned", "security"],
    project_urls={
        "Source Code": meta.github,
        "Twitter": meta.author["twitter"]
    },
    install_requires=meta.dependencies,
    long_description=readme
)
