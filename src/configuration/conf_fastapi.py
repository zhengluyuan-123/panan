#!/user/bin/env python
# -*- coding: utf8 -*-

import importlib

from fastapi import FastAPI, APIRouter

from configuration import config
from configuration.conf_log import get_logger
from core.web.fastapi_responses import KYZDefaultResponseJson
from utils import osext


logger = get_logger(__name__)


def register_api_router(api_router):
    # 为什么单独注册这个？？  monitor ： 监视器，显示屏 ---- 做日志
    importlib.import_module("core.monitor.api")
    model_list = osext.find_models_packages()
    for module_name in model_list:
        try:
            module = importlib.import_module("{package}.api".format(package=module_name))
            logger.info('加载了模块：%s' % module_name)
            if hasattr(module, config.create_api.__name__):
                logger.info("向FastAPI注册了路由")
            else:
                logger.warning("{}没有实现注册路由".format(module_name))
        except ModuleNotFoundError as e:
            logger.warning(f"{str(e)}:没有找到！！！！")

    else:
        # 获取所有的路由
        module_routers = config.get_routers()
        for router, args, kwargs in module_routers:
            api_router.include_router(router, prefix=kwargs["prefix"], tags=kwargs.get["tags"])

def create_app(config_obj: object = None, debug: bool = False):
    from configuration.config import get_setting,register_app
    app = FastAPI(debug=debug, default_response_class=KYZDefaultResponseJson)
    api_router = APIRouter()
    register_app(app)
    register_api_router(api_router)
    app.include_router(api_router, prefix="{}".format(get_proj_url_prefix()))

    pass