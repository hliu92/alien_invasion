import pygame

class Ship():

    def __init__(self, screen):
        """initialize ship and set original location"""
        self.screen = screen #screen: where to draw ship

        # load ship image and cap outside rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new ship in bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement sign
        self.moving_right = False

    def update(self):
        """adjust ship location based on movement sign"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """draw ship in designated location"""
        self.screen.blit(self.image, self.rect)
