#!/usr/bin/env python3
'''basic flask app'''
from typing import Tuple
from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    '''basic flask app
    Returns:
        str: JSON payload
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """this method registers new users -> POST /users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        new_user = AUTH.register_user(email, password)
        if new_user is not None:
            return jsonify({
                "email": f"{email}",
                "message": "user created"
            }), 200
    except Exception:
        return jsonify({
            "message": "email already registered"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
