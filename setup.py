"""
This module handles the setup configuration for the project.

It defines the necessary metadata such as project name, version, author,
and dependencies required for installation.

Example usage:
    $ python setup.py install

For more information, visit http://www.maximeblouin.com.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Investment Problems In Python",
    version="1.0.0",
    description="Investment Problems In Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Maxime Blouin",
    author_email="maxime.blouin@live.ca",
    keywords=["Investing"],
    url="http://www.maximeblouin.com",
    python_requires=">=3.10",  # Specify a minimum required Python version
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    # List of packages included in the distribution
    packages=["problems"],
    # List any dependencies required by your package
    install_requires=[
        "pandas>=2.2.1",
        "QuantLib>=1.33",
        "sympy>=1.12",
    ],
)
