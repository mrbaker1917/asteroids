import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, radius=SHOT_RADIUS)
        self.velocity = velocity
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt