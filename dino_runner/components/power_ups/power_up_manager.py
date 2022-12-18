import random, pygame
from dino_runner.components.power_ups.shield import Shield
class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.points = 0

    def update(self,points,game_speed, player):
        self.generate_power_ups(points)
        for powerup in self.power_ups:
            powerup.update(game_speed,self.power_ups)
            if player.dino_rect.colliderect(powerup.rect):
                powerup.start_time = pygame.time.get_ticks()
                player.shield = True
                player.type = powerup.type
                powerup.start_time = pygame.time.get_ticks()
                player.shield_time_up = powerup.start_time + (random.randint(5,8)*1000)
                self.power_ups.remove(powerup)

    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups)==0:
            if self.when_appers==points:
                self.when_appers = random.randint(self.when_appers + 150, self.when_appers + 500)
                self.power_ups.append(Shield())