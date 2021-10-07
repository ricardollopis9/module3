while True:
    iban = input("Introduce tu iban: ")
    if len(iban) == 24 and iban[2:].isdigit and iban[:2] == "ES":
            print("True")
            break
    else:
        print("Iban ERROR!")
