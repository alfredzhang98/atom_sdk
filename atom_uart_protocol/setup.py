from setuptools import setup
import os

def get_version():
    version = os.environ.get("PACKAGE_VERSION", "0.0.1")
    return version

if __name__ == "__main__":
    setup(
        version=get_version()
    )
