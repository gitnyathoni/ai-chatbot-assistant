import redis, hashlib, json
class ResponseCache:
    def __init__(self): self.r = redis.Redis()
    def get(self, q): return self.r.get(hashlib.md5(q.encode()).hexdigest())
    def set(self, q, v): self.r.setex(hashlib.md5(q.encode()).hexdigest(), 3600, json.dumps(v))
