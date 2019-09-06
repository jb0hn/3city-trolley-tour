import os
import csv


class Player(object):
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    def __str__(self):
        return self.name

    def change_position(self, new_position):
        self.position = new_position


class Place(object):
    def __init__(self, name):
        self.name = name
        self.neighbor_list = []

    def __str__(self):
        return self.name

    def add_neighbor(self, new_neighbor):
        self.neighbor_list.append(new_neighbor)


class Game(object):
    def __init__(self, name):
        self.player = Player(name)

        STATIONS = []

        # import stations list from csv file
        with open("3city_stations.csv") as skm_station_file:
            reader = csv.reader(skm_station_file)
            skm_station_list = list(reader)

        # transform nested, two-dim list into one dimentional
        for station in skm_station_list:
            STATIONS.append(station[0])

        self.places = []
        for city_name in STATIONS:
            place = Place(city_name)
            self.places.append(place)

    def what_neighbour(self):
        for place in self.places:
            if self.places.index(place) not in [0, len(self.places) - 1]:
                place.add_neighbor(self.places[self.places.index(place) - 1])
                place.add_neighbor(self.places[self.places.index(place) + 1])
            elif self.places.index(place) > 0:
                place.add_neighbor(self.places[self.places.index(place) - 1])
            else:
                place.add_neighbor(self.places[self.places.index(place) + 1])

    def travel(self):
        neighborhood = []

        print("You're currently in ", end='')
        print(self.places[self.player.position], ".", sep='')
        print("\nYou can go to: ")
        for neighbor in self.places[self.player.position].neighbor_list:
            print(" -> ", neighbor, sep='')

        while True:
            destination = input("\nWhere do you want to go?: ")
            for neighbor in self.places[self.player.position].neighbor_list:
                neighborhood.append(neighbor.name)

            if destination in neighborhood:
                break

        os.system('cls' if os.name == 'nt' else 'clear')

        for place in self.places:
            if destination == place.name:
                new_position = self.places.index(place)
        self.player.change_position(new_position)
        print("You arrived:", self.places[self.player.position])

    def play(self):
        self.what_neighbour()
        self.travel()
        self.places[self.player.position].neighbor_list.clear()


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
