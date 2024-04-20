import grpc
import concurrent.futures  # Agregar esta línea
import cache_pb2
import cache_pb2_grpc
import requests

class RickAndMortyServicer(cache_pb2_grpc.RickAndMortyServiceServicer):
    def GetCharacter(self, request, context):
        character_id = request.id
        character_data = self._fetch_character_data(character_id)
        if character_data:
            return cache_pb2.Character(
                id=character_data['id'],
                name=character_data['name'],
                status=character_data['status'],
                species=character_data['species'],
                type=character_data['type'],
                gender=character_data['gender'],
                image=character_data['image']
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Character not found")
            return cache_pb2.Character()

    def _fetch_character_data(self, character_id):
        response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_RickAndMortyServiceServicer_to_server(RickAndMortyServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
