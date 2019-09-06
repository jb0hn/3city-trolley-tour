class Location(object):
    def __init__(self, name):
        self.name = name
        self.neighbor_list = []

    def __str__(self):
        return self.name

    def add_neighbor(self, new_neighbor):
        self.neighbor_list.append(new_neighbor)
