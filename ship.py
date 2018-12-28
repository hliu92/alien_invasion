import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialize ship and set original location"""
        self.screen = screen #screen: where to draw ship
        self.ai_settings = ai_settings

        # load ship image and cap outside rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new ship in bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float number in center of ship
        self.center = float(self.rect.centerx)

        # movement sign
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust ship location based on movement sign"""
        # update ship center instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object with self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship in designated location"""
        self.screen.blit(self.image, self.rect)
