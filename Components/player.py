class Player(object):
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    def __str__(self):
        return self.name

    def change_position(self, new_position):
        self.position = new_position