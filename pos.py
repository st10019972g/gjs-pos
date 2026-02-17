import os

# ==========================================================
# EENVOUDIGE PUNT VAN VERKOOP (POS) STELSEL
# ==========================================================
# Hierdie program simuleer 'n kasregister op die command line.
#
# Die gebruiker kan:
# 1. Produkte byvoeg met pryse
# 2. Produkte verwyder
# 3. Alle produkte en totaal vertoon
# 4. Program verlaat
#
# ==========================================================


# Lys wat al die produkte sal stoor.
# Elke item in die lys is 'n tuple in hierdie formaat: (naam, prys)
produkte = []


# ---------------- FUNKSIE: MAAK SKERM SKOON ----------------
def maak_skerm_skoon():
    """
    Hierdie funksie maak die terminal/command line skerm skoon.
    Dit werk op:
    - Windows (cls)
    - Linux/Mac (clear)
    """

    # os.name == "nt" beteken Windows
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ---------------- FUNKSIE: WAG VIR ENTER ----------------
def wag_vir_enter(boodskap="Druk Enter om voort te gaan..."):
    """
    Hierdie funksie pause die program totdat die gebruiker Enter druk.
    Dit help dat die gebruiker die boodskap/resultate kan lees.
    """
    input(boodskap)


# ---------------- FUNKSIE: VOEG PRODUK BY ----------------
def voeg_produk_by():
    """
    Hierdie funksie vra vir:
    - 'n produknaam
    - 'n prys
    Daarna voeg dit die produk by die 'produkte' lys.
    """

    naam = input("Voer produk naam in: ")

    # Vra vir prys en probeer dit omskakel na 'n float
    # Indien die gebruiker verkeerde invoer tik (bv. letters),
    # sal ons dit hanteer en weer vra.
    while True:
        try:
            prys = float(input("Voer prys in: R"))
            break
        except ValueError:
            print("Ongeldige prys. Voer asseblief 'n nommer in, bv. 55.70")

    # Voeg die produk as tuple (naam, prys) by die lys
    produkte.append((naam, prys))
    
    print()
    print("+----------------------------+")
    print("| Produk suksesvol bygevoeg! |")
    print("+----------------------------+")
    print()

# ---------------- FUNKSIE: VERWYDER PRODUK ----------------
def verwyder_produk():
    """
    Hierdie funksie vra die gebruiker watter produk om te verwyder.
    Dit soek deur die lys en verwyder die eerste match.
    """

    if len(produkte) == 0:
        print("Daar is geen produkte om te verwyder nie.\n")
        return

    soek_naam = input("Watter produk wil jy verwyder?: ")

    # Loop deur elke item in die produkte lys
    for item in produkte:
        # item[0] is die produk se naam
        if item[0].lower() == soek_naam.lower():
            produkte.remove(item)
            print()
            print("+----------------------------+")
            print("| Produk verwyder!           |")
            print("+----------------------------+")
            print()
            return

    # As ons hier kom, beteken dit geen produk is gevind nie
    print()
    print("+----------------------------+")
    print("| Produk nie gevind nie!     |")
    print("+----------------------------+")
    print()


# ---------------- FUNKSIE: WYS PRODUKTE ----------------
def wys_produkte():
    """
    Hierdie funksie:
    - wys al die produkte en hulle pryse
    - bereken en wys die totaal
    """

    if len(produkte) == 0:
        print()
        print("+------------------------------------+")
        print("| Geen produkte is nog bygevoeg nie. |")
        print("+------------------------------------+")
        print()
        return

    totaal = 0

    print("------- PRODUKTE -------")

    # For-each lus: (naam, prys) word uit elke tuple gehaal
    for naam, prys in produkte:
        print(f"{naam}\t R{prys:.2f}")
        totaal += prys

    print("------------------------")
    print(f"Totaal R{totaal:.2f}\n")


# ---------------- FUNKSIE: WYS KIESLYS ----------------
def wys_kieslys():
    """
    Hierdie funksie wys net die kieslys opsies.
    Dit hou die hoof_program netjies en leesbaar.
    """
    print("===== POS KEUSELYS =====")
    print("1. Voeg produk by")
    print("2. Verwyder produk")
    print("3. Wys produkte en totaal")
    print("4. Verlaat program")


# ---------------- HOOF PROGRAM ----------------
def hoof_program():
    """
    Hierdie is die hoof beheerlus van die program.
    - 'keuse' is die sentinel veranderlike.
    - Elke keer as die menu wys, maak ons eers die skerm skoon.
    """

    keuse = ""

    # Die lus hardloop tot die gebruiker "4" kies
    while keuse != "4":
        maak_skerm_skoon()
        wys_kieslys()

        keuse = input("Kies 'n opsie: ")

        if keuse == "1":
            maak_skerm_skoon()
            voeg_produk_by()
            wag_vir_enter()

        elif keuse == "2":
            maak_skerm_skoon()
            verwyder_produk()
            wag_vir_enter()

        elif keuse == "3":
            maak_skerm_skoon()
            wys_produkte()
            wag_vir_enter("Druk Enter om terug te gaan na kieslys...")

        elif keuse == "4":
            maak_skerm_skoon()
            print("Totsiens!")

        else:
            print("Ongeldige opsie!")
            wag_vir_enter("Druk Enter om weer te probeer...")


# ---------------- PROGRAM BEGIN ----------------
hoof_program()
