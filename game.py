import os
os.system('cls')

##### functions

def welcome():
    print("Wilommen beim Zahlen Raten.")
    print("Viel Spaß!")

def game():
    secret_number = 42
    user_input = 0
    
    while user_input != secret_number:
        
        try:
            user_input = int(input("Bitte gib eine Zahl zwischen 1 und 100 an: "))
            
            if user_input <= 100 and user_input >= 1:
                if user_input == secret_number:
                    print("Richtig, Glückwunsch!")
                elif user_input < secret_number:
                    print("Zu klein, bitte nochmal versuchen.")
                else:
                    print("Zu groß, bitte nochmal versuchen.")
            else:
                print("Die angegebene Zahl ist nicht zwischen 1 und 100, bitte versuche es erneut")
            
        except:
            print("Eingabe nicht Gültig, bitte versuche es erneut!")


def again():
    user_input = input("Nochmal Spielen? j/n")
    
    if user_input == "j":
        return True
    else:
        return False

def goodby():
    print("Danke fürs Spielen. Tschöööö!")

##### main
play = True

welcome()

while play == True:
    game()
    play = again()

goodby()