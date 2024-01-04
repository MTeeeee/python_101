

# print("Hund", "Katze", "Maus")
# print("Katze")
# print("Maus")

my_list_1 = ["Hund", "Katze", "Maus"]
my_list_1.pop()
print(my_list_1)

my_list_2 = ["Hund", "Katze", "Maus", 42, True, ["salz", "pfeffer"]]



mega_list = my_list_1 + my_list_2
# print(mega_list)
# print(mega_list.index(42)) # findet die erste Stelle(index) des gesuchten Wertes in der list
# print(mega_list[6])

mega_list = [ my_list_1, my_list_2 ]
# print(mega_list)
# print(mega_list[1])
# print(mega_list[1][5])
# print(mega_list[1][5][0])

# print(my_list)
# print(my_list_2)
# print(mega_list)

my_list_1 = ["Hund", "Katze", "Maus"]

# print(my_list_1[0])
# print(my_list_1[1])
# print(my_list_1[2])

# print(my_list_1[-1])
# print(my_list_1[-2])
# print(my_list_1[-3])

tiere = ["Hund", "Katze", "Maus"]

enthalten = "Hund" in tiere
# print(enthalten)

# Mit append können neue items an das Ende der list anghangen werden

tiere.append("Hase")
# print(tiere)

# Mit insert können items an spezifischen Stellen eingefügt werden
tiere.insert(2,"Vogel")
# print(tiere)

tiere.pop() # entfert sofern kein index angegeben die letzte Stelle in der list
# pop(index) entfert die mit index angegebene Stelle
# print(tiere)

# tiere.remove("Vogel") # Entfernt ersten Eintrag mit der Bezeichnung
# print(tiere)
del tiere[2]
# print(tiere)

copy_tiere = tiere.copy()
# print(copy_tiere)

alle_tiere = tiere + copy_tiere
# print(alle_tiere)