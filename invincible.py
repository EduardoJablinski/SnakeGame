import random
import time
from settings import window_x, window_y, blue, white

class Invincible:
    def __init__(self):
        self.position = [random.randrange(1, (window_x//10)-1) * 10, 
                         random.randrange(1, (window_y//10)-1) * 10]
        self.visible = False
        self.start_time = time.time()
        self.color = blue
        self.color_last_switch = time.time()

    def spawn(self):
        self.position = [random.randrange(1, (window_x//10)-1) * 10, 
                         random.randrange(1, (window_y//10)-1) * 10]
        self.visible = True
        self.start_time = time.time()
        self.color_last_switch = time.time()

    def update_color(self):
        current_time = time.time()
        if current_time - self.color_last_switch >= 1:
            self.color_last_switch = current_time
        elif current_time - self.color_last_switch < 0.1:
            self.color = white
        else:
            self.color = blue