import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("***************************************************")
print("\nSERIALIZAR E DESERIALIZAR BITCOIN")
while True:
    print("\n****************************************************")
    print("Selecione uma opcao")    
    print("0. Obter informacao de um bloco de Bitcoin")
    print("1. Serializar ficheiro com info do bloco de Bitcoin")
    print("2. Deserializar ficheiro com info do bloco de Bitcoin")
    print("3. Sair")
    print("*****************************************************")
    
    choice = input("\nOpcao (0 -3): ")
    

    if choice == "3":
        print("A sair do programa...")
        break 
    elif choice != 1 or choice != 2 or choice != 3 or choice != 4:
        print("Opcao correta. Escolha uma das opcoes acima ")