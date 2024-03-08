def menu():
    while True:
        print("Menú")
        print("1 > Insertar vehículos \n2 > Cambiar estado \n3 > Alquilar vehículo \n4 > Reportes \n5 > Salir del juego")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))

        if opcionSelec == 1:
            print("¡Bienvenido a insertar vehículo!")
        elif opcionSelec == 2:
            print("¡Bienvenido a cambiar estado!")
            # aquí se llama una función
        elif opcionSelec == 3:
            print("¡Bienvenido a alquilar vehículo!")
            # aquí se llama una función
        elif opcionSelec == 4:
            print("¡Bienvenido a reportes!")
            # aquí se llama una función
        elif opcionSelec == 5:
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()