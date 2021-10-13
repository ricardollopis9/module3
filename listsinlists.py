lista = []
while True:
    print("Opciones: ")
    print("1-Add a number to the list")
    print("2-Add a number in a posiition in the list")
    print("3-Show the length of the list")
    print("4-Delete the last number in the list")
    print("5-Delete a number in the list")
    print("6-Count numbers")
    print("7-Positions of a numbers")
    print("8-Show the list")
    print("9-Exit")

    option = int(input("Opcion: "))
    lista.pop
    if option == 1:
        lista.append(input("Numero: "))
    if option == 2:
        i = int(input("Posicion 1: "))
        lista[i]= int(input("Numero: "))
    if option == 3:
        print(len(lista))
    if option == 4:
        lista.pop([-1])
    if option == 5:
        lista.pop[int(input("Posicion 1:"))]
    if option == 6:
        lista.count(int(input("Numero: ")))
    if option == 7:
        lista.index(int(input("Numero: ")))
    if option == 8:
        print("")
        print(lista)
    if option == 9:
        print("")
        print("Fin")
        break
    if option < 1 or option > 9:
        print("Opcion Invalida!!")