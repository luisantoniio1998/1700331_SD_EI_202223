import xmlrpc.server
import requests
import pickle

class BlockInfoServer(xmlrpc.server.SimpleXMLRPCServer):
    def __init__(self, address):
        super().__init__(address, allow_none=True)
        self.register_function(self.get_block_info)
        self.register_function(self.serialize_file)
        self.register_function(self.deserialize_file)

    def get_block_info(self, hash_code):
        url = "https://blockchain.info/rawblock/{}".format(hash_code)
        response = requests.get(url)
        if response.status_code == 200: #200 -- resposta desejada do request

            data = response.json()
            filename = hash_code + ".txt"

            with open(filename, "w") as f:
                f.write(str(data))
            
            return "Informação do bloco guardado em " + filename
        else:
            return "Erro: Não foi possivel obter a informação do bloco desejado"
        
    def serialize_file(self, filename):
        with open(filename, "r") as f:
            file_contents = f.read()
        serialized_file = pickle.dumps(file_contents)
        serialized_filename = filename + ".pickle"
        with open(serialized_filename, "wb") as f:
            f.write(serialized_file)
        return "Ficheiro serializado guardado em : " + serialized_filename

    def deserialize_file(self, serialized_filename):
        with open(serialized_filename, "rb") as f:
            serialized_file = f.read()
        deserialized_file = pickle.loads(serialized_file)
        return "Ficheiro deserializado em : " + deserialized_file
    

server = BlockInfoServer(("localhost", 8000))
print("A receber na porta 8000...")
server.serve_forever()