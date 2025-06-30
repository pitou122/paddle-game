import pygame

from config import *
from calc import *





class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, edge , id, font):
        super().__init__()
        self.string = EMPTY
        self.image = pygame.Surface((edge, edge) , pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (y, x))
        self.color = BLOCK_COLOR
        self.text_color = WHITE
        self.draw()
        self.font = font
        self.id = id

    def draw(self):
        self.image.fill(self.color)
        pygame.draw.rect(self.image, WHITE, self.image.get_rect(), 1)

        if self.string != EMPTY:
            text = self.font.render(self.string, True, self.text_color)
            text_rect = text.get_rect(center= self.image.get_rect().center)
            self.image.blit(text, text_rect)

    def set_text(self, number , type = "None"):
        if type == "wrong": self.text_color = WRONG_ANSWER_COLOR
        if type == "correct": self.text_color = TEXT_COLOR
        self.string = str(number)

    def update(self, cell_targeted):
        self.update_target(cell_targeted)
        self.draw()

    def update_target(self, cell_targeted):
        self.color = BLOCK_COLOR
        if cell_targeted is None: return
        x, y = divmod(cell_targeted.id, 9)
        ax , ay = divmod(self.id, 9)
        if ax == x or ay == y:
            self.color = TARGET_RELATED_COLOR

        target_square_owner = (x // 3) * 27 +  (y // 3) * 3
        self_square_owner = (ax // 3) * 27 + (ay // 3) * 3
        if self_square_owner == target_square_owner:
            self.color =TARGET_RELATED_COLOR

        if self == cell_targeted:
            self.color = TARGET_COLOR


class Number(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, number, font):
        super().__init__()
        self.string = number
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = WHITE
        self.font = font
        self.draw()

    def draw(self):
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), border_radius = 5)
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), 2, border_radius = 5)
        text = self.font.render(str(self.string), True, BLACK)
        text_rect = text.get_rect(center = self.image.get_rect().center)
        self.image.blit(text, text_rect)

class Route(pygame.sprite.Sprite):
    def __init__(self, x , y, img , id):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.id = id


