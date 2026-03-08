#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from .const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, KEYDOWN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/city.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Aqui criamos a fonte e renderizamos o texto
        font = pygame.font.SysFont(None, text_size)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        # Desenha o texto na janela
        self.window.blit(text_surf, text_rect)

    def run(self, if_event=None):
        menu_option = 0
        pygame.mixer_music.load('./asset/game-boss-music.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Chamada correta do método que você criou acima:
            self.menu_text(70, 'City', (255, 128, 0), (WIN_WIDTH / 2, 80))
            self.menu_text(70, 'Shooter', (255, 128, 0), (WIN_WIDTH / 2, 130))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 300 + 40 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 300 + 40 * i))
            


            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit()  # Quit the game
                type: object
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Down Key
                        if menu_option <len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # Up Key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

            pygame.display.flip()

            ## minuto 20


# Every text will be like am image on screen

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)