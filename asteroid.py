import pygame
from constants import *
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r_angle = random.uniform(20, 50)
            new_vector_a = self.velocity.rotate(r_angle)
            new_vector_b = self.velocity.rotate(-r_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_a = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_a.velocity = new_vector_a
            new_asteroid_b.velocity = new_vector_b
