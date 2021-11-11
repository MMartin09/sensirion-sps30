import codecs
import os.path
from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="sensirion-sensirion_sps30",
    version=get_version("sensirion_sps30/__init__.py"),
    author="MMartin09",
    author_email="mmartin09@outlook.at",
    description="Sensirion SPS30 Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["sensirion_sps30"],
    url="https://github.com/MMartin09/sensirion-sps30",
    project_urls={
        "Homepage": "https://mmartin09.github.io/pm-dashboard/",
        "Bug Tracker": "https://github.com/MMartin09/sensirion-sps30/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
