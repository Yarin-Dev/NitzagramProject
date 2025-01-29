import constants
from Post import Post
import pygame

class ImagePost(Post):
    def __init__(self, image):
        super().__init__()
        self.image = image