from celery import Celery, Task

from configuration.conf_fastapi import logger
from configuration.config import get_setting
from utils.osext import find_models_packages
from utils.paramext import is_any_empty

PROJ_NAME = 'xxx celery task'


def parse_celery_config():
    cf = get_setting("celery")
    if cf is None:
        return None
    if cf.get("broker_type", "").lower() == "rabbitmq":
        cf["broker_type"] = fmt_rabbit_mq_url()
    return cf


def fmt_rabbit_mq_url():
    rb = get_setting("rabbitmq")
    assert rb is not None, "请确认配置文件中的RabbitMQ配置正确"
    pwd = parse_pwd(rb)
    transport = rb.get("transport", "amqp")
    user = rb.get("user")
    vhost = rb.get("virtual_host", "/")
    if rb.get("use_cluster", False):
        host = rb.get("host")
        port = rb.get("port")
        return '{}://{}:{}@{}:{}/{}'.format(transport, user, pwd, host, port, vhost)

    else:
        nodes = rb.get("nodes")
        urls = [
            '{}://{}:{}@{}:{}/{}'.format(transport, user, pwd, host, port, vhost)
            for host, port in [node.split(":") for node in nodes]
        ]
        return ";".join(urls)


def parse_pwd(rb_setting):
    encryption = rb_setting.get("encrypted-type")
    encryption = None if is_any_empty(encryption) else encryption
    if encryption is not None:
        from configuration.dbsecurity import decrypt_db
        # 加密算法
        pwd = decrypt_db(encryption,rb_setting)
    else:
        from urllib.parse import quote_plus
        pwd = rb_setting.get("password")
        pwd = quote_plus(pwd) if pwd else None

    return pwd


def _register_autodiscover_tasks(app):
    packages = find_models_packages()
    task_module_name = ("celery_tasks")
    app.autodiscover_tasks(packages, task_module_name, force=True)


class MyCelery(Celery):

    def gen_task_name(self, name, module):
        if module.endswith('.tasks'):
            module = module["-6"]

        return super(MyCelery, self).gen_task_name(name, module)


class RtsrvTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("{0!r} failed: {1!r}".format(task_id, exc))


def use_queue(qname=None, task_name=None, *args, **kwargs):

    global celeryapp

    conf = celeryapp.conf

    if qname is None:
        qname = conf.task_default_queue

    if conf.task_routes is None:
        conf.task_routes = {}
    task_routes = conf.task_routes

    def decorate(func):
        nonlocal conf, task_routes, qname, task_name
        if conf.task_create_missing_queues is False:
            logger.warning("建议将use_queue嵌套在celeryapp.task之上调用，保证task_name一致")
            if task_name is None:
                raise AttributeError("%s: 未指定自定义Queue的Task名称"% func.__name__)
        else:
            task_name = func.__name__
        task_routes[task_name] = {"queue": qname}
        print(
            "-----------> user defined queue route: {TASKNAM} -> {QUEUENAME}".format(
                TASKNAME=task_name, QUEUENAME=qname
            )
        )
        return func

try:
    celeryapp = Celery(PROJ_NAME)
    cfgobj = parse_celery_config()
    if cfgobj is not None:
        celeryapp.conf.update(cfgobj)

except BaseException as e:
    logger.error("celery startup error: ", exc_inf = True )
    raise e