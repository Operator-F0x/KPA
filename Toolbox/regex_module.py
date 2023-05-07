import re

def regex_password(PSW):
    password_REGEX = r'^[a-zA-Z0-9!"#$&]+$'
    return bool(re.match(password_REGEX, PSW))

