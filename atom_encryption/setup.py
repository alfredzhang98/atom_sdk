from setuptools import setup
import os

def get_version():
    version = os.environ.get("PACKAGE_VERSION", "1.2.0")
    return version

if __name__ == "__main__":
    setup(
        version=get_version()
    )
