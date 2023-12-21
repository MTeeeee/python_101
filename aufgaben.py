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
integer_variable = 42
print("type_integer:", type(integer_variable))

# float
float_variable = 3.14
print("type_float:", type(float_variable))

# string
string_variable = "Hello world"
print("type_string:", type(string_variable))

# boolean
boolean_variable = True
print("type_boolean:", type(boolean_variable))
