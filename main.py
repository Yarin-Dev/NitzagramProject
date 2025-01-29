import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Post import *
from classes.ImagePost import *
from classes.TextPost import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Niggagram')

    clock = pygame.time.Clock()

    # Set up background image
    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = ImagePost("YuvalEl", "Israel", "my first post description", "images/ronaldo.jpg")
    post2 = TextPost("YuvalEl", "Israel", "and here is the second one", "Post Text", (255, 255, 255), (0, 0, 0))
    posts = [post1, post2]

    index = 0
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ((POST_X_POS  <= pos[0] <= POST_X_POS + POST_WIDTH) and (POST_Y_POS <= pos[1] <= POST_Y_POS + POST_HEIGHT)):
                    index += 1
                    if index == len(posts):
                        index = 0

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        posts[index].display()
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
