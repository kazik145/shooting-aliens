import pygame
class Settings:

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.background = pygame.image.load('images/sky.jpg')

        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (51, 204, 204)
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1