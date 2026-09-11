from flask import Flask, request, jsonify
from agents import run_agent

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    task = data.get("task")

    if not task:
        return jsonify({
            "error": "No task provided"
        }), 400

    result = run_agent(task)

    return jsonify({
        "task": task,
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)