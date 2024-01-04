print("hello world!") # das ist ein Kommentar

stadt = "Berlin"
my_integer = 5
my_float = 5.5
my_bool = True

# print(stadt)
# print(my_integer)
# print(my_bool)


# wenn y kleiner als x dann rechne x - y
# wenn y größer als x dann rechne x + y

def rechner(x, y, m):
    # x = 5
    # y = 6
    # m = 2
    
    if x > y :
        return (x - y)*m
    else:
        return (x + y)*m

z = rechner(5, 3, 2)
# z = 4
print(z)
print(rechner(5, 6, 2))
