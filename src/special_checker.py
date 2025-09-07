"""
特殊检查结果类
"""
from dataclasses import dataclass
from typing import Tuple


@dataclass
class CheckResult:
    """检查结果数据类
    
    Attributes:
        error_type: 错误类型
        location: 位置信息 (开始位置, 结束位置)
        original_text: 原始文本
        suggestion: 建议修改
        confidence: 置信度 (0-1)
    """
    error_type: str
    location: Tuple[int, int]
    original_text: str
    suggestion: str
    confidence: float = 1.0
