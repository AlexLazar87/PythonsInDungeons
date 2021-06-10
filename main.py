import os
import Player
import winsound


introMsg = """
**********************************************************************************************
*    Welcome,stranger.                                                                       *
*    Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.    *
*    In a country where magic rules, anything is possible if you wish so.                    *
*    It all depends on you, brave hero.                                                      *
**********************************************************************************************


"""

sound = "Main_Menu.wav"
winsound.PlaySound(sound,winsound.SND_ASYNC)

print(introMsg)
print("\033[1;32;40m Would you like to start the adventure?\n")
answer = input ("Yes or No -> ")
if answer.upper() == "YES":
    print("OK")
    os.system('cls')
    answer = input("""What type of player are you:
         ** 1. Warrior ** 
         ** 2. Wizard  **   """)
    if answer == '1':
        player_name = input("What is your name, WARRIOR? ")
        player = Player.Warrior(player_name)
        print("-=- W 3 L C 0 M 3 -=- to the ***** Pyth0ns1nDunge0ns *****")
        input("Press a key to continue ...")
        os.system('cls')
        sound = "Exploring.wav"
        winsound.PlaySound(sound,winsound.SND_ASYNC)
        print(""""You now have 3 paths ahead:
        1. -> To The Village
        2. -> To The Forrest
        3. -> To The Desert""")
        path_option = input("What is your choice? ")

    elif answer == '2':
        player_name = input("What is your name, WIZARD? ")
        player = Player.Wizard(player_name)
        print("-=- W 3 L C 0 M 3 -=- to the ***** Pyth0ns1nDunge0ns *****")
        os.system('cls')

    else:
        print("Chose a valid action")



else:
    print("Thank you, good bye!")