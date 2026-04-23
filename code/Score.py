import sys
from datetime import datetime

import pygame
from plotly.graph_objs.volume import Surface
from pygame import Rect
from pygame.constants import K_BACKSPACE
from pygame.font import Font

from code.Const import MUSIC_FILE, FILEPATH, COLOR_YELLOW, SCORE_POS, MENU_OPTION, DB_NAME, COLOR_WHITE
from code.DbProxy import DbProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load(f'./asset/{FILEPATH['Score']}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer.music.load(MUSIC_FILE['Score'])
        pygame.mixer.music.play(-1)
        db_proxy = DbProxy(DB_NAME)
        winner_name: str = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!!', COLOR_YELLOW, SCORE_POS['Title'])
            text: str = ''

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1\'s  name (4 characters)'
            elif game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team\'s  name (4 characters)'
            elif game_mode == MENU_OPTION[2]:
                score = max(player_score)
                player = 'Player 1' if player_score[0] == score else 'Player 2'
                text = f"Enter {player}'s name (4 characters)"

            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(winner_name) == 4:
                        db_proxy.save({'name': winner_name, 'score': score, 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        winner_name = winner_name[:-1]
                    else:
                        if len(winner_name) < 4:
                            winner_name += event.unicode

            self.score_text(20, winner_name, COLOR_WHITE, SCORE_POS['Name'])

            pygame.display.flip()

    def show(self):
        pygame.mixer.music.load(MUSIC_FILE['Score'])
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME    SCORE    DATE', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DbProxy(DB_NAME)
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            _, name, score, date = player_score
            self.score_text(20, f'{name}    {score: 05d}    {date}', COLOR_YELLOW, SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/%m/%Y')
    return f'{current_time} - {current_date}'
