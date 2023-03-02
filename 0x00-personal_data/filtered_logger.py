#!/usr/bin/env python3
"""Personal data project"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    '''implement data filter'''
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
