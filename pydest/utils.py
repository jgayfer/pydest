import re


def check_alphanumeric(*args):
    """Check arguments are alphanumeric"""
    for arg in args:
        valid = re.match('^[\w-]+$', str(arg))
        if not valid:
            raise ValueError("arguments must consist of alphanumeric characters only")
