import ARMem as ar
import time
import random as r
lista=[0,1,2,3,4]
lista1=[]
def SortLista(lista):
    for i in range(len(lista)):
        random= r.sample(lista,3)
        lista1.append(random)
    return lista1
(SortLista(lista))

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
tiempo_total=0
for x in lista:
    print(f'Memorice la siguiente secuencia...')
    print(x)
    time.sleep(5)
    print(f'Ordene los marcadores en el orden que se le indicó!')
    time.sleep(3)
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

    tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
    tiempo_total+=tiempo_partida
    print(f'Tiempo de partida: {tiempo_partida}s')

    time.sleep(3)
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

print (f'El usuario ha completado el juevo en un tiempo de {tiempo_total}s')