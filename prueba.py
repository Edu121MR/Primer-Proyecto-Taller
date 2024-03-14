import time as t
import random as r
import ARMem as ar

frutas = [" Piña ", " Cereza ", " Uvas ", " Pera ", " Guanabana "]
lista = [0, 1, 2, 3, 4]
lista1 = []
ListaJugadores = []
ListaJugadoresTiempo = []


def ObtenerFruta(j):
    return frutas[j]


def SortLista(lista, x):
    for i in range(len(ListaJugadores) * 5):
        random = r.sample(lista, x)
        lista1.append(random)
    return lista1


def Juego(index, FrutasNombres="",g=""):
    tiempo_total = 0
    i = 0
    for x in lista1:
        for j in x:
            g=ObtenerFruta(j)
            FrutasNombres += g
        if i == len(ListaJugadores):
            i = 0
        print('\033[2J')
        print(f"Es el turno del jugador {ListaJugadores[i]}")
        i += 1
        print("¡Memorice la siguiente secuencia!")
        print(FrutasNombres)
        t.sleep(2)
        print("¡Ordene los marcadores en el orden que se le indicó!")
        t.sleep(5)
        print('\033[2J')
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_total += tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        t.sleep(3)
    print(f"El tiempo total del nive fue {tiempo_total}")
    t.sleep(5)
    print('\033[2J')


def Nivel1():
    SortLista(lista, 3)
    Juego(1)


def Nivel2():
    SortLista(lista, 4)
    Juego(1)


def Nivel3():
    SortLista(lista, 5)
    Juego(1)


def RegistroJugadores(nombre: str):
    ListaJugadores.append(nombre)
    ListaJugadoresTiempo.append(nombre)


def Menu():
    while True:
        print(chr(27) + "[2J")
        print("!!Juego de Memória!!")
        print("1) Registrar Jugadores")
        print("2) Jugar")
        print("3) Salir del Juego\n")
        opt = int(input("Que funcion desea realizar: "))

        if opt == 1:
            RegistrarJugadores()
        elif opt == 2:
            if len(ListaJugadores) == 0:
                print('\033[2J')
                print("No hay jugadores registrados")
                print("Por favor a continuación registre el o los jugadores")
                t.sleep(5)
                RegistrarJugadores()
            print('\033[2J')
            print("Nivel 1")
            print("El juego comenzará en 3 segundos...")
            t.sleep(3)
            print('\033[2J')
            Nivel1()
            print('\033[2J')
            print("Nivel 2")
            print("El juego comenzará en 3 segundos...")
            t.sleep(3)
            print('\033[2J')
            Nivel2()
            print('\033[2J')
            print("Nivel 3")
            print("El juego comenzará en 3 segundos...")
            t.sleep(3)
            print('\033[2J')
            Nivel3()
            print('\033[2J')

        elif opt == 3:
            print("Gracias por jugar")
            t.sleep(5)
            break
    print('\033[2J')


def RegistrarJugadores():
    print('\033[2J')
    while True:
        name = input("Ingrese el nombre del o los jugadores, cuando termine de escribir los nombres escriba salir:")
        if name.lower() == "salir":
            break
        elif name != "salir":
            RegistroJugadores(name)
    print('\033[2J')
    print("Los jugadores registrados son: ", ListaJugadores)
    t.sleep(5)


Menu()
