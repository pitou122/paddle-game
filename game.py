import pygame
from config import *
from sprite import *

themes = [
    {
        "img": "img/makoto_hanaoka_1.jpg"
    },
    {
        "img": "img/march_7th_1.jpg"
    }
]

class Game:
    def __init__(self, screen, theme):
        self.font = pygame.font.Font(None, 25)
        self.screen = screen
        self.cells = pygame.sprite.Group()
        self.choices = pygame.sprite.Group()
        self.theme = theme
        self.build()
        self.target = None
        self.solution = random_solution()
        self.problem = sudoku(self.solution)
        self.reset()
        self.wrong = 0
        self.next_state = None


    def draw_image(self, name):
        image = pygame.image.load(name).convert_alpha()
        image_rect = image.get_rect(topleft = (0, 0))
        self.screen.blit(image, image_rect)

    def draw(self):
        self.draw_image(themes[self.theme]["img"])
        self.cells.update(self.target)
        self.cells.draw(self.screen)
        self.choices.draw(self.screen)

    def reset(self):
        for cell in self.cells:
            x , y = divmod(cell.id, 9)
            text = self.problem[x][y] if self.problem[x][y] else EMPTY
            cell.set_text(text)


    def build(self):
        for i in range(9):
            x , y = PADDING + 9 + i * SQUARE_EDGE, 600
            number = Number(x , y , CHOICE_EDGE, CHOICE_EDGE , i +1 , self.font)
            self.choices.add(number)
        for i in range(9):
            for j in range(9):
                x ,y = PADDING + i * SQUARE_EDGE, PADDING + j * SQUARE_EDGE
                cell = Cell(x , y, SQUARE_EDGE, i*9 + j, self.font)
                self.cells.add(cell)


    def event_handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            cell_selected = [cell for cell in self.cells if cell.rect.collidepoint(x,y)]
            number_selected = [number for number in self.choices if number.rect.collidepoint(x, y)]
            if cell_selected:
                if self.target == cell_selected[0]:
                    self.target = None
                else:
                    self.target = cell_selected[0]
            elif number_selected:
                tx, ty = divmod(self.target.id, 9)
                if self.target is None: return
                if self.problem[tx][ty]: return
                number = number_selected[0].string
                if number == self.solution[tx][ty]:
                    string = "correct"
                else:
                    string = "wrong"
                    self.wrong += 1

                self.target.set_text(number, string)
            else:
                self.target = None
