def to_underscore(s: str):
    s = s.replace("'", '')
    return '_'.join([ss.lower() for ss in s.split()])

