import pygame
from constants import *
from helpers import screen
from classes.Comment import *

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username: str, location: str, description: str):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.share_counter = 0
        self.comments = []

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
    
    def add_share(self):
        self.share_counter += 1

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # Fonts & Colors
        color = (0, 0, 0)
        font = pygame.font.SysFont("chalkduster.ttf", 20)
        font1 = pygame.font.SysFont("chalkduster.ttf", 17)
        
        # Texts
        username = font.render(self.username, True, color)
        description = font.render(self.description, True, color)
        location = font1.render(self.location, True, color)
        likes = font.render(str(self.likes_counter), True, color)
        
        # Show elements on the screen
        screen.blit(username, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        screen.blit(location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        screen.blit(likes, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = 0
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))
        # Display 4 comments starting from comments_display_index
        for i in range(1, len(self.comments) + 1):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY:
                break
