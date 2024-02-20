from setuptools import setup, find_packages
from webshotapi.version import __version__
import os


ROOT_PATH = os.path.dirname(__file__)
PKG_NAME = "webshotapi"
PKG_PATH = os.path.join(ROOT_PATH, PKG_NAME.replace("-", "_"))


with open('README.md','r') as r:
    long_description = r.read()

with open('requirements.txt', 'r') as r:
    requirements = r.readlines()

setup(
    name='webshotapi',
    version=__version__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    author="WebShotApi.com",
    author_email="contact@webshotapi.com",
    description="Api client for WebShotApi.com. \
        Website screenshot api client, \
        extract html from rendered website \
        extract words with coordinates from website, \
        extract styles from HTML selectors(elements)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://webshotapi.com/clients/python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/webshotapi/website-screenshot-python-client/issues",
        "Documentation": "https://webshotapi.com/docs/python/",
        "Source Code": "https://github.com/webshotapi/website-screenshot-python-client",
    },
    license="MIT",
    python_requires='>=3.8',
)