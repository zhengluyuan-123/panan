#!/user/bin/env python
# -*- coding: utf8 -*-
"""
    @Auther:
    @CreateTime: 2020-8-5 12:32
    @Describe:

    pip install PyYAML
    """

import yaml
import functools

from os import environ
from os.path import join, split
from typing import List
from core.resource import ResourceInfo

from core.web.fastapi_custom import FastAPIRouter
from core.web.flask_custom import FlaskAPIRouter
from utils import osext
from utils.common import check_environment


_web_app = None
_module_routers = []


class Loader(yaml.SafeLoader):

    def __init__(self, stream):
        self._root = split(stream)[0]
        super().__init__(stream)

    def include(self, node):
        filename = join(self._root, self.construct_scalar(node))
        with open(filename, "r", encoding='utf8') as f:
            return yaml.load(f,Loader)

Loader.add_constructor("!include", Loader.include)


@functools.lru_cache()
def read_yaml(file_name):
    """
    @functools.lru_cache()   缓存结果，减少重复的计算
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        config = yaml.load(f, Loader)
    return config



def get_config_file():
    env = check_environment(force=False)
    parent_dir = osext.join_abs_dir(__file__, '..', '..', 'config_files')
    conf_file_default = join(parent_dir,'settings.yml')
    conf_file_env = join(parent_dir,'settings-{ENV}.yml'.format(ENV=env))
    print("enviroment configuration file: " + conf_file_env)
    return conf_file_default,conf_file_env


_ALL_SETTINGS = {
    "defined_in_global_yaml":{},
    "defined_in_model_local":{},
}
default_f, env_f = get_config_file()
_ALL_SETTINGS["defined_in_global_yaml"] = read_yaml(default_f)


def _read_from_local_cache(file_path: str,hierarchical_keys: List[str]):
    global _ALL_SETTINGS
    settings = _ALL_SETTINGS["defined_in_global_yaml"].setdefault(file_path, read_yaml(file_path))
    return _read_from_config_file(settings, hierarchical_keys)



def _read_from_global_cache(file_path: str,hierarchical_keys: List[str]):
    global _ALL_SETTINGS
    settings = _ALL_SETTINGS["defined_in_model_local"].setdefault(file_path, read_yaml(file_path))
    return _read_from_config_file(settings, hierarchical_keys)



def _read_from_config_file(settings: dict,hierarchical_keys: List[str]):
    for key in hierarchical_keys:
        settings = settings.get(key)
    return settings



# 使用了apollos
def get_setting(
        partition: str,
        default: str = None,
        from_local: ResourceInfo = None,
):
    """

    :param partition: 分割
    :param default:
    :return:
    """
    environ_var = partition.replace(":", "-")
    settings = environ.get(environ_var, None)
    if settings is None:
        settings = environ.get(environ_var.upper(), None)
    if settings is not None:
        return settings
    hierarchical_keys = partition.split(":")
    if from_local is not None:
        config_file_path = from_local.get_resource()
        try:
            settings = _read_from_local_cache(config_file_path,hierarchical_keys)
        except AttributeError:
            pass
        else:
            return settings
    try:
        settings = _read_from_global_cache(hierarchical_keys)
    except AttributeError as e:
        settings = default
        print(f"Not Foung Key '{partition}' in configuration files: " + str(e))
    else:
        if settings is None:
            settings = default
    return settings



 # ?????问什么是列表
def get_app() -> List[object]:
    global _web_app
    return _web_app


# ????? 设置全局app，只创建一个
def register_app(app):
    global _web_app
    if not _web_app:
        _web_app=app
    return _web_app


def register_routers(router, *args, **kwargs):
    global _module_routers
    _module_routers.append([router, args, kwargs])


def get_routers():

    global _module_routers
    return _module_routers


def create_api(name, url_prefix, *args, **kwargs):
    app = get_app()
    try:
        from flask import Flask

        if isinstance(app,Flask):
            router = FlaskAPIRouter(
                name=name,
                import_name = kwargs.get("import_name", name),
                url_prefix = url_prefix,
            )
            register_routers(router, *args, **kwargs)
            return router
    except ImportError:
        pass

    try:
        from fastapi import FastAPI

        if isinstance(app, FastAPI):
            router = FastAPIRouter()
            register_routers(router, prefix=url_prefix, *args, **kwargs)
            return router
    except ImportError:
        pass

    raise Exception('只支持Flask和FastAPI组件')

def get_prog_instance_dir():

    return osext.join_abs_dir(__file__, "..", "..")


if __name__ == '__main__':
    print(check_environment())