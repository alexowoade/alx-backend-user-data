#!/usr/bin/env python3
'''basic flask app'''
from typing import Tuple
from flask import Flask, jsonify, abort, request
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


@app.route('/users', methods=['POST'])
def register_user() -> Tuple[str, int]:
    """Registers a new user if it does not exist before"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg, 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
