import threading

def multiplos(nome, x):
    for i in range(0,20):
        z=nome+str(i*x)+"\n"
        print(z)
    z="\nA thread" + nome + "terminou\n"; 
    print(z)

def soma(nome, x):
    for i in range(0,11):
        z=nome+str(i*x)+ "\n"
        print(z)
    z="\nA thread" + nome + "terminou\n";
    print(z)

x1 = threading.Thread(target=multiplos, args =("t1_mult", 2))
x2= threading.Thread(target=soma, args=("t2_soma", 3))