from os import path
from setuptools import setup


def read_file(file_path):
    with open(path.join(path.dirname(__file__), file_path)) as f:
        return f.read()


setup(
    name="it",
    version="1.0",
    author="Hajime Yamasaki Vukelic",
    author_email="hayavuk@gmail.com",
    description="Higher order operators for functional programming in Python",
    license="BSD",
    keywords="functional programming function operators higher order",
    url="http://example.com",
    long_description=read_file('README.rst'),
)
