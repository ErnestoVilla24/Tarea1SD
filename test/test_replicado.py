import requests
import json
from cache_replicado import ReplicatedCache

def test_cache_with_api():
    cache = ReplicatedCache()

    for character_id in range(1, 51):
        # Hacemos una solicitud a la API de Rick and Morty para obtener datos de un personaje específico
        response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
        character_data = json.loads(response.text)

        # Guardamos los datos del personaje en el caché
        cache.set(character_id, character_data)

        # Verificamos si los datos se han almacenado correctamente en el caché
        assert cache.get(character_id) == character_data

if __name__ == "__main__":
    test_cache_with_api()
    print("Pruebas pasadas.")
