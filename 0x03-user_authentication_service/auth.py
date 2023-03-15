#!/usr/bin/env python3
'''athentication'''
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import checkpw
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''hash password
    Args:
        password (str): password
    Returns:
        bytes: hashed password
    '''
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    '''returs a string representation of a new UUID'''
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''registers new users to database
        Args:
            email (str): user email
            password (str): user password
        Returns:
            User: Newly created User
        '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''validates credentials
        Args:
            email (str): user email
            password (str): user email
        Returns:
            bool: True if matches else False
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_password = user.hashed_password
        encoded_password = password.encode()

        if checkpw(encoded_password, user_password):
            return True

        return False
