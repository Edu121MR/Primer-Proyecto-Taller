import random as r
import time
lista=[0,1,2,3,4]
lista1=[]

def SortLista(lista):
    for i in range(len(lista)):
        random= r.sample(lista,3)
        lista1.append(random)
    return lista1
(SortLista(lista))


def SubLista(index):
    if index < len(lista1):
        print("Memorice la siguiente secuencia...")
        print(lista1[index])
        time.sleep(2)
        print("Ordene los marcadores en el orden que se le indicó!")
        time.sleep(2)
        print (chr(27) + "[2J")


SubLista(1)
