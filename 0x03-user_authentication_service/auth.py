#!/usr/bin/env python3
'''athentication'''
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    '''hash password
    Args:
        password (str): password
    Returns:
        bytes: hashed password
    '''
    return hashpw(password.encode('utf-8'), gensalt())
