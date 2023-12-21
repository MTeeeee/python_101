import os
os.system('cls')

# Aufgabe 1: ------------------------

# a)
# Schreibe einen print() Befehl der "Hallo mein Name ist <name>" ausgibt. 
# Bsp.: "Hallo mein Name ist Tony."

# b)
# Schreibe nun deinen Namen in eine Variable.
# Schreibe einen Befehl der ausgibt: "Hallo mein Name ist <name>" und die Variable nutzt.

# c)
# Schreibe es so um, dass der Nutzer zunächst nach seinem Namen gefragt wird und dann die Antwort bekommt "Hallo <Name> schön das du da bist."
# tipp: input()


# print("Hallo mein Name ist Tony.")

# name = "Tony"

# print("mein name ist " + name)

# user_name = input("what is your name \n \n \n")
# print("hallo " + user_name)


# Aufgabe 2: ------------------------

# Nutze die Built-in Funktion type().
# Bsp.:
# x = 5
# type_of_x = type(x)
# print(type_of_x)

# Erstelle 4 primitive Varaiblen String, Integer, Float und Boolean und überprüfe sie mit obrigen Befehl.

# integer
# integer_variable = 42
# print("type_integer:", type(integer_variable))

# # float
# float_variable = 3.14
# print("type_float:", type(float_variable))

# # string
# string_variable = "Hello world"
# print("type_string:", type(string_variable))

# # boolean
# boolean_variable = True
# print("type_boolean:", type(boolean_variable))


# Aufgabe 3: ------------------------


# Erstelle zwei Variablen mit jeweils einer Zahl.
# Erstelle eine neue Variable namens ergebnis.
# ergebnis soll die addition der beiden Zahlen enthalten.

# Die Ausgabe soll sagen:
# ´´´
# Zahl 1 ist x
# Zahl 2 ist y
# Das ergebnis der Addition lautet: z
# ´´´

# Hinweis: xyz sollen durch Zahlen ersetzt werden.

# zahl1 = 5
# zahl2 = 200
# ergebnis = zahl1 + zahl2
# print("Zahl 1 ist", zahl1)
# print("Zahl 2 ist", zahl2)
# print("Das ergebnis der komplizierten Rechnung lautet:", ergebnis)


# Aufgabe 4 : ------------------------

# a)

# Übernehme folgenden Code und vervollständige ihn:

# a)

# zahl_1 = 20
# zahl_2 = 10

# ###################
# # ändere den Code hier: 
# # (es dürfen Zeilen hinzugefügt werden)
# # ändere den Code hier:
# ergebnis_addition = zahl_1 + zahl_2
# ergebnis_subtraktion = zahl_1 - zahl_2
# ergebnis_multiplikation = zahl_1 * zahl_2
# ergebnis_division = zahl_1 / zahl_2

# ###################

# print(ergebnis_addition)
# print(ergebnis_subtraktion)
# print(ergebnis_multiplikation)
# print(ergebnis_division)

# b)
# zahl_1 = float(input("Gib die erste Zahl ein: "))
# zahl_2 = float(input("Gib die zweite Zahl ein: "))
 
# addition = zahl_1 + zahl_2
# subtraktion = zahl_1 - zahl_2
# multiplikation = zahl_1 * zahl_2
# division = zahl_1 / zahl_2

# print(addition)
# print(subtraktion)
# print(multiplikation)
# print(division)

# Aufgabe 5: ---------------------------

# Hier ist ein Code der nicht Funktioniert, es haben sich 9 Fehler eingeschlichen, kannst du sie finden?:


# alter = int(input("Bitte gib dein Alter ein: "))

# if alter <= 17:

#     print("Du bist zu jung für diesen Film")

# else:

#     print("Viel Spaß beim Film")


# Aufgabe 6 : ---------------------------


# Übernehme folgenden Code und vervollständige Ihn so, dass das Programm die Rechenmethode überprüft.
# Bei einem "+" soll eine Addition durchgeführt werden und bei einem "-" eine Subtraktion

# zahl_1 = 20
# zahl_2 = 10
# rechenmethode = "-"
# ergebnis = 0

# ###################

# if rechenmethode == "+":
#     ergebnis = zahl_1 + zahl_2
# else:
#     ergebnis = zahl_1 - zahl_2


# ###################

# print("Das ergebnis ist:" + str(ergebnis))

########################################################
# zahl_1 = 20
# zahl_2 = 10
# rechenmethode = input("für Addieren + und für Subtrahieren -")

# if rechenmethode == "+" :
#     ergebnis = (zahl_1 + zahl_2)
# elif rechenmethode == "-" :
#     ergebnis = (zahl_1 - zahl_2)
# else:
#     print("du hast kein Operator angegeben")

# print(ergebnis)

########################################################

# optional: Wer möchte kann das ganze auf die vier Grundrechenarten erweitern und 
# die Zahlen, sowie die Rechenmethode über den Nutzer abfragen.



# zahl_1 = int(input("Bitte gib die erste Zahl:" ))
# zahl_2 = int(input("Bitte gib die zweite Zahl:" ))
# rechenmethode = input("Bitte gib Rechenmethode: (+ - * /)")

# if rechenmethode == "+":
#     ergebnis = zahl_1 + zahl_2
#     print("Ergebnis:", ergebnis)
# elif rechenmethode == "-":
#     ergebnis = zahl_1 - zahl_2
#     print("Ergebnis:", ergebnis)
# elif rechenmethode == "/":
#     ergebnis = zahl_1/zahl_2
#     print("Ergebnis:", ergebnis)
# elif rechenmethode == "*":
#     ergebnis = zahl_1*zahl_2
#     print("Ergebnis:", ergebnis)
# else:
#     print("Ungültige Rechenmethode. Du hast " + str(rechenmethode) + " gegeben")


# Aufgabe 7 : ---------------------------

# Wir haben zwei Variablen auto und farbe.
# Wir wissen das auto entweder BMW oder Mercedes sein kann.
# Der BMW kann entweder weiß oder blau sein.
# Der Mercedes kann entweder rot oder schwarz sein.
# Schreibe ein Skrip, welches Auto und Farbe prüft und für jede Kombination eine passende Ausgabe gibt:
# Bsp. "Es ist ein weißer BMW"
# Dabei sollen if Bedingungen verschachtelt genutzt werden.
# Falls Auto oder Farbe nicht bekannt sind, soll entsprechend "Auto/Farbe nicht bekannt" ausgegeben werden.