"""
中文处理工具套件安装脚本
"""
from setuptools import setup, find_packages

# 读取README文件
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取版本信息
with open("src/__init__.py", "r", encoding="utf-8") as fh:
    for line in fh:
        if line.startswith("__version__"):
            version = line.split('"')[1]
            break

setup(
    name="chinese-kit",
    version=version,
    author="Fusyong",
    author_email="fusyong@example.com",
    description="常用中文处理工具套件",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fusyong/chinese-kit",
    project_urls={
        "Bug Reports": "https://github.com/fusyong/chinese-kit/issues",
        "Source": "https://github.com/fusyong/chinese-kit",
    },
    packages=find_packages(),
    package_dir={"": "."},
    package_data={
        "src": ["resource/*.json"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=5.0",
            "mypy>=1.0",
        ],
    },
    keywords="chinese, text-processing, character-check, gsk, 汉字, 文本处理",
)
