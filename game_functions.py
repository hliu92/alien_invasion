import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # respond to keydown
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """if < limit, then fire a bullet"""
    # create a bullet and add it to Group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # respond to keyup
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # respond to mouse or keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update image on screen, and switch to new screen"""
    # redraw screen in each loop
    screen.fill(ai_settings.bg_color)
    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # make the latest screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update bullets locations and remove vanished bullets"""
    # update bullets locations
    bullets.update()

    # remove vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """react to collisions"""
    # remove collided bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # delete current bullets and create new alien fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    """calculate how many aliens in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """calculate how many rows"""
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and put in current row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """create alien fleets"""
    # create an alien, and calculate how many aliens in a row
    # space between aliens is the width of alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # create aliens fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

def check_fleet_edges(ai_settings, aliens):
    """take action when alien reach edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """move all aliens down, and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """react to ship and alien collision"""
    if stats.ships_left > 0:
        # deduct 1 ship left
        stats.ships_left -= 1

        # empty alien and bullet
        aliens.empty()
        bullets.empty()

        # create new alien fleet, reset ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if aliens reached screen bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat like ship collided
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """check if aliens at edge, and update all aliens' location"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check if ship and alien collided
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # check if aliens reach screen bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
