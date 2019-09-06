import os

from game import Game


def intro(name):
    with open("intro.txt", "r") as intro_file:
        header = intro_file.readline()
        body = intro_file.read()

    print(header)
    print("Hello ", name, "!", sep='')
    print(body)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Whats your name?: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    intro(name)
    game = Game(name)

    again = None
    while again != "n":
        game.play()
        again = input("\nDo you still want to travel? [Y/N]: ")
        os.system('cls' if os.name == 'nt' else 'clear')


main()
input("To exit, press Enter.")
