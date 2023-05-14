import xmlrpc.client

while True:
    print("\n********************************************")
    print("\nSERIALIZAR E DESERIALIZAR BLOCO DE BITCOIN")
    print("\n********************************************")
    print("0. Receber informação de um bloco de bitcoin")
    print("1. Serializar ficheiro com informação do bloco")
    print("2. Deserializar ficheiro com informação do bloco")
    print("3. Sair")
    print("*********************************************\n")
    option = input("Escolha uma opção: ")
    if option == "0":
        hash_code = input("\nDigite o código hash: ")
        server = xmlrpc.client.ServerProxy("http://localhost:8000")
        response = server.get_block_info(hash_code)
        print(response)
    elif option == "1":
        hash_code = input("\nDigite o código hash pretendido :")
        filename = filename = hash_code + ".txt"
        server = xmlrpc.client.ServerProxy("http://localhost:8000")
        response = server.serialize_file(filename)
        print(response)
    elif option == "2":
        hash_code = input("\nDigite o código hash pretendido :")
        server = xmlrpc.client.ServerProxy("http://localhost:8000")
        response = server.deserialize_file(hash_code + ".txt" + ".pickle")
        print(response)
    elif option == "3":
        print("\nA sair do programa...")
        break
    else :
        print("Opção errada, por favor escolha uma opção acima indicada") 

