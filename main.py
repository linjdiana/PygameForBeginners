import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello Code Blooded!")
CYAN = (179, 229, 252)
FPS = 60
VEL = 5 #velocity

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def draw_window(red, yellow):
    WIN.fill(CYAN)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: #LEFT; a key means you can move left at the rate of velocity
            yellow.x -= VEL
    if keys_pressed[pygame.K_d]: #RIGHT; a key means you can move right at the rate of velocity
            yellow.x += VEL
    if keys_pressed[pygame.K_w]: #UP; note it's the y axis being changed
            yellow.y -= VEL
    if keys_pressed[pygame.K_s]: 
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: #LEFT; a key means you can move left at the rate of velocity
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: #RIGHT; a key means you can move right at the rate of velocity
            red.x += VEL
    if keys_pressed[pygame.K_UP]: #UP; note it's the y axis being changed
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN]: 
            red.y += VEL          


def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed() 
        yellow_handle_movement(keys_pressed, yellow)
        

        draw_window(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
    