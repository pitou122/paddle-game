import pygame
from pygame.examples.music_drop_fade import play_next

from config import *
from sprite import Route

route = [
    {
        "img": "img/march_7th_1.jpg"
    }
]


class Menu:
    def __init__(self , screen):
        self.screen = screen
        self.routes = pygame.sprite.Group()
        self.next_state = None
        self.play_theme = None
        self.route_num = 1
        for i in range(self.route_num):
            self.build(0 , (i + 1) * 100,  route[i]["img"],i)

    def build(self, x, y , img, id):
        self.routes.add(Route(x, y, img, id))

    def draw_text(self, size, text, color, center):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color).convert_alpha()
        text_rect = text.get_rect(center = center)
        self.screen.blit(text, text_rect)


    def draw(self):
        rect = pygame.Rect(0,0,WIDTH, 100)
        pygame.draw.rect(self.screen, BLOCK_COLOR, rect)
        self.draw_text(50, "Route List", WHITE, rect.center)
        for i in range(1 , len(self.routes) + 1, 1):
            rect = pygame.Rect(0, i * 100, WIDTH, 100)
            pygame.draw.rect(self.screen, TARGET_COLOR, rect)
        self.routes.draw(self.screen)

    def event_handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            chosen_route = [route for route in self.routes if route.rect.collidepoint(pos)]
            if chosen_route:
                self.next_state = "play"
                self.play_theme = chosen_route[0].id





