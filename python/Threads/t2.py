import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

def multiplos(nome, x):
    for i in range(0,20):
        z=nome+str(i*x)+"\n"
        print(z)
    z="\nA thread" + nome + "terminou\n"
    print(z)

def soma(nome, x): 
    for i in range(0, 11):
        z=nome+str(i+x)+"\n"
        print(z)
    z="\nA thread" + nome + "terminou\n"
    print(z)

    executor = ThreadPoolExecutor(max_workers=4)
    executor.submit(multiplos("t1-mullt",2))
    executor.submit(multiplos("t2-mult",3))
    executor.submit(multiplos("t3-sum",5))
    executor.submit(multiplos("t4-sum",7))