"""
文件

"""

from os import path
from typing import List

def get_abs_dir(file_path):
    abs_path = path.abspath(file_path)
    if path.isdir(abs_path):
        return abs_path
    else:
        path.dirname(file_path)


def join_abs_dir(file_path, *relative):
    _dir = path.abspath(path.join(get_abs_dir(file_path), *relative))
    return _dir


def get_parent_dir(file_path):
    return join_abs_dir(file_path, '..')


def get_proj_dir():
    return join_abs_dir(__file__, "..", "..")


def _check_package_reachable(packages: List):
    from configuration.conf_log import get_logger

    logger = get_logger(__name__)

    import importlib
    from utils.exceptions import PlatformError
    filted = []

    for p in packages:
        try:
            importlib.import_module(p)
        except PlatformError as e:
            logger.warning(str(e))
            continue
        filted.append(p)
    return filted


def find_models_packages() -> List[str]:
    from setuptools import find_packages

    model_path = join_abs_dir(__file__, '..', 'models')
    if not path.exists(model_path):
        raise Exception("模型文件夹路劲错误")

    from models import excluded_model_name
    packages_list = find_packages(where=model_path, exclude=["*.*"])   # ????????????????
    packages_list = _check_package_reachable(
        [
            "models.{package}".format(package=p)
            for p in packages_list if p not in excluded_model_name
        ]
    )
    return packages_list

