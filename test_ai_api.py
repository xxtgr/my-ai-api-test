import pytest
from api_client import AIClient
from assertions import (
    assert_status_code,
    assert_response_code,
    assert_response_not_empty,
    assert_keyword_in_response
)

# 测试配置
BASE_URL = "http://127.0.0.1:5000"   # 替换成你实际的API地址


@pytest.fixture
def client():
    """fixture：创建客户端并登录"""
    client = AIClient(BASE_URL)
    # 实际使用时替换成真实的用户名密码
    login_resp = client.login("admin", "123456")
    assert_response_code(login_resp, 200)
    return client


# 参数化测试：测试AI问答接口
@pytest.mark.parametrize("question, expected_keyword", [
    ("今天天气怎么样", "天气"),
    ("帮我写一首关于春天的诗", "春"),
    ("1+1等于几", "2"),
    ("讲一个笑话", "笑"),
    ("什么是人工智能", "智能"),
])
def test_ai_chat(client, question, expected_keyword):
    """测试AI问答接口"""
    print(f"\n📝 测试问题: {question}")

    # 调用接口
    response = client.ask_ai(question)

    # 执行断言
    assert_status_code(response, 200)
    assert_response_code(response, 200)
    assert_response_not_empty(response)
    assert_keyword_in_response(response, expected_keyword)

    # 打印回答（调试用）
    answer = response.json().get("data", {}).get("answer", "")
    print(f"🤖 AI回答: {answer[:100]}...")


# 边界条件测试
@pytest.mark.parametrize("question, expected_code", [
    ("", 400),  # 空问题
    ("a" * 10000, 400),  # 超长问题
])
def test_ai_chat_boundary(client, question, expected_code):
    """测试边界条件"""
    response = client.ask_ai(question)
    assert_status_code(response, 200)
    # 注意：实际业务码可能不是400，按实际情况调整
    assert response.json().get("code") == expected_code