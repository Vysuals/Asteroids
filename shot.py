import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
