class PartitionedCache:
    def __init__(self, partitions=3, max_size=100, policy='LRU'):
        self.partitions = [{} for _ in range(partitions)]
        self.max_size = max_size
        self.policy = policy

    def _get_partition(self, key):
        return hash(key) % len(self.partitions)

    def get(self, key):
        partition = self._get_partition(key)
        if key in self.partitions[partition]:
            return self.partitions[partition][key]
        else:
            return None

    def set(self, key, value):
        partition = self._get_partition(key)
        self.partitions[partition][key] = value
