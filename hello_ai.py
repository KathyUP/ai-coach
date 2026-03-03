import requests

# 替换成你的 Qwen API Key
API_KEY = "sk-cbdfd40ee3d94650bc865e9c17f0afdc"

url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": "qwen-max",  # 也可以用 qwen-plus（便宜）或 qwen-turbo（快）
    "input": {
        "messages": [{"role": "user", "content": "什么水果最好吃"}]
    }
}

response = requests.post(url, headers=headers, json=data)

# print("Response:", response.json())

# ✅ Qwen 的返回结构是 output.text，不是 choices
if "output" in response.json():
    content = response.json()["output"]["text"]
    print("✅ AI 回答：", content)
else:
    print("❌ 错误：", response.json().get("message", "未知错误"))