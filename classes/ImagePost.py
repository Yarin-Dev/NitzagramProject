from constants import *
from classes.Post import *
import pygame
from helpers import screen

class ImagePost(Post):
    def __init__(self, username: str, location: str, description: str, image: str):
        super().__init__(username, location, description)
        self.image = image

    def display(self):
        super().display()
        img = pygame.image.load(self.image)
        image = pygame.transform.scale(img,(POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))