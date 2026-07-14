# sk-ws-H.EDIYLDH.jeuu.MEYCIQDK7zhB2DcoRw7qcp7ZdXUwRZ3s4ZL8jtPjyGNhQ2I3_wIhALcirXIgnCdaJkWtS2QzMHFWLcimqy43I30HTKV-8jul
import requests

# 粘贴你刚复制的sk开头API Key
API_KEY = "sk-ws-H.EDIYLDH.jeuu.MEYCIQDK7zhB2DcoRw7qcp7ZdXUwRZ3s4ZL8jtPjyGNhQ2I3_wIhALcirXIgnCdaJkWtS2QzMHFWLcimqy43I30HTKV-8jul"
# 固定接口地址无需修改
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
# 选用qwen-turbo轻量免费模型
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
    print("输入quit退出对话")
    while True:
        user_text = input("你：")
        if user_text.lower() == "quit":
            break
        print("AI：", chat(user_text), "\n")