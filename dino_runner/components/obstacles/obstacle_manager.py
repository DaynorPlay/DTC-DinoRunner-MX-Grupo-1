#obstacle_manager.py
import random, pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles)==0:
            cactus_size = random.randint(0,3)

            if cactus_size == 0:
                smallCactus = Cactus(SMALL_CACTUS)
                smallCactus.rect.y = 325
                self.obstacles.append(smallCactus)
            elif cactus_size == 1 or cactus_size==2:
                pos_bird = [235,272,327]
                pos = random.randint(0,2)
                bird = Bird(BIRD)
                bird.rect.y = pos_bird[pos]
                self.obstacles.append(bird)
            else:
                largeCactus = Cactus(LARGE_CACTUS)
                largeCactus.rect.y = 305
                self.obstacles.append(largeCactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect) and not(game.player.shield):
                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                else:
                    pygame.time.delay(1000)
                    game.death_count +=1
                    self.obstacles.remove(obstacle)
                    game.playing = False
                    break
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)