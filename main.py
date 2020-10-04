#hracia plocha
pole = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

vitaz = "-"

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
    if vitaz != "-":
        return
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
    if vitaz != "-":
        return
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
    riadok()
    stlpec()
    diagonal()
    if vitaz == "X":
        print("Hrac X vyhral, gratulujeme :)")
    elif vitaz == "0":
        print("Hrac 0 vyhral, gratulujeme :)")

def riadok():
    global vitaz
    if pole[0] == pole[1] == pole[2] != "-":
        vitaz = pole[0]
    elif pole[3] == pole[4] == pole[5] != "-":
        vitaz = pole[3]
    elif pole[6] == pole[7] == pole[8] != "-":
        vitaz = pole[6]
    else: return

def stlpec():
    global vitaz
    if pole[0] == pole[3] == pole[6] != "-":
        vitaz = pole[0]
    elif pole[1] == pole[4] == pole[7] != "-":
        vitaz = pole[1]
    elif pole[2] == pole[5] == pole[8] != "-":
        vitaz = pole[2]
    else: return

def diagonal():
    global vitaz
    if pole[0] == pole[4] == pole[8] != "-":
        vitaz = pole[0]
    elif pole[2] == pole[4] == pole[6] != "-":
        vitaz = pole[2]
    else: return


start()


