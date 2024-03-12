import random as r
import time
import ARMem as ar
lista=[0,1,2,3,4]

lista1=[]

def SortLista(lista):
    for i in range(len(lista)):
        random= r.sample(lista,2)
        lista1.append(random)
    return lista1
#(SortLista(lista))

def SubLista(index):
    tiempo_total=0
    for x in lista1:
        
        print("Memorice la siguiente secuencia...")
        print(x)
        time.sleep(5)
        print("Ordene los marcadores en el orden que se le indicó!")
        time.sleep(5)
        print (chr(27) + "[2J")
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_total += tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
#SubLista(1)
def Nivel1():
    SortLista(lista)
    SubLista(1)
Nivel1()
    


