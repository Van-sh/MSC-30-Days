import re

def validate_pin(pin):
    return re.fullmatch(r'(\d{6}|\d{4})', pin) != None
