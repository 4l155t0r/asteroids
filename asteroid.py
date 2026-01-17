import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Logic to split the asteroid into smaller pieces

        # Destroy the current asteroid
        self.kill()

        # If the asteroid is too small, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        # Otherwise, create two smaller asteroids
        else:
            log_event(f"asteroid_split")

            # Create two new asteroids with smaller radius
            random_angle1 = uniform(20, 50)
            a1_rotation = self.velocity.rotate(random_angle1)
            a2_rotation = self.velocity.rotate(-random_angle1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Set their velocities to be slightly bigger than the original asteroid's velocity
            asteroid1.velocity = a1_rotation * 1.2
            asteroid2.velocity = a2_rotation * 1.2
