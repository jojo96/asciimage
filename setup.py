# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open("README.md","r") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="asciimage",
    version="3.14159265",
    description="ASCII art Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jojo96/asciimage",
    author="Ujjayanta",
    author_email="ujjayanta.bhaumik.18@ucl.ac.uk",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["asciimage"],
    include_package_data=True,
    install_requires=["Pillow","docx"]
)