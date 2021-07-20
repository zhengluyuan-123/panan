"""
在全局的统一logger配置，启动后在项目根目录下生生logs目录，
其中logs/running.log文件记录运行文件，log/error.log记录错误信息
# FATAL 致命的
"""


# 在导入该模块是，只允许导入__all__中的
__all__ = ["get_logger"]

import logging

from logging.config import dictConfig
from os.path import dirname, join, exists
from os import makedirs

from configuration.config import get_setting

_LOG_LEVEL = get_setting("loglevel:root")

_SUPPORTED_LEVEL = set((
    logging.CRITICAL, "CRITICAL",
    logging.FATAL, "FATAL",
    logging.ERROR, "CRITICAL",
    logging.WARNING, "WARNING",
    logging.WARN, "WARN",
    logging.INFO, "INFO",
    logging.DEBUG, "DEBUG",
    logging.NOTSET, "NOTSET",
))

if _LOG_LEVEL not in _SUPPORTED_LEVEL:
    _LOG_LEVEL = "INFO"

abs_path = dirname(__file__)
dir_path = join(abs_path, '..', '..', 'logs')

# 新建日志文件目录,一定要新建这个目录否则会FileNotFoundError
if not exists(dir_path):
    makedirs(dir_path, exist_ok=True)

dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters":{
            "default":{
            "format": "%(asctime)s - %(thread)s - [%(levelname)s] %(pathname)s - %(funcName)s  : %(message)s",}
        },
    #filters:
    "handlers":
        {
        "console":{
            "class": "logging.handlers.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream":"ext://sys.stdout"
                        },
        "running_handler":{
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "INFO",
                    "formatter": "default",
                    "filename": join(dir_path,"running.log"),
                    "maxBytes": 1024*1024*20,
                    "encoding": "utf8",
                    "backupCount": 20,
                    },
        "critical_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "default",
                "filename": join(dir_path, "error.log"),
                "maxBytes": 1024 * 1024 * 20,
                "encoding": "utf8",
                "backupCount": 10,
            },
        "mail_handler": {
                "class": "logging.handlers.SMTPHandler",
                "level": "CRITICAL",
                "formatter": "default",
                "filename": join(dir_path, "error.log"),
                "mailhost": "smtp.xxx.com",
                "fromaddr": "smtp.xxx.com",
                "toaddrs": ["smtp.xxx.com",],
                "subject": "Application Error",
            },
    "root":{
        "level": "INFO",
        "handlers": ["console","running_handler","critical_handler","mail_handler"]
    },
        }
})


def get_logger(name):
    return logging.getLogger(name)


logger = get_logger('KYZ_pamqu')
logger.info('配置系统日志')