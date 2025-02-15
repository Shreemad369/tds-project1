from flask import Flask, request, jsonify
import os
import subprocess
from pathlib import Path
import openai

app = Flask(__name__)
DATA_DIR = "/data"
AIPROXY_TOKEN = os.environ.get("AIPROXY_TOKEN")

# Set up OpenAI API key
openai.api_key = AIPROXY_TOKEN
openai.api_base = "https://api.aiproxy.io/v1"

def sanitize_path(user_path):
    """Ensure paths stay within allowed directories or specific exceptions."""
    safe_path = Path(DATA_DIR) / user_path
    print(f"Sanitizing path: {safe_path}")  # Debugging line
    
    if not str(safe_path).startswith(DATA_DIR):
        raise ValueError("Path traversal attempt detected")
    
    return safe_path


@app.route('/run', methods=['POST'])
def execute_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task description is missing"}), 400

    try:
        # Use OpenAI GPT-4o-Mini to parse and execute the task
        response = openai.ChatCompletion.create(
             model="gpt-4o-mini",
             messages=[
                  {"role": "user", "content": task}
                  ],
                  max_tokens=200,
                  )
        llm_output = response["choices"][0]["message"]["content"]



        # Here you can add logic to process the LLM's output and execute tasks.
        return jsonify({"status": "success", "output": llm_output}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/read', methods=['GET'])
def read_file():
    path = request.args.get('path')
    if not path:
        return "Path parameter is required", 400

    try:
        sanitized_path = sanitize_path(path)
        with open(sanitized_path, 'r') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

