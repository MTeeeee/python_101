########################
# Primitive Datentypen #
########################

myInteger = 2 # Zahl
myFloat = 4.2 # Float
myString = "3" # String
myBool = True # Boolean

print(myString)
print(myInteger)

# Strings können aneinander angehangen werden in dem man sie mit einem + verbindet

item_1 = "pen"
item_2 = "pineapple"
item_3 = item_2 + item_1

print(item_3)

# Unterschiedliche Datentypen lassen sich in Python nicht ohne weiteres Kombinieren.
fusion_str = myString + str(myInteger)
print(fusion_str)

fusion_int = int(myString) + myInteger
print(fusion_int)

# Zahlen können mathematisch verrechnet werden

zahl_1 = 2
zahl_2 = 3
summe = zahl_1 + zahl_2

print(summe)

# hierfür können wir Arithmetische Operatoren nutzen

x = 10 
y = 5

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation

#####################################################

# x = 10 
# y = 5

# print("Die Zahlen lauten x = ", x, " y = ", y)
# print("Addition", x + y)    # Addition
# print("Subtraction", x - y) # Subtraction
# print("Multiplication", x * y) # Multiplication
# print("Division", x / y) # Division
# print("Modulus", x % y) # Modulus
# print("Exponentiation", x ** y) # Exponentiation