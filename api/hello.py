# api/hello.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello from Vercel Flask API!"})


# Entry for Vercel serverless
def handler(request):
    with app.test_request_context(
        path=request.path,
        method=request.method,
        json=request.get_json(silent=True)
    ):
        return app.full_dispatch_request()
