import requests


class AIClient:
    """AI接口客户端封装"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def login(self, username, password):
        """登录接口"""
        url = f"{self.base_url}/api/login"
        data = {
            "username": username,
            "password": password
        }
        response = self.session.post(url, json=data)
        if response.status_code == 200 and response.json().get("code") == 200:
            self.token = response.json().get("data", {}).get("token")
        return response

    def ask_ai(self, question):
        """AI问答接口（需要先登录）"""
        url = f"{self.base_url}/api/chat"
        headers = {
            "Authorization": f"Bearer {self.token}" if self.token else ""
        }
        data = {
            "question": question,
            "temperature": 0.7
        }
        response = self.session.post(url, json=data, headers=headers)
        return response