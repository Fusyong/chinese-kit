# 中文处理工具套件 (Chinese Kit)

**处于模板阶段，不可用**

一个用于中文文本处理的Python工具包，提供多种中文文本处理功能。

## 功能特性

- [x] 对照《通用规范汉字表》检查字符
    - [ ] 繁简转换检查
- [x] 中文字符判断
- [ ] 权威词书词语注音
    - [ ] 加注拼音
- [ ] UTF字符集检查

## 安装

```bash
pip install chinese-kit
```

## 快速开始

### 中文字符判断

```python
from chinese_kit import is_chinese_character

# 判断是否为中文字符
print(is_chinese_character('中'))  # True
print(is_chinese_character('a'))   # False
```

### 通用规范汉字表检查

```python
from chinese_kit import check_to_cscc

# 检查文本中的汉字是否符合通用规范汉字表
text = "这是一段测试文本"
results = check_to_cscc(text)

for result in results:
    print(f"位置 {result.location}: {result.original_text} -> {result.suggestion}")
```

### 高级用法

```python
from chinese_kit import CSCCChecker

# 创建检查器实例
checker = CSCCChecker()

# 检查文本，可以指定忽略的字符
results = checker.check_text("测试文本", ignore_list="测试")

# 处理检查结果
for result in results:
    if result.error_type == 'traditional_character':
        print(f"发现繁体字: {result.original_text} -> {result.suggestion}")
    elif result.error_type == 'variant_character':
        print(f"发现异体字: {result.original_text} -> {result.suggestion}")
    elif result.error_type == 'not_general_standard_kanji':
        print(f"非规范汉字: {result.original_text}")
```

## 开发

### 环境要求

- Python 3.8+

### 安装开发依赖

```bash
pip install -e ".[dev]"
```

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
black src tests
isort src tests
```

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v0.1.0
- 初始版本发布
- 实现中文字符判断功能
- 实现通用规范汉字表检查功能
- 支持繁简转换检查
- 支持异体字检查




