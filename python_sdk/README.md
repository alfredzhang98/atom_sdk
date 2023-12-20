# 核心注意

文件目录结构
1. xxx_SDK
	1. SDK
		1. "__init__. py"
		2. xxx. py
	2. Data/Setting
		1. xxx. xxx
	3. LICENSE
	4. MANIFEST. in
	5. README. md
	6. requirements. txt
	7. setup. py

>Tips: SDK name in the setup.py file should be same as the file 1 in the second level
# 文件准备
## 文件 1 init 文件
```python

# __init__.py
from .read_files import SDK
from .read_files import SDK.xxx

__version__ = '0.0.1'
__all__ = ['SDK', 'xxx']

```

## 文件 2 setup 文件

``` python

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
    name="SDK",
    version="0.0.1",
    author="xxx",
    author_email="xxx@gmail.com",
    description="A package for reading YAML and JSON and so many other kinds of files",
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
    # Include any package inside your package containing *.yaml and *.json files
    package_data={
        '': ['data/*.xxx'],  # Adjust the pattern to match where your json files are.
    },
    include_package_data=True,
	install_requires=[
        'xxx>=xx.xx',
    ],
)

# entry_points={
#     'console_scripts': [
#         'SDK_main=SDK.[要调的py模块名称]:main',  # Assumes a main function in read_files.py for entry point
#     ],
# },

# def main():
#     # 函数内容
#     print("Executing ReadFiles...")

```

### 版本说明

- **主版本号**：当你做了不兼容的 API 修改时，增加主版本号。
- **次版本号**：当你以向后兼容的方式添加功能时，增加次版本号。
- **修订号**：当你进行向后兼容的问题修正时，增加修订号。


## 文件 3 License

[[License]]
## 文件 4 Readme. md

README. md

```markdown

# Read Files Package
This package provides a simple interface for xxx. It is designed to be easy to use and integrate into larger Python applications.

## Installation
To install the package, run the following command:

```bash
pip install SDK.whl

```

## 文件 4 requirement （非必须）

`install_requires` 中指定了运行库所需的最小依赖，同时在 `requirements.txt` 中为开发环境指定了额外的依赖（如测试库和构建工具）

```txt
xxx >= xx.xx

```


## 文件 6 MANIFEST. in

MANIFEST. In

```shell

# Include the xxx files from the data directory
recursive-include data *.xxx

# Include the README
include README.md

# Include other important files such as LICENSE, requirements.txt if they exist
include LICENSE
include requirements.txt

```


## 测试文件（待完善）

# 开始打包

``` shell

# 清理之前的构建输出
python setup.py clean --all

# 生成源代码分发包
python setup.py sdist
python setup.py bdist_egg #（过时）

# 构建 wheel 包 !!!
python setup.py bdist_wheel

```


# 上传 PyPI

```shell

pip install twine

twine upload dist/*

# 确保在上传之前，你已经在 PyPI 上注册了相应的项目名称，并且你的 `.pypirc` 文件（通常位于你的主目录下）已经正确设置

```

[[pypirc说明]]

# 使用包（安装过程）

```shell

# setup 安装
python setup.py install

# 注意路径
pip install *.whl

# PyPI
pip install SDK


```