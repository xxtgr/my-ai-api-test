# AI接口自动化测试

用pytest和requests做的AI接口测试小项目。

## 用到了什么

- Python + pytest
- requests（调接口）
- Flask（模拟AI服务）
- pytest-html（测试报告）

## 项目结构

```
- api_client.py    # 接口封装
- assertions.py    # 断言函数
- test_ai_api.py   # 测试用例
- mock_server.py   # Mock服务
- run_tests.py     # 运行入口
```

## 怎么跑

1. 安装依赖
```
pip install pytest requests flask pytest-html
```

2. 启动Mock服务
```
python mock_server.py
```

3. 另开一个终端，运行测试
```
pytest test_ai_api.py -v --html=report.html
```

## 测了什么

- 正常问答（天气、诗歌、数学、笑话、AI概念）
- 边界情况（空输入、超长输入）

共7个用例，全部通过。

## 测试报告

运行后会生成 `report.html`，浏览器打开就能看。
```
