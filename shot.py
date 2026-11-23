from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
