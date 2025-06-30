import pygame

pygame.init()
from game import *
from menu import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


state = Menu(screen)
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        state.event_handle(event)
        if event.type == pygame.QUIT:
            running = False
    state.draw()
    if state.next_state == "play":
        state = Game(screen, state.play_theme)
    pygame.display.update()
    clock.tick(60)