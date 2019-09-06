import os
import csv

from Components.player import Player
from Components.location import Location


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

        self.locations = []
        for city_name in STATIONS:
            location = Location(city_name)
            self.locations.append(location)

    def what_neighbour(self):
        for location in self.locations:
            if self.locations.index(location) not in [0, len(self.locations) - 1]:
                location.add_neighbor(
                    self.locations[self.locations.index(location) - 1])
                location.add_neighbor(
                    self.locations[self.locations.index(location) + 1])
            elif self.locations.index(location) > 0:
                location.add_neighbor(
                    self.locations[self.locations.index(location) - 1])
            else:
                location.add_neighbor(
                    self.locations[self.locations.index(location) + 1])

    def travel(self):
        neighborhood = []

        print("You're currently in ", end='')
        print(self.locations[self.player.position], ".", sep='')
        print("\nYou can go to: ")
        for neighbor in self.locations[self.player.position].neighbor_list:
            print(" -> ", neighbor, sep='')

        while True:
            destination = input("\nWhere do you want to go?: ")
            for neighbor in self.locations[self.player.position].neighbor_list:
                neighborhood.append(neighbor.name)

            if destination in neighborhood:
                break

        os.system('cls' if os.name == 'nt' else 'clear')

        for location in self.locations:
            if destination == location.name:
                new_position = self.locations.index(location)
        self.player.change_position(new_position)
        print("You arrived:", self.locations[self.player.position])

    def play(self):
        self.what_neighbour()
        self.travel()
        self.locations[self.player.position].neighbor_list.clear()
