import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Wrap around screen edges
        # if self.position.x < 0:
        #     self.position.x = 800
        # elif self.position.x > 800:
        #     self.position.x = 0
        # if self.position.y < 0:
        #     self.position.y = 600
        # elif self.position.y > 600:
        #     self.position.y = 0