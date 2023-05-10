import redis
from copy import deepcopy 
import json


redis_conn = redis.StrictRedis(host='172.16.216.254', db=11, decode_responses=True)
keys = redis_conn.keys('*CTFR:spider.tasks.send_spider_failed_or_lost_notification*')
for k in keys:
    code = ''
    im = k.split(':')[1].split('.')[-1]
    fr = '.'.join(k.split(':')[1].split('.')[:-1])
    code += 'from ' + fr + ' import ' + im
    values = redis_conn.lrange(k, 0, -1)
    for v in values:
        code_copy = deepcopy(code)
        args = json.loads(v)['args']
        kwargs = json.loads(v)['kwargs']
        code_copy += "\n\n"
        code_copy += f'{im}(*{args}, **{kwargs})'
        print(code_copy)
    print("\n", "*"*100, "\n")
    # redis_conn.delete(k)
