import re

def check_mail(str): 
    pattern=r"^\w+[@][a-z]{2,6}(\.[a-z]{2,4}){1,2}$"
    number=re.compile(pattern)
    return bool(number.findall(str))

def check_phone(str):
    pattern=r"^[+]{1}[0-9]{1} [(]{1}[0-9]{3}[)]{1} [0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$"
    number=re.compile(pattern)
    return bool(number.findall(str))

