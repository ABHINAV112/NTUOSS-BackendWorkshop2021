import os
from flask import Flask, request, jsonify
import flask
from pymongo import MongoClient
from bson.objectid import ObjectId


# config requires the following keys
# mongo_uri containing srv to mongodb 
from config import config


app = Flask(__name__)
# CORS(app)

PORT = os.getenv('PORT',8000)


client = MongoClient(config["mongo_uri"])
db = client["workshop-database"]

user_collection = db["Users"]


@app.route("/api", methods=["GET"])
def get():
    return jsonify(request.args.to_dict())

@app.route("/api", methods=["POST"])
def post():
    return jsonify(request.json)


@app.route("/api/user", methods=["GET"])
def get_user_details():
    try:
        url_params = request.args.to_dict()
        user_id = url_params["id"]
        result = user_collection.find_one({"_id":ObjectId(user_id)})
        result["_id"] = str(result["_id"])
        return jsonify(result)
    except:
        return "Exception"

@app.route("/api/user", methods=["POST"])
def add_user():
    try:
        body = request.json
        result = user_collection.insert_one(body).inserted_id
        return str(result)
    except:
        return "Exception"


@app.route("/api/user", methods=["PUT"])
def edit_user():
    try:
        url_params = request.args.to_dict()
        user_id = url_params["id"]
        body = request.json
        result = user_collection.find_one_and_update({"_id":ObjectId(user_id)},
                    {'$set':body})
        return str(result)
    except:
        return "Exception"


@app.route("/api/user", methods=["DELETE"])
def delete_user():
    try:
        url_params = request.args.to_dict()
        user_id = url_params["id"]
        user_collection.find_one_and_delete({"_id":ObjectId(user_id)})
        return "success"
    except:
        return "Exception"

app.run(debug=True, host="0.0.0.0", port=PORT)
