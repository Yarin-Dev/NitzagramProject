from constants import *
from classes.Post import *
import pygame
from helpers import screen
from helpers import center_text
import pywhatkit

class TextPost(Post):
    def __init__(self, username: str, location: str, description: str, text: str, color: tuple, text_color: tuple):
        super().__init__(username, location, description)
        self.text = text
        self.color = color
        self.text_color = text_color

    def display(self):
        super().display()
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.color, square)
        font = pygame.font.SysFont("chalkduster.ttf", 30)
        text = font.render(self.text, True, self.text_color)
        obj = center_text(1, text, 1)
        screen.blit(text, (obj.x, obj.y))
        
    def share(self, phone_num):
        content = "**{}'s post from Nitzagram!**\n{} likes • {} shares • {} comments\n\n".format(self.username, self.likes_counter, self.share_counter, len(self.comments))
        content += f"*{self.text}*\n{self.description}"
        pywhatkit.sendwhatmsg_instantly(phone_num, content)
        
