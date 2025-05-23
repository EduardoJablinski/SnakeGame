import random
import time


class Enemy:
    def __init__(self, position, color, speed, x_min, x_max, y_min, y_max):
        self.initial_position = position[:]  # Adicione esta linha!
        self.position = position[:]
        self.color = color
        self.speed = speed
        self.move_counter = 0
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.alive = True
        self.respawn_time = 0


    def move_towards(self, target_position):
        self.move_counter += 1
        if self.move_counter >= self.speed:
            # Decide aleatoriamente se vai tentar alinhar X ou Y primeiro
            if random.choice([True, False]):
                # Primeiro X, depois Y
                if self.position[0] != target_position[0]:
                    if self.position[0] < target_position[0]:
                        new_x = self.position[0] + 10
                        if new_x <= self.x_max:
                            self.position[0] = new_x
                    else:
                        new_x = self.position[0] - 10
                        if new_x >= self.x_min:
                            self.position[0] = new_x
                elif self.position[1] != target_position[1]:
                    if self.position[1] < target_position[1]:
                        new_y = self.position[1] + 10
                        if new_y <= self.y_max:
                            self.position[1] = new_y
                    else:
                        new_y = self.position[1] - 10
                        if new_y >= self.y_min:
                            self.position[1] = new_y
            else:
                # Primeiro Y, depois X
                if self.position[1] != target_position[1]:
                    if self.position[1] < target_position[1]:
                        new_y = self.position[1] + 10
                        if new_y <= self.y_max:
                            self.position[1] = new_y
                    else:
                        new_y = self.position[1] - 10
                        if new_y >= self.y_min:
                            self.position[1] = new_y
                elif self.position[0] != target_position[0]:
                    if self.position[0] < target_position[0]:
                        new_x = self.position[0] + 10
                        if new_x <= self.x_max:
                            self.position[0] = new_x
                    else:
                        new_x = self.position[0] - 10
                        if new_x >= self.x_min:
                            self.position[0] = new_x
            self.move_counter = 0

    def move_away(self, target_position):
        self.move_counter += 1
        if self.move_counter >= self.speed:
            if random.choice([True, False]):
                # Primeiro X, depois Y
                if self.position[0] != target_position[0]:
                    if self.position[0] < target_position[0]:
                        new_x = self.position[0] - 10
                        if new_x >= self.x_min:
                            self.position[0] = new_x
                    else:
                        new_x = self.position[0] + 10
                        if new_x <= self.x_max:
                            self.position[0] = new_x
                elif self.position[1] != target_position[1]:
                    if self.position[1] < target_position[1]:
                        new_y = self.position[1] - 10
                        if new_y >= self.y_min:
                            self.position[1] = new_y
                    else:
                        new_y = self.position[1] + 10
                        if new_y <= self.y_max:
                            self.position[1] = new_y
            else:
                # Primeiro Y, depois X
                if self.position[1] != target_position[1]:
                    if self.position[1] < target_position[1]:
                        new_y = self.position[1] - 10
                        if new_y >= self.y_min:
                            self.position[1] = new_y
                    else:
                        new_y = self.position[1] + 10
                        if new_y <= self.y_max:
                            self.position[1] = new_y
                elif self.position[0] != target_position[0]:
                    if self.position[0] < target_position[0]:
                        new_x = self.position[0] - 10
                        if new_x >= self.x_min:
                            self.position[0] = new_x
                    else:
                        new_x = self.position[0] + 10
                        if new_x <= self.x_max:
                            self.position[0] = new_x
            self.move_counter = 0

    def kill(self):
        self.alive = False
        self.respawn_time = time.time()

    def try_respawn(self):
        if not self.alive and time.time() - self.respawn_time >= 10:
            self.position = self.initial_position[:]
            self.alive = True