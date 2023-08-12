import re


def to_underscore(s: str):
    s = re.sub(r'[^\w\s]', '', s)
    return '_'.join([ss.lower() for ss in s.split()])

