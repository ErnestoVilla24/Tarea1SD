import grpc
import cache_pb2
import cache_pb2_grpc

def get_character(stub, character_id):
    response = stub.GetCharacter(cache_pb2.GetCharacterRequest(id=character_id))
    if response.id:
        return response
    else:
        return None

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cache_pb2_grpc.RickAndMortyServiceStub(channel)

    # Ejemplo de uso del cliente gRPC
    character_id = 1
    character = get_character(stub, character_id)
    if character:
        print("Character ID:", character.id)
        print("Name:", character.name)
        print("Status:", character.status)
        print("Species:", character.species)
        print("Type:", character.type)
        print("Gender:", character.gender)
        print("Image:", character.image)
    else:
        print("Character not found.")

if __name__ == '__main__':
    main()
