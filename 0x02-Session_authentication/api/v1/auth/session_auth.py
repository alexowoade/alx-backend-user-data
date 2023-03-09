#!/usr/bin/env python3
"""Implement Session Authentication"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''defines methods and attributes for implementing
    session authentication'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a session ID for a user_id

        Args:
            user_id (str, optional): User id. Defaults to None.

        Returns:
            str: a uuid for user
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
