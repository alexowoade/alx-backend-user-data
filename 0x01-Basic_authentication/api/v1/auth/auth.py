#!/usr/bin/env python3
"""Auth class"""
from flask import request
from flask import Flask
from typing import List, TypeVar


class Auth:
    """class for handling auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles auth

        Args:
            path (str):
            excluded_paths (List[str]): _description_

        Returns:
            bool:
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """handle authorization header

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        request = Flask(__name__)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """handle current user

        Returns:
            TypeVar: User
        """
        request = Flask(__name__)
        return None
