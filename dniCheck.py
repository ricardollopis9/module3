dniList = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    dni = input("Introduce tu dni: ")

    if len(dni) == 9 and dni[:-1].isdigit and dni[-1].isalpha:
        decimals = int(dni[:-1]) % 23

        if dni[-1] == dniList[decimals]:
            print("True")
            break
        else:
            print("False")
    else:
        print("Dni ERROR!")
