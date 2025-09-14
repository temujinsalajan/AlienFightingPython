import pygame
from setting import Settings
from ship import Ship
from game_functions import check_events, update_screen  


def run_game():

    ai_settings = Settings()
    
    

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Simple Pygame Window")
    ship = Ship(screen)
    running = True
    while running:
        check_events(ship)  # Check for events like keypresses and window closing
        ship.update()  # Update the ship's position based on movement flags
        update_screen(ai_settings, screen, ship)  # Update the screen with the ship

run_game()