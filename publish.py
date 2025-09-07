#!/usr/bin/env python3
"""
发布脚本 - 用于构建和发布包到PyPI
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, check=True):
    """运行命令并打印输出"""
    print(f"运行命令: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if check and result.returncode != 0:
        print(f"命令失败，退出码: {result.returncode}")
        sys.exit(1)
    
    return result


def clean_build():
    """清理构建文件"""
    print("清理构建文件...")
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"删除目录: {path}")
            elif path.is_file():
                path.unlink()
                print(f"删除文件: {path}")


def build_package():
    """构建包"""
    print("构建包...")
    run_command("python -m build")


def check_package():
    """检查包"""
    print("检查包...")
    run_command("python -m twine check dist/*")


def upload_to_testpypi():
    """上传到测试PyPI"""
    print("上传到测试PyPI...")
    run_command("python -m twine upload --repository testpypi dist/*")


def upload_to_pypi():
    """上传到正式PyPI"""
    print("上传到正式PyPI...")
    run_command("python -m twine upload dist/*")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python publish.py [clean|build|check|test|publish]")
        print("  clean   - 清理构建文件")
        print("  build   - 构建包")
        print("  check   - 检查包")
        print("  test    - 上传到测试PyPI")
        print("  publish - 上传到正式PyPI")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "clean":
        clean_build()
    elif command == "build":
        clean_build()
        build_package()
    elif command == "check":
        build_package()
        check_package()
    elif command == "test":
        clean_build()
        build_package()
        check_package()
        upload_to_testpypi()
    elif command == "publish":
        clean_build()
        build_package()
        check_package()
        upload_to_pypi()
    else:
        print(f"未知命令: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
