
from os import environ

from utils.paramext import parse_bool

_apollo_enabled = parse_bool(environ.get("APOLLO_ENABLE", False))