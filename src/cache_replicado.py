class ReplicatedCache:
    def __init__(self, max_size=100, policy='LRU'):
        self.cache = {}
        self.max_size = max_size
        self.policy = policy

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        self.cache[key] = value
