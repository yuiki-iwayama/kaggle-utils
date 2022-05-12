from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="kagutils",
    version="0.0.8",
    packages=find_packages(),
    install_requires=_requires_from_file("requirements.txt")
)