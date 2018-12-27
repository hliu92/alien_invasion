import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height)) #screen: surface
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen)

    # start main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai.settings, screen, ship)

run_game()
