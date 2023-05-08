import xmlrpc.client

def menu():
    print("Serializar e Deserializar bloco Bitcoin")
    print("********************************************")
    print("0. Receber informação de um bloco de bitcoin")
    print("1. Serializar ficheiro com informação do bloco")
    print("2. Deserializar ficheiro com informação do bloco")
    print("*********************************************")
    option = input("Enter an option: ")
    if option == "0":
        hash_code = input("Enter the hash code: ")
        server = xmlrpc.client.ServerProxy("http://localhost:8000")
        response = server.get_block_info(hash_code)
        print(response)

menu()
