from flask import Flask, request, jsonify
from ai_utils_new import ask_qwen
from flask_cors import CORS  # 新增
import os

app = Flask(__name__)
CORS(app)  # 允许所有来源访问（开发阶段可用）

@app.route('/ask', methods=['POST'])
def chat():
    data = request.get_json()
    print('请求数据',data)
    messages = data.get('messages', [])
    
    if not messages:
        return jsonify({"error": "问题不能为空"}), 400
    
    try:
        answer = ask_qwen(messages)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)