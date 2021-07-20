__all__ = ["get_db_engines"]

import os

from urllib.parse import quote_plus
from sqlalchemy import event,exc,engine_from_config

from configuration.conf_log import get_logger
from configuration.config import get_setting
from utils.paramext import is_any_empty

logger = get_logger(__name__)

def _init_db_engines():
    db_settings: dict = get_setting(partition="db")
    engines = {}
    for name,setting in db_settings.items():
        if setting.get('enabled', True) is False:
            continue
        pwd, dburl = None, setting.get("sqlalchemy-url", None)
        encryption = setting.get("encrypted-type")
        encryption = None if is_any_empty(encryption) else encryption
        if encryption is not None:
            from configuration.dbsecurity import decrypt_db
            # 加密算法
            pwd = decrypt_db(encryption, setting)
            dburl = None
        elif dburl is None:
            pwd = quote_plus(setting.get("password"))

        if dburl is None:
            protocol = setting.get("db_protocol")
            user = setting.get("user")
            host = setting.get("host")
            prot = setting.get("prot")
            dbname = setting.get("dbname")
            charset = setting.get("charset", None)
            if is_any_empty(user,host,prot,dbname):
                raise KeyError(" 需要在配置文件指明：user host prot dbname")
            dburl = "{DBTYPE}://{USER}:{PWD}@{HOST}:{PORT}/{DBNAME}{CHARSET}".format(
                DBTYPE=protocol, USER=user, PWD=pwd, HOST=host, PORT=prot, DBNAME=dbname,
                CHARSET=charset
            )
            setting["sqlalchemy-url"] = dburl
        engine = engine_from_config(setting, prefix="sqlalchemy-")
        event.listens_for(engine, "connect")(connect)
        event.listens_for(engine, "checkout")(checkout)
        engines[name] = engine

    logger.info("createed database engines:{}".format(engines))

    test_connection(engines)
    return engines



def connect(adapi_connection, connection_record):
    connection_record.info["pid"] = os.getpid()


def checkout(adapi_connection, connection_record, connection_proxy):
    pid = os.getpid()
    if connection_record.info["pid"] != pid:
        connection_record.connection = connection_proxy.connection = None
        raise exc.DisconnectionError("Connection record belongs to pid {}".format(pid))

def get_db_engines():
    global _ALL_ENGINES
    db_engines = _ALL_ENGINES
    return db_engines

def test_connection(engines):

    for name,engine in engines.items():
        connection = engine.connect()
        connection.close()


_ALL_ENGINES = _init_db_engines()