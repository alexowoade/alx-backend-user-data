#!/usr/bin/env python3
'''authentication view'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """handle auth_routes

    Returns:
        _type_: _description_
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})

    if users is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not User.is_valid_password(self, password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = users[0]

    session_id = auth.create_session(user.id)

    user_dict = jsonify(user.to_json())

    session_name = getenv('SESSION_NAME')

    return user_dict.set_cookie(session_name, session_id)
