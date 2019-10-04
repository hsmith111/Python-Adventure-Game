import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("I'm sorry, that is not an option.")
    return response


def intro():
    print_pause("You find yourself in a small town, filled "
                "with a few shops and a lot of houses.")
    print_pause("You've heard that there is a robber who "
                "breaks into homes every night, stealing everything of value.")
    print_pause("You're here to stop him.")
    print_pause("All you have in your pockets is a pack "
                "of chewing gum and a little bit of money.")
    print_pause("In front of you is a general store.")
    print_pause("To your left is a very pretty little house "
                "with a garden and a swing.")


def choose_direction(items):
    store = valid_input("Would you like to go in the general store "
                        "or the house?\n\nEnter 1 for the general "
                        "store.\nEnter 2 for the house.\n", "1", "2")
    if store == '1':
        general_store(items)
    if store == '2':
        house(items)


def general_store(items):
    weapon = ['knife', 'sword', 'pickaxe', 'hammer']
    # if you already bought the handcuffs and
    # weapon, you can't buy anything more
    if "handcuffs" in items:
        print_pause("You enter the general store.")
        print_pause("You already used your money to buy "
                    "supplies, so there is nothing"
                    " more for you to do in here.")
        print_pause("You walk back outside to the town square.")
        choose_direction(items)
    # if you don't have a weapon yet, you'll buy one here
    else:
        weapon = random.choice(weapon)
        print_pause("You enter the general store and browse the shelves.")
        print_pause(f"You use the money in your pocket to buy a {weapon} and "
                     "a pair of handcuffs.")
        print_pause("You walk back outside to the town square.")
        items.append("handcuffs")
        choose_direction(items)


def house(items):
    print_pause("You knock on the door of the house "
                "to ask if you can spend the night.")
    print_pause("You are startled when the bandit answers the door very "
                "rudely and asks what you want.")
    choice = valid_input("Do you want to (1) run away or "
                         "(2) challenge the bandit to a fight?\n",
                         "1", "2")
    if choice == '1':
        print_pause("You run away, back towards the town square.")
        choose_direction(items)
    if choice == '2':
        # if you have the handcuffs and weapon, you can defeat the bandit
        if "handcuffs" in items:
            print_pause("Luckily, you are prepared! You fight "
                        "the bandit and win, "
                        "putting the handcuffs on his wrists.")
            print_pause("You secure him there and leave to find the sheriff.")
            print_pause("Game over, you win!!")
        # if you have no weapon, the bandit will win the fight
        else:
            print_pause("You do your best, but you don't have "
                        "anything to fight with.")
            print_pause("The bandit overpowers you and locks "
                        "you in the closet.")
            print_pause("Game over! You lost.")
        play_again(items)


def play_again(items):
    play_again = valid_input("Would you like to play again? "
                             "(yes/no)\n", "yes", "no")
    if play_again == 'no':
        print_pause("Ok, goodbye. Thanks for playing!")
    if play_again == 'yes':
        print_pause("Ok, restarting the game now.")
        # resetting the list of items so that you
        # don't still have the handcuffs and weapon
        if "handcuffs" in items:
            items.remove("handcuffs")
        intro()
        choose_direction(items)


def play_game():
    items = []
    intro()
    choose_direction(items)


play_game()


if __name__ == "__main__":
    play_game()
