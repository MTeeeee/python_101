import os
os.system('cls')

# Funktionen
# Wiederverwendbare Blöcken von Code


# def message():
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")

# print("Start")
# message()
# print("nächster Abschnitt")
# message()
# print("Ende")


# Flächeninhalt: A = a * b

# f(x) = 2x + 5



def area(a, b):         # parameter
    result = a * b
    return result      # return ist sehr wichtig


# #######################################################


# ergebnis = area(2, 5)              # argumente

# print(f"Die Fläche ist {ergebnis} Quatdratmeter groß.")





# def taschenrechner():
#     zahl_1 = int(input("Bitte gib die erste Zahl:" ))
#     zahl_2 = int(input("Bitte gib die zweite Zahl:" ))
#     rechenmethode = input("Bitte gib Rechenmethode: (+ - * /)")

#     if rechenmethode == "+":
#         ergebnis = zahl_1 + zahl_2
#         print("Ergebnis:", ergebnis)
#     elif rechenmethode == "-":
#         ergebnis = zahl_1 - zahl_2
#         print("Ergebnis:", ergebnis)
#     elif rechenmethode == "/":
#         ergebnis = zahl_1/zahl_2
#         print("Ergebnis:", ergebnis)
#     elif rechenmethode == "*":
#         ergebnis = zahl_1*zahl_2
#         print("Ergebnis:", ergebnis)
#     else:
#         print("Ungültige Rechenmethode. Du hast " + str(rechenmethode) + " gegeben")
        
        
# ###########

# print("Hallo willkommen beim super awesome Taschenrechner")

# taschenrechner()

# nochmal = input("Nochmal? y/n")

# if nochmal == "y":
#     taschenrechner()
# else:
#     print("ok dann nicht")


# print("Danke das du den Taschenrechner benutzt hast.")


# Was ist eine function
# Wiederverwendbarer Block Code


def hello_user():
    print("Hello")
    name = input("Wie heißt du?")
    print("Hallo " + name + " schön dich kennenzulernen!")
    print("Nächste Person bitte!")

hello_user()
