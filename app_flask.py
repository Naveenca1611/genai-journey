from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my DevOps App 🚀"

@app.route("/users")
def users():
    with open("users.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
