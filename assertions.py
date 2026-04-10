def assert_status_code(response, expected_code):
    """断言HTTP状态码"""
    assert response.status_code == expected_code, \
        f"期望状态码{expected_code}，实际{response.status_code}"
    print(f"✅ 状态码验证通过: {expected_code}")

def assert_response_code(response, expected_code):
    """断言业务code"""
    actual_code = response.json().get("code")
    assert actual_code == expected_code, \
        f"期望业务码{expected_code}，实际{actual_code}，错误信息: {response.json().get('msg')}"
    print(f"✅ 业务码验证通过: {expected_code}")

def assert_response_not_empty(response):
    """断言响应不为空"""
    data = response.json()
    assert data is not None, "响应内容为空"
    print("✅ 响应不为空验证通过")

def assert_keyword_in_response(response, keyword):
    """断言响应中包含指定关键词"""
    response_text = str(response.json())
    assert keyword in response_text, \
        f"期望响应中包含'{keyword}'，实际响应: {response_text[:200]}"
    print(f"✅ 关键词验证通过: '{keyword}'")