import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from random import uniform


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = uniform(20, 50)
        velocity_a = self.velocity.rotate(random_angle)
        velocity_b = self.velocity.rotate(-(random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(
            x=self.position.x, y=self.position.y, radius=new_radius  # type: ignore
        )
        asteroid_a.velocity = velocity_a * 1.2
        asteroid_b = Asteroid(
            x=self.position.x, y=self.position.y, radius=new_radius  # type: ignore
        )
        asteroid_b.velocity = velocity_b * 1.2

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
