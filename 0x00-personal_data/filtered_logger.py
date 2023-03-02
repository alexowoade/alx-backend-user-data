#!/usr/bin/env python3
"""Personal data project"""
from re import sub


def filter_datum(
        fields: list[str], redaction: str,
        message: str, separator: str
) -> str:
    """a basic data filter

    Args:
        fields (list[str]): list of strings representing
        all fields to obfuscate

        redaction (str): string representing by what the
        field will be obfuscated

        message (str): string representing the log line

        separator (str):  string representing by which character is separating
        all fields in the log line (message)

    Returns:
        str: the log message obfuscated:
    """
    for field in fields:
        message = sub(f'{field}=.*?{separator}',
                      f'{field}={redaction}{separator}', message)
    return message
