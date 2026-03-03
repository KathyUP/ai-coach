import requests
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()
def ask_qwen(question: str) -> str:
    """
    调用 Qwen API 回答问题
    :param question: 用户提问
    :return: AI 的回答文本
    """
    API_KEY = os.getenv("QWEN_API_KEY")  # 暂时写死，明天改成 .env
    if not API_KEY:
        raise ValueError("请在 .env 文件中设置 QWEN_API_KEY")

    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-max",
        "input": {
            "messages": [{"role": "user", "content": question}]
        }
    }

    response = requests.post(url, headers=headers, json=data)
    
    if "output" in response.json():
        return response.json()["output"]["text"]
    else:
        error_msg = response.json().get("message", "未知错误")
        raise Exception(f"Qwen API 错误: {error_msg}")