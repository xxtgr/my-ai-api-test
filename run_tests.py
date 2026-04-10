import pytest
import sys

if __name__ == "__main__":
    # 运行所有测试并生成报告
    args = [
        "test_ai_api.py",           # 测试文件
        "-v",                        # 详细输出
        "--html=report.html",        # 生成HTML报告
        "--self-contained-html",     # 报告独立（不依赖外部文件）
    ]
    sys.exit(pytest.main(args))