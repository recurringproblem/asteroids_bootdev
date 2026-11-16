from circleshape import *
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        old_radius = self.radius
        new_angle = random.uniform(30, 50)
        split_one_angle = self.velocity.rotate(new_angle)
        split_two_angle = self.velocity.rotate(-new_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_one.velocity = split_one_angle * 1.2
        new_asteroid_two.velocity = split_two_angle * 1.2
