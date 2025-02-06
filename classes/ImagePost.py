import pygame
import pywhatkit
from helpers import screen, load_and_scale
from constants import *
from classes.Post import *

class ImagePost(Post):
    def __init__(self, username: str, location: str, description: str, image: str):
        super().__init__(username, location, description)
        self.image = image

    def display(self):
        super().display()
        image = load_and_scale(self.image, POST_WIDTH, POST_HEIGHT)
        screen.blit(image, (POST_X_POS, POST_Y_POS))
        
    def share(self, phone_num):
        self.add_share()
        content = "**{}'s post from Nitzagram!**\n{} likes • {} shares • {} comments\n\n".format(self.username, self.likes_counter, self.share_counter, len(self.comments))
        content += f"{self.description}"
        pywhatkit.sendwhats_image(phone_num, self.image, content)
