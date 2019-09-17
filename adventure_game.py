import time

import random

items = []

weapon = ['knife', 'sword', 'axe', 'hammer']

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("I'm sorry, that is not an option.")
            time.sleep(2)
    return response

while True:
    #intro
    print("You find yourself in a small town, filled with a few shops and a lot of houses.")
    time.sleep(2)
    print("You've heard that there is a robber who breaks into homes every night, "
            "stealing everything of value.")
    time.sleep(2)
    print("You're here to stop him.")
    time.sleep(2)
    print("All you have in your pockets is a pack of chewing gum and a little bit of money.")
    time.sleep(2)
    print("In front of you is a general store.")
    time.sleep(2)
    print("To your left is a very pretty little house with a garden and a swing.")
    time.sleep(2)
    #choice of direction to move
    while True:
        store = valid_input("Would you like to go in the general store or the house?\n\n"
                            "Enter 1 for the general store.\n"
                            "Enter 2 for the house.\n", "1", "2")
        if store == '1':
            if "handcuffs" in items:
                print("You enter the general store.")
                time.sleep(2)
                print("You already used your money to buy supplies, so there is nothing"
                    " more for you to do in here.")
                time.sleep(2)
                print("You walk back outside to the town square.")
                time.sleep(2)
            else:
                weapon = random.choice(weapon)
                print("You enter the general store and browse the shelves.")
                time.sleep(2)
                print(f"You use the money in your pocket to buy a {weapon} and a pair of handcuffs.")
                time.sleep(2)
                print("You walk back outside to the town square.")
                time.sleep(2)
                items.append("handcuffs")

        if store == '2':
            print("You knock on the door of the house to ask if you can spend the night.")
            time.sleep(2)
            print("You are startled when the bandit answers the door very "
                "rudely and asks what you want.")
            time.sleep(2)
            choice = valid_input("Do you want to (1) run away or (2) challenge the bandit to a fight?\n",
                            "1", "2")
            if choice == '1':
                print("You run away, back towards the town square.")
                time.sleep(2)
            if choice == '2':
                if "handcuffs" in items:
                    print("Luckily, you are prepared! You fight the bandit and win, "
                        "putting the handcuffs on his wrists.")
                    time.sleep(2)
                    print("You secure him there and leave to find the sheriff.")
                    time.sleep(2)
                    #break
                else:
                    print("You do your best, but you don't have anything to fight with.")
                    time.sleep(2)
                    print("The bandit overpowers you and locks you in the closet.")
                    time.sleep(2)
                # Quit the program or restart from the beginning.
                play_again = valid_input("Game over! Would you like to play again? (yes/no)\n", "yes", "no")
                if 'no' in play_again:
                    print("Ok, goodbye. Thanks for playing!")
                    time.sleep(2)
                    break
                    # how to get the game to repeat from the very beginning?
                elif 'yes' in play_again:
                    print("Ok, restarting the game now.")
                    time.sleep(2)
                    if "handcuffs" in items:
                        items.remove("handcuffs")
                    break
                else:
                    print("I'm sorry, I don't understand.")
                    time.sleep(2)
                if 'no' in play_again:
                    break

    # If this break is enabled, the game will end when the player says 'no' to playing again.
    # But it will also mean that if they say 'yes' to playing again, it will end.
    break
