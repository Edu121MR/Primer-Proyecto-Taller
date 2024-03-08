while True:
    numero = input("Digite un número ")

    lista_numero = list(numero)

    nuevo = sorted(lista_numero)

    if nuevo != lista_numero:
        print("No esta ordenado")

    if nuevo == lista_numero:
        print("Si esta ordenado")