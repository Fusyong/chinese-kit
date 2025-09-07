"""
中文处理工具套件

一个用于中文文本处理的Python工具包，包含通用规范汉字表检查等功能。
"""

from .chinese import is_chinese_character
from .cscc import check_to_cscc, CSCCChecker
from .special_checker import CheckResult

__version__ = "0.1.0"
__author__ = "Fusyong"
__email__ = "fusyong@example.com"

__all__ = [
    "is_chinese_character",
    "check_to_cscc", 
    "CSCCChecker",
    "CheckResult"
]
