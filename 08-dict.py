import os
os.system('cls')

# Dictionary

# my_dict = {"hund": "Bello", "katze": "Miau", "maus": "Piep"}

my_dict = {
    "hunde": ["Bello", "Lucky", "Buddy"],
    "katzen": {
        "schwarz": "Snowball",
        "weiß": "Blacky",
        "rot": "Tiger"
        },
    "maus": "Piep",
    "anzahl": 6,
    "genug": False
    
}



# Anzeigen von Items
# print(my_dict["anzahl"])
# print(my_dict["hunde"])
# print(my_dict["hunde"][0])
# print(my_dict["katzen"])
# print(my_dict["katzen"]["schwarz"])
# print(my_dict["katzen"]["rot"])


# verändern von dictionaries
my_dict["vögel"] = ["Polly", "Captain Blaubart"]
my_dict["hunde"].append("Sam")
my_dict["katzen"]["weiß"] = "Whitey"
print(my_dict)

print("vögel" in my_dict) # Prüft öb Vögel vorhanden sind
copy_my_dict = my_dict.copy()
del my_dict
# my_dict.pop("vögel") # Löscht Vögel
# my_dict.popitem()
# del my_dict["hunde"]
# print("vögel" in my_dict) # Prüft ob Vögel enthalten sind

print(copy_my_dict.keys())
print(copy_my_dict.values())




