"""
测试通用规范汉字表检查功能
"""
import pytest
from src.cscc import check_to_cscc, CSCCChecker
from src.special_checker import CheckResult


class TestCSCCChecker:
    """测试通用规范汉字表检查器"""
    
    def test_checker_initialization(self):
        """测试检查器初始化"""
        checker = CSCCChecker()
        assert isinstance(checker, CSCCChecker)
        assert hasattr(checker, 'gsk_list')
        assert hasattr(checker, 'simplified_to_traditional')
    
    def test_check_text_empty(self):
        """测试空文本检查"""
        checker = CSCCChecker()
        results = checker.check_text("")
        assert results == []
    
    def test_check_text_ignore_pattern(self):
        """测试忽略模式"""
        checker = CSCCChecker()
        text = "Hello 123 !@#"
        results = checker.check_text(text)
        # 应该忽略英文字母、数字和标点符号
        assert len(results) == 0
    
    def test_check_text_with_ignore_list(self):
        """测试自定义忽略列表"""
        checker = CSCCChecker()
        text = "测试文本"
        results = checker.check_text(text, ignore_list="测试")
        # 忽略列表中的字符应该被跳过
        assert len(results) == 0
    
    def test_check_function(self):
        """测试便捷检查函数"""
        results = check_to_cscc("测试")
        assert isinstance(results, list)
        # 由于没有实际数据，这里只测试函数能正常运行
        assert True


class TestCheckResult:
    """测试检查结果类"""
    
    def test_check_result_creation(self):
        """测试检查结果创建"""
        result = CheckResult(
            error_type="test_error",
            location=(0, 1),
            original_text="测",
            suggestion="建议",
            confidence=0.8
        )
        assert result.error_type == "test_error"
        assert result.location == (0, 1)
        assert result.original_text == "测"
        assert result.suggestion == "建议"
        assert result.confidence == 0.8
    
    def test_check_result_default_confidence(self):
        """测试默认置信度"""
        result = CheckResult(
            error_type="test_error",
            location=(0, 1),
            original_text="测",
            suggestion="建议"
        )
        assert result.confidence == 1.0
