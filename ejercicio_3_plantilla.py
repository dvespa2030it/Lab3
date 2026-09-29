try:
    numero_dia = int(input("Escribe un número del 1 al 7: "))
    match numero_dia:
        case 1:
            print("Has escrito el numero 1")
        case 2:
            print("Has escrito el numero 2")
        case 3:
            print("Has escrito el numero 3")
        case 4:
            print("Has escrito el numero 4")
        case 5:
            print("Has escrito el numero 5")
        case 6:
            print("Has escrito el numero 6")
        case 7:
            print("Has escrito el numero 7")
        case _:
            print("Error: el número debe estar entre 1 y 7.")
except ValueError:
    print("Error: Debes ingresar un número entero.") 