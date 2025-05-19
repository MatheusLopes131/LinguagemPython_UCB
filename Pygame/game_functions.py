import pygame
import sys
from bullet import Bullet

def check_events(bullet,screen,ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = True
                    ship.rect.centerx += 1

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = True
                    ship.rect.centerx -= 1

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(bullet,screen,ship)
                    bullets.add(new_bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = False

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = False

def update_screen(screen,ship,bullets):
    bg_color = (230,230,230)
    screen.fill(bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    bullets.draw_bullet()
    pygame.display.flip()