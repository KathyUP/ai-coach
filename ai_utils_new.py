# ai_utils.py
import os
from http import HTTPStatus
import dashscope

# 设置 API Key（确保环境变量已配置）
dashscope.api_key = os.getenv("QWEN_API_KEY")  # 或直接写死（不推荐）

def ask_qwen(messages):
    """
    支持多轮对话的 Qwen 调用
    :param messages: List[Dict], e.g. [{"role": "user", "content": "..."}]
    :return: str, AI 的回答
    """
    response = dashscope.Generation.call(
        model='qwen-max',          # 也可以用 qwen-plus / qwen-turbo
        messages=messages,         # ← 关键：传 messages
        result_format='message'    # ← 必须加！否则返回格式不同
    )

    if response.status_code == HTTPStatus.OK:
        # 注意：result_format='message' 时，内容在这里
        return response.output.choices[0].message.content
    else:
        # 抛出详细错误，方便调试
        raise Exception(
            f"Qwen API Error {response.status_code}: "
            f"{response.code} - {response.message}"
        )