from setuptools import setup, find_packages
import os

# Utility function to read the README file.
def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Long description not available"

setup(
    name="WAdatabase",
    version="0.0.1",
    author="alfred",
    author_email="alfred.zhang98@gmail.com",
    description="A package for reading different kinds of database",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/alfredzhang98/atom_sdk.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: SDK",
        "Development Status :: 1 - Beta",
        # "Development Status :: 5 - Production/Stable",

        # 如果你的包是为网络开发设计的，你可能会使用如下的环境标记
        # "Framework :: Django"
        # "Framework :: Flask"
        # "Environment :: Web Environment"

        # 科学计算或数据分析设计
        # Intended Audience :: Science/Research
        # Topic :: Scientific/Engineering
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'pymysql>=1.1',
    ],
)