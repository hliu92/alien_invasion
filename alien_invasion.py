import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height)) #screen: surface
    pygame.display.set_caption("Alien Invasion")

    # create stats that saves game stats
    stats = GameStats(ai_settings)

    # create a ship, a bullets Group and an aliens Group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create aliens Group
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
