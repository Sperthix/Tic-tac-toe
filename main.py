pole = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def vypis_pole():
    print(pole[0] + " " + pole[1] + " " + pole[2])
    print(pole[3] + " " + pole[4] + " " + pole[5])
    print(pole[6] + " " + pole[7] + " " + pole[8])

def start():
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    tah()

def tah():
    kontrola_vyhry()
    volba = input("zadaj poziciu svojho tahu: 1-9")
    volba = int(volba) - 1
    if (pole[volba] == "-"):
        pole[volba] = "X"
        vypis_pole()
        tah2()
    else:
        print("tah nemozno uskutocnit")
        tah()

def tah2():
    kontrola_vyhry()
    volba2 = input("zadaj poziciu svojho tahu: 1-9")
    volba2 = int(volba2) - 1
    if (pole[volba2] == "-"):
        pole[volba2] = "O"
        vypis_pole()
        tah()
    else:
        print("tah nemozno uskutocnit")
        tah2()


def kontrola_vyhry():
    print()


start()


