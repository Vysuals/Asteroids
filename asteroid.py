import pygame
import random
from circleshape import CircleShape

ASTEROID_MIN_RADIUS = 20

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        rand_ang = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(rand_ang)
        new_vel2 = self.velocity.rotate(-rand_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast1.velocity = new_vel1 * 1.2
        new_ast2.velocity = new_vel2 * 1.2
        self.kill()
