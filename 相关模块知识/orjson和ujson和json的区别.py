# -*- coding: utf-8 -*-
import json
import ujson
import orjson
import time


def cost_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        # print(result)
        return result

    return inner


a = {}
for i in range(1, 100000000):
    a[str(i)] = 1


@cost_time
def json_dumps(obj):
    return json.dumps(obj)


@cost_time
def ujson_dumps(obj):
    return ujson.dumps(obj)


@cost_time
def orjson_dumps(obj):
    return orjson.dumps(obj)


r1 = json_dumps(a)
r2 = ujson_dumps(a)
r3 = orjson_dumps(a)

# 结果

# 130.38414025306702

# 42.63353109359741

# 7.99960470199585