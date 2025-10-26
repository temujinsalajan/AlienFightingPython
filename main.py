import pygame
from setting import Settings
from ship import Ship
from game_functions import check_events, update_screen  
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien


def run_game():

    ai_settings = Settings()
    
    

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Simple Pygame Window")
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    for i in range(5):
        alien = Alien(ai_settings, screen)
        aliens.add(alien)
    running = True
    while running:
        check_events(ai_settings, screen, ship, bullets)  # Check for events like keypresses and window closing
        ship.update()  # Update the ship's position based on movement flags
        bullets.update()  # Update the position of bullets
        aliens.update()  # Update the position of aliens
        update_screen(ai_settings, screen, ship, bullets, aliens)  # Update the screen with the ship and bullets

run_game()