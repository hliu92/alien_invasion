import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class for a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize liens and set its initial location"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image, set rect settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # each alien starts from top left corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save aliens' exact location
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien on designated location"""
        self.screen.blit(self.image, self.rect)
