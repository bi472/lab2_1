import re

def test_regular(str):
    reg = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    return re.search(reg, str);