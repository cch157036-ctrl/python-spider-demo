"""
调用阿里千问大模型 API
技术点：通过 .env 管理密钥 + requests 调用 LLM 接口
"""

import os
import requests
from dotenv import load_dotenv

# 脚本所在目录，确保 .env 文件和脚本在同一目录，不依赖运行时的当前目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(SCRIPT_DIR, ".env")
load_dotenv(ENV_PATH, override=True)  # override=True 强制用 .env 的值覆盖系统环境变量

API_KEY = os.environ.get("DASHSCOPE_API_KEY")
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
MODEL = "qwen-turbo"


def chat(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    res = requests.post(API_URL, headers=headers, json=body, timeout=30)
    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    else:
        return f"调用失败：{res.text}"


if __name__ == "__main__":
    if not API_KEY:
        print("错误：没有找到 API Key，请检查 .env 文件是否配置了 DASHSCOPE_API_KEY")
        exit()

    print("输入 quit 退出对话")
    while True:
        user_text = input("你：")
        if user_text.lower() == "quit":
            break
        print("AI：", chat(user_text), "\n")
