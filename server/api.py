from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
import json 
import logging

import model
import service

app = Flask(__name__, static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api/v1/user-resources", methods=["POST"])
@cross_origin()
def save_user_resources():
    if not request.json and type(request.json) is list:
        abort(400)

    users = json_to_users(request.json)
    service.save_user_resources(users)
    return jsonify({"status": "success"}), 201

# TODO Change this code to use a lib
def json_to_users(raw_users):
    users = []
    for raw_user in raw_users:
        user = model.User(
            raw_user.get("email"), 
            raw_user.get("first_name"), 
            raw_user.get("last_name"),
            json_to_resources(raw_user.get("resources_to_grant")),
            json_to_resources(raw_user.get("resources_to_revoke"))
        )
        users.append(user)
    return users


def json_to_resources(raw_resources):
    resources = []
    for raw_resource in raw_resources:
        resource = model.Resource(
            raw_resource.get("name"), 
            model.ResourceType[raw_resource.get("type")]
        )
        resources.append(resource)
    return resources


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)