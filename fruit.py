import random
from settings import window_x, window_y

class Fruit:
    def __init__(self):
        self.position = [random.randrange(1, (window_x//10)-1) * 10, 
                         random.randrange(1, (window_y//10)-1) * 10]
        self.spawn = True

    def respawn(self):
        self.position = [random.randrange(1, (window_x//10)-1) * 10, 
                         random.randrange(1, (window_y//10)-1) * 10]
        self.spawn = True