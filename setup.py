import io
from setuptools import setup, find_packages

requirements = ["requests"]

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

setup(
    name="ipgeocache",
    version="0.1.0",
    url="https://github.com/seanbreckenridge/ipgeocache",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description=("""a small cache layer for geolocation info for IP addresses"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["ipgeocache"]),
    install_requires=requirements,
    keywords="",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)