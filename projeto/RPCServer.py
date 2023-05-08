import xmlrpc.server
import requests

class BlockInfoServer(xmlrpc.server.SimpleXMLRPCServer):
    def __init__(self, address):
        super().__init__(address, allow_none=True)
        self.register_function(self.get_block_info)

    def get_block_info(self, hash_code):
        url = "https://blockchain.info/rawblock/{}".format(hash_code)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open("{}.txt".format(hash_code), "w") as f:
                f.write(str(data))
            return "Informação do bloco guardado em {}.txt".format(hash_code)
        else:
            return "Erro: Não foi possivel obter a informação do bloco desejado"

server = BlockInfoServer(("localhost", 8000))
print("A receber na porta 8000...")
server.serve_forever()