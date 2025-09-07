"""
测试中文字符判断功能
"""
import pytest
from src.chinese import is_chinese_character


class TestChineseCharacter:
    """测试中文字符判断"""
    
    def test_chinese_character(self):
        """测试中文字符"""
        assert is_chinese_character('中') == True
        assert is_chinese_character('文') == True
        assert is_chinese_character('字') == True
        assert is_chinese_character('符') == True
    
    def test_non_chinese_character(self):
        """测试非中文字符"""
        assert is_chinese_character('a') == False
        assert is_chinese_character('1') == False
        assert is_chinese_character('!') == False
        assert is_chinese_character(' ') == False
        assert is_chinese_character('') == False
    
    def test_edge_cases(self):
        """测试边界情况"""
        # 测试空字符串
        with pytest.raises(IndexError):
            is_chinese_character('')
        
        # 测试多字符字符串（只检查第一个字符）
        assert is_chinese_character('中文') == True
        assert is_chinese_character('abc') == False
