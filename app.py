import os
from flask import Flask, request, jsonify
import flask


app = Flask(__name__)
# CORS(app)

PORT = os.getenv('PORT',8000)

@app.route("/api", methods=["GET"])
def get():
    return jsonify(request.args.to_dict())

@app.route("/api", methods=["POST"])
def post():
    return jsonify(request.json)


@app.route("/api", methods=["PUT"])
def put():
    return jsonify(request.args.to_dict())


@app.route("/api", methods=["DELETE"])
def delete():
    return jsonify(request.args.to_dict())


app.run(debug=True, host="0.0.0.0", port=PORT)
