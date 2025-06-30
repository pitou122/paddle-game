import pygame

pygame.init()
from game import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


state = Game(screen, 1)
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        state.event_handle(event)
        if event.type == pygame.QUIT:
            running = False
    state.draw()
    state.update()
    pygame.display.update()
    clock.tick(60)