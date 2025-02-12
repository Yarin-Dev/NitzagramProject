import pygame
from helpers import screen, mouse_in_button, read_from_user, load_and_scale, put_like_sign, resolve_phone_number
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Post import *
from classes.ImagePost import *
from classes.TextPost import *
from buttons import *
from classes.Comment import Comment


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = load_and_scale('Images/background.png', WINDOW_WIDTH, WINDOW_HEIGHT)

    post1 = ImagePost("YuvalEl", "Israel", "my first post description", "images/ronaldo.jpg")
    post2 = TextPost("YuvalEl", "Israel", "and here is the second one", "Post Text", (255, 255, 255), (0, 0, 0))
    posts = [post1, post2]
    
    index = 0
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        current_post = posts[index]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # Check next post button click
                if mouse_in_button(click_post_button, pos):
                    
                    # Move to the next one or restart if reached the last post
                    index += 1
                    if index == len(posts):
                        index = 0

                # Check comment button click
                elif mouse_in_button(comment_button, pos):
                    
                    # Ask for username and content
                    username = read_from_user("Enter nickname:")
                    text = read_from_user("Enter content: ")
                    
                    # Add the comment
                    current_post.add_comment(Comment(username, text))
                
                # Check like button click
                elif mouse_in_button(like_button, pos):
                    
                    # Add the like to the post
                    current_post.add_like()
                
                # Check share button click
                elif mouse_in_button(share_button, pos):
                    share_to_num = read_from_user(title="Enter phone number to share to:")
                    
                    # Share the post to the number provided - If the number is a valid num
                    if share_to_num.isdigit():
                        current_post.share(resolve_phone_number(share_to_num))
                    
        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()
        current_post.display_comments()
        
        # Put the red heart if user make a like to the post
        if current_post.likes_counter > 0:
            put_like_sign()
        
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
        
    pygame.quit()
    quit()


main()
