#!/usr/bin/python3
"""Flask API with basic endpoints and POST functionality"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage of users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return API status"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user object if exists, else 404"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create new user
    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
