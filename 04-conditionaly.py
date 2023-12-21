# In python können wir Bedingungen formulieren in dem wir zwei Werte miteinander vergleichen.
# Die finden wir oft unter dem Begriff conditionals und lasst sich am einfachsten mit if statements demonstrieren.
# 

# Nehmen wir an das ein script soll überprüfen wer wir sind und uns nur reinlassen wenn es uns kennt.

# print("")

# alter = int(input("Bitte gib dein Alter ein: "))

# # alter_als_zahl = int(alter)

# if alter == 7:
#     print("Du bist 7")
#     # weitere Schritte
# elif alter == 10:
#     print("Du bist 10")
# else:
#     print("Du bist weder 7 noch 10")

# if name != "Tony": # Verneinung
#     print("Du bist nicht Tony!")
# else:
#     print("Du musst wohl Tony sein.")


# Hierzu einpaar Vergleichs Operatoren
# gleich:           a == b
# nicht Gleich:     a != b
# weniger als:      a < b
# weniger gleich:   a <= b
# größer als:       a > b
# größer gleich:    a >= b

########################################################

# name = input("Wie heißt du? ")
# print("Hallo " + name)

# alter = 5

# alter = input("Wie alt bist du?")

# zahl = int(alter)
    
# if zahl >= 18:
#     print("Du bist volljährig")
# else:
#     print("Du bist noch nicht Volljährig!")
    
########################################################


# Darüber hinaus können wir mehrere Bedingungen auf einmal prüfen, 
# indem wir sie mit Logischen Operatoren verbinden.

# Logische Operatoren
# and
# or
# not

first_name = "Tony"
uhrzeit = 9

last_name = "Stark"

if first_name == "Tony" and uhrzeit <= 8:
    print("Welcome!")
else:
    print("Alert!")

# vollwertige Liste: https://www.w3schools.com/python/python_operators.asp

