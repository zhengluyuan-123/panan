
import os

from configuration.enums import SUPPORTED_PROFILES


def check_environment(force: bool = False):
    """

    :param force: 为true表示强制检查环境名称,如果环境变量（APOLLO.CLUSTER或DEPLOYMODE）中设置的环境标识不在预定义则抛出异常
    :return:
    """
    env_flag = "APOLLO_CLUSTER"
    env = os.environ.get(env_flag, None)
    if env is None:
        env_flag = "DEPLOYMODE"
        env = os.environ.get(env_flag, None)
    if env is None or env not in SUPPORTED_PROFILES:
        msg = "必须在系统中设置环境变量APOLLO.CLUSTER或DEPLOYMODE，目前可选值{}".format(SUPPORTED_PROFILES)
        if force is True:
            raise (msg)
        else:
            import logging
            logging.warning(msg)
    return env



def get_proj_url_prefix():
    from configuration.config import get_setting
    pre = get_setting("url_prefix")
    if pre is None:
        pre = ""
    elif not pre.startwith("/"):
        pre = "/" + pre
    return pre