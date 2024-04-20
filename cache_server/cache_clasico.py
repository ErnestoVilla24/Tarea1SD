from collections import OrderedDict

class ClassicCache:
    def __init__(self, max_size=100, policy='LRU'):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.policy = policy

    def get(self, key):
        if key in self.cache:
            if self.policy == 'LRU':
                self.cache.move_to_end(key)
            elif self.policy == 'MRU':
                self.cache.move_to_beginning(key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            if self.policy == 'LRU':
                self.cache.move_to_end(key)
            elif self.policy == 'MRU':
                self.cache.move_to_beginning(key)
        else:
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
            self.cache[key] = value
