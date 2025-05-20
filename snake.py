from settings import yellow, orange

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.color = yellow
        self.color_visible = False
        self.color_start_time = 0
        self.power_ready = True
        self.power_active = False
        self.power_duration = 5
        self.power_cooldown = 10
        self.power_start_time = 0
        self.power_cooldown_start = 0
        self.energy_max = 3.0  # segundos de poder
        self.energy = self.energy_max
        self.energy_recharge = 0.5  # segundos para recarregar 0.1 de energia
        self.last_energy_update = 0
        self.power_speed = 2
        self.normal_speed = 1
        self.speed = self.normal_speed

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

    def activate_power(self, orange, current_time):
        if self.power_ready and not self.power_active:
            self.color = orange
            self.speed = self.power_speed
            self.power_active = True
            self.power_ready = False
            self.power_start_time = current_time

    def update_energy(self, space_pressed, current_time):
        # Consome energia se espaço está pressionado
        if space_pressed and self.energy > 0:
            if self.speed != self.power_speed:
                self.speed = self.power_speed
            self.energy -= current_time - self.last_energy_update
            if self.energy < 0:
                self.energy = 0
        else:
            if self.speed != self.normal_speed:
                self.speed = self.normal_speed
            # Recarrega energia
            if self.energy < self.energy_max:
                self.energy += (current_time - self.last_energy_update) / self.energy_recharge
                if self.energy > self.energy_max:
                    self.energy = self.energy_max
        self.last_energy_update = current_time