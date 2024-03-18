import time as t                              #Importa la librería time
import random as r                            #Importa la librería random
import ARMem as ar                            #Importa la librería ARMem

Frutas = [" Piña ", " Cereza ", " Uvas ", " Pera ", " Guanabana "]         #Lista de las futas utilizadas para el juego
Lista1 = [0, 1, 2, 3, 4]                      #Lista para usar en el nivel 1
Lista2 = [0, 1, 2, 3, 4]                      #Lista para usar en el nivel 2
Lista3 = [0, 1, 2, 3, 4]                      #Lista para usar en el nivel 3
ListaJugadores = []                           #Lista donde se guardan los nombres de los jugadores
ListaJugadoresTiempo = {}                     #Diccionario donde se guaraan los tiempos de los jugadores

def ObtenerFruta(t) -> str:
    """Función que retorna la fruta segun el número que se le de

    Args:
        t (num): Número de la fruta

    Returns:
        str: Retorna la fruta
    """
    return(Frutas[t])         #Retorna la fruta segun el número que se le de

def MezclarLista(Lista, x) -> list:
    """Función que mezcla las listas de las frutas

    Args:
        Lista (List): Lista de las frutas
        x (Num): Número correspondiente a cada lista de frutas

    Returns:
        list: Retorna la lista temporal para el nivel donde se este
    """
    ListaTemporal = []                                 # Lista temporal donde se guardan las listas de las frutas
    for i in range(len(ListaJugadores)):               # Ciclo que recorre la lista de los jugadores
        OrdenJugador = []                              # Lista donde se guardan las frutas de cada jugador
        for _ in range(5):                             # Ciclo que recorre la lista de las frutas
            orden_jugador = r.sample(Lista, x)         # Se mezclan las frutas para cada jugador
            OrdenJugador.append(orden_jugador)         # Se agrega la lista de las frutas a la lista de los jugadores
        ListaTemporal.append(OrdenJugador)             # Se agrega la lista temporal de las frutas a la lista de los jugadores
    return ListaTemporal                               #Retorna la lista temporal para el nivel donde se este

def Juego(ListaMezclada: list, Nivel: int):
    """ Funcion que realiza el juego

    Args:
        ListaMezclada (list): Lista de las frutas mezcladas
        Nivel (int): Nivel que se esta ejecutando
    """
    for i in range(5 * len(ListaJugadores)):                        #Ciclo que recorre la lista de los jugadores
        Jugador = ListaJugadores[i % len(ListaJugadores)]           #Se obtiene el nombre de el jugador
        OrdenFrutas = ListaMezclada[i // 5][i % 5]                  #Se obtiene la lista de las frutas mezcladas
        FrutasNombres = ""                                          #Variable donde se guardan los nombres de las frutas
        TiempoTotal = 0                                             #Variable donde se guarda el tiempo total
        print(f'\033[2J')                                           #Limpia la pantalla
        print(f'Es el turno del jugador {Jugador}')                 #Imprime el mensaje con el nombre de el jugador
        print("¡Memorice la siguiente secuencia!")                  #Imprime el mensaje
        for FrutaIndex in OrdenFrutas:                              #Ciclo que recorre la lista de las frutas
            FrutaNombre = ObtenerFruta(FrutaIndex)                  #Se obtiene el nombre de la fruta
            FrutasNombres += FrutaNombre + " "                      #Se guardan los nombres de las frutas
            print(FrutaNombre)                                      #Imprime el nombre de la fruta
            t.sleep(2)                                              #Se duerme 2 segundos 
        print("¡Ordene los marcadores en el orden que se le indicó!")     #Imprime el mensaje
        t.sleep(3)                                                        #Se duerme 3 segundos
        print('\033[2J')                                                  #Limpia la pantalla
        t.sleep(3)                                                        #Se duerme 3 segundos
        TiempoPartida = round(ar.start_sorting(OrdenFrutas, flip_image=True, show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False), 2)   #Se obtiene el tiempo de la partida cuando se ordenen las frutas en el orden correcto 
        TiempoTotal += TiempoPartida                                      #Se suma el tiempo de partida al tiempo total
        print('\033[2J')                                                  #Limpia la pantalla
        print(f'Tiempo de partida para {Jugador}: {TiempoPartida}s')      #Imprime el mensaje con el tiempo de partida de el jugador
        t.sleep(6)                                                        #Se duerme 3 segundos

        if Jugador not in ListaJugadoresTiempo:                           #Si el jugador no esta en la lista de los jugadores
            ListaJugadoresTiempo[Jugador] = {}                            #Se agrega el nombre de el jugador a la lista de los jugadores
        ListaJugadoresTiempo[Jugador][Nivel] = TiempoTotal                #Se agrega el tiempo total de el jugador al nivel que se este ejecutando

def Nivel1():
    """ Función que ejecuta el nivel 1
    """
    MezclaNivel1 = MezclarLista(Lista1, 3)       #Se mezclan las frutas para el nivel 1
    Juego(MezclaNivel1, 1)                       #Se ejecuta el juego para el nivel 1

def Nivel2():
    """Función que ejecuta el nivel 2
    """
    MezclaNivel2 = MezclarLista(Lista2, 4)       #Se mezclan las frutas para el nivel 2
    Juego(MezclaNivel2, 2)                       #Se ejecuta el juego para el nivel 2

def Nivel3():
    """Función que ejecuta el nivel 3
    """
    MezclaNivel3 = MezclarLista(Lista3, 5)       #Se mezclan las frutas para el nivel 3
    Juego(MezclaNivel3, 3)                       #Se ejecuta el juego para el nivel 3

def ObtenerTiempoTotal(Jugador: str) -> float:
    """Función que obtiene el tiempo total de cada jugador

    Args:
        Jugador (str): Nombre de el jugador

    Returns:
        float: Retorna el tiempo total de cada jugador
    """
    if Jugador in ListaJugadoresTiempo:                       #Si el jugador esta en la lista de los jugadores
        return sum(ListaJugadoresTiempo[Jugador].values())    #Retorna el tiempo total de cada jugador
    else:                                                     #Si el jugador no esta en la lista de los jugadores
        return 0                                              #Retorna 0

def EncontrarGanador() -> str:
    """Función que obtiene el ganador del juego

    Returns:
        str: Retorna el nombre de el ganador, el que hizo el menor tiempo en los 3 niveles
    """
    TiemposTotales = {Jugador: ObtenerTiempoTotal(Jugador) for Jugador in ListaJugadores}       #Diccionario donde se guardan los tiempos totales de cada jugador para compararlos y saber quien gano
    Ganador = min(TiemposTotales, key=TiemposTotales.get)                                    #Se obtiene el ganador, el que hizo el menor tiempo en los 3 niveles
    return(Ganador)                                                                             #Retorna el nombre de el ganador

def RegistroJugadores(Nombre: str):
    """Función que registra los jugadores

    Args:
        Nombre (str): Nombres de los jugadores
    """
    ListaJugadores.append(Nombre)      #Se agrega el nombre de los jugadores a la lista de los jugadores

def Menu():
    """ Función que ejecuta el menú del juego
    """
    while(True):                           #Ciclo que se ejecuta mientras sea verdadero
        print(chr(27) + "[2J")             #Limpia la pantalla
        print("====================")      #Imprime el mensaje(decoración)
        print("!!Juego de Memoria!!")      #Imprime el mensaje
        print("====================")      #Imprime el mensaje(decoración)
        print("\n")                        #Se salta una línea
        print("1) Registrar Jugadores")    #Imprime el mensaje
        print("2) Jugar")                  #Imprime el mensaje
        print("3) Salir del Juego\n")      #Imprime el mensaje y se salta una línea
        Opcion = int(input("Qué función desea realizar: "))      #Se le pide al usuario que ingrese una opción
        
        if Opcion == 1:                      #Si escoge la opción 1
            RegistrarJugadores()             #Se ejecuta la función de registrar jugadores
        elif Opcion == 2:                    #Si escoge la opción 2
            if len(ListaJugadores) == 0:     #Si la lista de los jugadores esta vacía
                print('\033[2J')             #Limpia la pantalla
                print("No hay jugadores registrados")      #Imprime el mensaje no hay jugadores registrados
                print("Por favor a continuación registre el o los jugadores: ")      #Imprime el mensaje para que registre el o los jugadores
                t.sleep(5)                   #Se duerme 5 segundos
                RegistrarJugadores()         #Se ejecuta la función de registrar jugadores
            print('\033[2J')                 #Limpia la pantalla
            print("Nivel 1")                 #Imprime el mensaje
            print("El juego comenzará en 3 segundos...")                             #Imprime el mensaje
            t.sleep(3)                       #Se duerme 3 segundos
            print('\033[2J')                 #Limpia la pantalla
            Nivel1()                         #Se ejecuta el nivel 1
            print('\033[2J')                 #Limpia la pantalla
            print("Nivel 2")                 #Imprime el mensaje
            print("El juego comenzará en 3 segundos...")                             #Imprime el mensaje
            t.sleep(3)                       #Se duerme 3 segundos
            print('\033[2J')                 #Limpia la pantalla
            Nivel2()                         #Se ejecuta el nivel 2
            print('\033[2J')                 #Limpia la pantalla
            print("Nivel 3")                 #Imprime el mensaje
            print("El juego comenzará en 3 segundos...")                             #Imprime el mensaje
            t.sleep(3)                       #Se duerme 3 segundos
            print('\033[2J')                 #Limpia la pantalla
            Nivel3()                         #Se ejecuta el nivel 3
            print('\033[2J')                 #Limpia la pantalla

            Ganador = EncontrarGanador()     #Se llama a la función para encontrar el ganador
            print(f"El ganador es: {Ganador} con un tiempo total de {ObtenerTiempoTotal(Ganador)}s")       #Imprime el mensae con el nombre de el ganador y su tiempo total
            t.sleep(5)                       #Se duerme 5 segundos
            break                            #Se rompe el ciclo

        elif Opcion == 3:                    #Si escoge la opción 3
            print("Gracias por jugar")       #Imprime el mensaje gracias por jugar
            t.sleep(5)                       #Se duerme 5 segundos
            break                            #Se rompe el ciclo
    print('\033[2J')                         #Limpia la pantalla
   
def RegistrarJugadores():
    """Función para registrar a los jugadores
    """
    print('\033[2J')                         #Limpia la pantalla
    while(True):                             #Ciclo que se ejecuta mientras sea verdadero
        Nombre = input("Ingrese el nombre del o los jugadores, cuando termine de escribir los nombres escriba salir:")      #Se le pide al usuario que ingrese el nombre de el o los jugadores
        if Nombre.lower() == "salir":        #Se pone el .lower para que no importe si el usuario escribe en mayúsculas o minúsculas
            if len(ListaJugadores) == 0:     #Si la lista de los jugadores esta vacía
                print('\033[2J')             #Limpia la pantalla
                print("No hay jugadores registrados")       #Imprime el mensaje no hay jugadores registrados
                print("Debe ingresar al menos un jugador para poder jugar")       #Imprime el mensaje
                t.sleep(5)                   #Se duerme 5 segundos
                RegistrarJugadores()         #Se ejecuta la funcion para registrar a los jugadores
            break                            #Se rompe el ciclo
        elif Nombre != "salir":              #Si el nombre no es salir, se registra como un nombre
            RegistroJugadores(Nombre)        #Se ejecuta la función para registrar a los jugadores con su nombre
    print('\033[2J')                         #Limpia la pantalla
    print("El o los jugadores registrados son: ", ListaJugadores)        #Imprime el mensaje con los jugadores registrados
    t.sleep(5)                               #Se duerme 5 segundos

Menu()                                       #Se ejecuta el menú del juego