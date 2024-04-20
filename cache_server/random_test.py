import requests
import json
import random
from cache_clasico import ClassicCache
from cache_replicado import ReplicatedCache
from cache_particionado import PartitionedCache
from metrics import save_metrics

def run_random_tests(cache_type, policy):
    cache = None
    if cache_type == "classic":
        cache = ClassicCache(policy=policy)
    elif cache_type == "replicated":
        cache = ReplicatedCache(policy=policy)
    elif cache_type == "partitioned":
        cache = PartitionedCache(policy=policy)
    
    hits = 0
    misses = 0

    for _ in range(50):
        character_id = random.randint(1, 671)  # IDs de personajes en la API de Rick and Morty
        if cache.get(character_id) is not None:
            hits += 1
        else:
            response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
            character_data = json.loads(response.text)
            cache.set(character_id, character_data)
            misses += 1

    save_metrics(cache_type, policy, hits, misses)

if __name__ == "__main__":
    run_random_tests("classic", "LRU")
    run_random_tests("classic", "MRU")
    run_random_tests("replicated", "LRU")
    run_random_tests("replicated", "MRU")
    run_random_tests("partitioned", "LRU")
    run_random_tests("partitioned", "MRU")
