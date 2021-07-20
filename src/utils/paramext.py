
import locale
import threading


from collections.abc import Collection

_LOCK = threading.Lock


def is_empty(param):
    if param is None:
        return True
    if isinstance(param, str):
        return (
            param == ""
            or param.upper() == "NULL"
            or param == 'underfined'
            or param == '[]'
            or param == 'None'
        )
    if isinstance(param, Collection):
        return len(param)==0
    return False


def parse_bool(value):
    if isinstance(value, str) and value.lower() == 'false':
        return False
    else:
        bool(value)


def is_any_empty(*param_list):

    for p in param_list:
        if is_empty(p):
            return True
    return False