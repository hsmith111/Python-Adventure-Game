import time

import random

items = []

weapon = ['knife', 'sword', 'axe', 'hammer']

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("I'm sorry, that is not an option.")
    return response

while True:
    #intro
    print_pause("You find yourself in a small town, filled with a few shops and a lot of houses.")
    print_pause("You've heard that there is a robber who breaks into homes every night, "
            "stealing everything of value.")
    print_pause("You're here to stop him.")
    print_pause("All you have in your pockets is a pack of chewing gum and a little bit of money.")
    print_pause("In front of you is a general store.")
    print_pause("To your left is a very pretty little house with a garden and a swing.")
    #choice of direction to move
    while True:
        store = valid_input("Would you like to go in the general store or the house?\n\n"
                            "Enter 1 for the general store.\n"
                            "Enter 2 for the house.\n", "1", "2")
        if store == '1':
            if "handcuffs" in items:
                print_pause("You enter the general store.")
                print_pause("You already used your money to buy supplies, so there is nothing"
                    " more for you to do in here.")
                print_pause("You walk back outside to the town square.")
            else:
                weapon = random.choice(weapon)
                print_pause("You enter the general store and browse the shelves.")
                print_pause(f"You use the money in your pocket to buy a {weapon} and a pair of handcuffs.")
                print_pause("You walk back outside to the town square.")
                items.append("handcuffs")

        if store == '2':
            print_pause("You knock on the door of the house to ask if you can spend the night.")
            print_pause("You are startled when the bandit answers the door very "
                "rudely and asks what you want.")
            choice = valid_input("Do you want to (1) run away or (2) challenge the bandit to a fight?\n",
                            "1", "2")
            if choice == '1':
                print_pause("You run away, back towards the town square.")
            if choice == '2':
                if "handcuffs" in items:
                    print_pause("Luckily, you are prepared! You fight the bandit and win, "
                        "putting the handcuffs on his wrists.")
                    print_pause("You secure him there and leave to find the sheriff.")
                    #break
                else:
                    print_pause("You do your best, but you don't have anything to fight with.")
                    print_pause("The bandit overpowers you and locks you in the closet.")
                # Quit the program or restart from the beginning.
                play_again = valid_input("Game over! Would you like to play again? (yes/no)\n", "yes", "no")
                if 'no' in play_again:
                    print_pause("Ok, goodbye. Thanks for playing!")
                    break
                    # how to get the game to repeat from the very beginning?
                elif 'yes' in play_again:
                    print_pause("Ok, restarting the game now.")
                    if "handcuffs" in items:
                        items.remove("handcuffs")
                    break
                else:
                    print_pause("I'm sorry, I don't understand.")
                if 'no' in play_again:
                    break

    # If this break is enabled, the game will end when the player says 'no' to playing again.
    # But it will also mean that if they say 'yes' to playing again, it will end.
    break
