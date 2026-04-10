from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)


# ==================== Mock登录接口 ====================
@app.route('/api/login', methods=['POST'])
def login():
    """模拟登录接口"""
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    # 模拟不同场景的返回
    if username == "" or password == "":
        return jsonify({
            "code": 400,
            "msg": "用户名或密码不能为空",
            "data": None
        }), 200

    if username == "admin" and password == "123456":
        return jsonify({
            "code": 200,
            "msg": "登录成功",
            "data": {
                "token": "mock-token-" + str(int(time.time())),
                "username": "admin"
            }
        }), 200
    else:
        return jsonify({
            "code": 401,
            "msg": "用户名或密码错误",
            "data": None
        }), 200


# ==================== Mock AI问答接口 ====================
@app.route('/api/chat', methods=['POST'])
def chat():
    """模拟AI问答接口 - 带延迟和随机性"""

    # 1. 获取请求头中的token（验证登录状态）
    auth_header = request.headers.get('Authorization', '')
    if not auth_header or 'Bearer' not in auth_header:
        return jsonify({
            "code": 401,
            "msg": "未登录或token已失效",
            "data": None
        }), 200

    # 2. 获取请求参数
    data = request.get_json()
    if not data:
        return jsonify({
            "code": 400,
            "msg": "请求参数不能为空",
            "data": None
        }), 200

    question = data.get('question', '')
    temperature = data.get('temperature', 0.7)

    # 3. 边界条件测试
    if question == "":
        return jsonify({
            "code": 400,
            "msg": "问题不能为空",
            "data": None
        }), 200

    if len(question) > 1000:
        return jsonify({
            "code": 400,
            "msg": "问题长度超过限制(1000字符)",
            "data": None
        }), 200

    # 4. 模拟AI处理延迟（0.5-2秒，可测试超时场景）
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)

    # 5. 根据关键词返回不同的回答（用于测试参数化）
    if "天气" in question:
        answer = "今天北京天气晴朗，气温18-25℃，适合出行。"
    elif "诗" in question or "诗歌" in question:
        answer = "《春日》\n春水初生乳燕飞，\n黄蜂小尾扑花归。\n窗含远色通书幌，\n鱼拥香钩近石矶。"
    elif "笑话" in question:
        answer = "为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 = Dec 25！"
    elif "人工智能" in question or "AI" in question:
        answer = "人工智能（AI）是计算机科学的一个分支，致力于创建能够执行通常需要人类智能的任务的系统。"
    elif "1+1" in question or "等于" in question:
        answer = "1+1等于2"
    else:
        # 模拟AI的随机性（同个问题可能得到不同答案）
        random_answers = [
            f"这是一个关于「{question}」的问题。",
            f"感谢你的提问，关于「{question}」，我的理解是...",
            f"「{question}」是个很好的问题，让我想想。"
        ]
        answer = random.choice(random_answers)

    # 6. 返回成功响应
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": {
            "answer": answer,
            "question": question,
            "temperature": temperature,
            "response_time": round(delay, 2)
        }
    }), 200


# ==================== 健康检查接口 ====================
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "AI Mock Server"})


# ==================== 启动服务器 ====================
if __name__ == '__main__':
    print("=" * 50)
    print("🚀 AI Mock Server 启动成功！")
    print("📡 访问地址: http://127.0.0.1:5000")
    print("📋 可用接口:")
    print("   POST /api/login  - 登录接口")
    print("   POST /api/chat  - AI问答接口")
    print("   GET  /health    - 健康检查")
    print("=" * 50)
    app.run(host='127.0.0.1', port=5000, debug=True)