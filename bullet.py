import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a Class that manages bullets"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object on spot of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rect at (0,0) as bullet, then set the correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # save bullet location as float number
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.ship_speed_factor = ai_settings.bullet_speed_factor

        def update(self):
            """move bullet upwards"""
            # update bullet location float number
            self.y -= self.ship_speed_factor
            # update bullet rect location
            self.rect.y = self.y

        def draw_bullet(self):
            """draw bullet on screen"""
            pygame.draw.rect(self.screen, self.color, self.rect)
