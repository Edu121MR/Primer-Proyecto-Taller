import time as t
ListaJugadores = []
def RegistroJugadores(nombre: str):
    ListaJugadores.append(nombre)

def Menu():
    while True:
        print (chr(27) + "[2J")
        print("!!Juego de Memória!!")
        print("1) Registrar Jugadores")
        print("2) Jugar")
        print("3) Salir del Juego\n")
        opt= int(input("Que funcion desea realizar: "))
        
        if opt == 1:
            RegistrarContacto()
        elif opt == 2:
            pass
        elif opt == 3:
            print("Gracias por jugar")
            break
    print (chr(27) + "[2J")

def RegistrarContacto():
    print (chr(27) + "[2J")
    while True:
        name=input ("Ingrese el nombre del o los jugadores, cuando termine de escribir los nombres escriba salir:")
        if name == "salir":
            break
        elif name != "salir": 
            RegistroJugadores(name)
    print (chr(27) + "[2J")
    print("Los jugadores registrados son: ", ListaJugadores)   
    t.sleep(5) 
Menu()