import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
#r.set('foo', 'bar')
print r.get('foo')

r.hset('test', ('val1','val2'), (100,200))
