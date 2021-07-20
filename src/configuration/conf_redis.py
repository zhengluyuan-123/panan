import redis

from configuration.conf_log import get_logger
from configuration.config import get_setting

from utils.paramext import is_any_empty

logger = get_logger(__name__)

def parse_pwd(_redis_setting):
    encryption = _redis_setting.get("encrypted-type")
    encryption = None if is_any_empty(encryption) else encryption
    if encryption is not None:
        # 加密算法
        from configuration.dbsecurity import decrypt_db
        # 加密算法
        pwd = decrypt_db(encryption, _redis_setting)
    else:
        pwd = _redis_setting.get("password", None)

    return pwd


def get_redis_client() -> redis.Redis:
    redis_setting = get_setting("redis")
    assert redis_setting is not None, '请确认正确配置redis文件'
    pwd = parse_pwd(redis_setting)
    if redis_setting.get("use_cluster", False) is False:
        host = redis_setting.get("host")
        port = redis_setting.get("port")
        db = redis_setting.get("db")
        pool = redis.ConnectionPool(host=host, port=port, db=db,)
        return redis.Redis(connection_pool=pool)
    else:
        from rediscluster import RedisCluster
        nodes = redis_setting.get("nodes")
        startup_nodes = [
            {"host":host,"port":port} for host,port in [
                node.split(":") for node in nodes
            ]
        ]
        rc = RedisCluster(startup_nodes=startup_nodes,decode_responses=False,
                          password=pwd, skip_full_coverage_check=True)
        return rc



_redis_conn_pool_client = get_redis_client()


def get_redis_conn() -> redis.Redis:
    return _redis_conn_pool_client