import pygame
from ship import Ship
from bullet import Bullet
import game_functions as gf

from pygame.sprite import Group


def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Invasão Aliens")

    ship = Ship(screen)
    bullets = Group()

    while True:
        gf.check_events(bullets,screen,ship)
        ship.update()
        bullets.update()
        gf.update_screen(screen,ship,bullets)


run_game()