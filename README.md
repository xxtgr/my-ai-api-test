# AI API 自动化测试框架

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-9.0+-blue.svg)](https://pytest.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

## 📖 项目简介

本项目是一个针对AI接口的自动化测试框架，支持：
- AI问答接口的功能测试
- 接口封装与断言管理
- 数据驱动测试（参数化）
- 可视化测试报告生成
- 本地Mock Server模拟AI行为

## 🛠️ 技术栈

| 技术 | 用途 |
| :--- | :--- |
| Python 3.10 | 主编程语言 |
| pytest | 测试框架 |
| requests | HTTP请求 |
| Flask | Mock Server |
| pytest-html | 测试报告 |

## 📁 项目结构
ai-api-test-framework/
├── api_client.py # API客户端封装
├── assertions.py # 公共断言函数
├── test_ai_api.py # pytest测试用例
├── mock_server.py # Flask Mock服务
├── run_tests.py # 测试运行入口
├── report.html # 测试报告（生成）
└── README.md # 项目说明
