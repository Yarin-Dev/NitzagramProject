import pygame
from constants import *
from helpers import screen, load_and_scale

class Comment:
    def __init__(self, nickname: str, text: str):
        
        # If reached max comment length, make it shorter
        if len(text) > MAX_COMMENT_LENGTH:
            text = text[:MAX_COMMENT_LENGTH] + '..'
            
        self.nickname = nickname
        self.text = text
    
    def display(self, position_index: int):
        """
        Displays the comment sorted by position_index.
        :return: None
        """
        font = pygame.font.SysFont("chalkduster.ttf",
                                   20)
        text = font.render(self.nickname + ': ' + self.text, True, GREY)
        
        text_x = DESCRIPTION_TEXT_X_POS + 20
        text_y = DESCRIPTION_TEXT_Y_POS + 30 * position_index
        
        user_profile = load_and_scale('NitzagramProject-main/Images/user-profile.png', 30, 27)
        screen.blit(text, (text_x, text_y))
        screen.blit(user_profile, (text_x - 30, text_y - 7))