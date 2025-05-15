from settings import yellow

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.color = yellow
        self.color_visible = False
        self.color_start_time = 0
        self.speed = 1 

    def change_direction(self, change_to):
        if change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        for _ in range(self.speed):
            if self.direction == 'UP':
                self.position[1] -= 10
            if self.direction == 'DOWN':
                self.position[1] += 10
            if self.direction == 'LEFT':
                self.position[0] -= 10
            if self.direction == 'RIGHT':
                self.position[0] += 10
                
    def grow(self):
        self.body.insert(0, list(self.position))

    def shrink(self):
        self.body.pop()

    def reset_color(self, yellow):
        self.color = yellow
        self.color_visible = False

    def set_invincible(self, blue, current_time):
        self.color = blue
        self.color_start_time = current_time
        self.color_visible = True