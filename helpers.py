import pygame

from constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def from_text_to_array(text):
    """
    the function get text and break it into sentences that fits the screen, in
    case the text too long to for one line
    :param text: string
        text to show on screen
    :return: list of sentences
    """
    text_array = []
    text_to_edit = text
    if len(text) > 20:
        while not (len(text_to_edit) <= 0):
            if len(text_to_edit) < LINE_MAX_LENGTH:
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[0: LINE_MAX_LENGTH]
                text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                while not (temp[-1] == ' ') and not (temp[-1] == ','):
                    text_to_edit = temp[-1] + text_to_edit
                    temp_len = int(len(temp))
                    temp = temp[0: temp_len - 1]
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def draw_text_box():
    pygame.draw.rect(screen, GREY, pygame.Rect(
        VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS, 300, 20))
    pygame.draw.rect(screen, WHITE,
                     pygame.Rect(VIEW_MORE_COMMENTS_X_POS + 1,
                                 VIEW_MORE_COMMENTS_Y_POS + 1, 298, 18))
    pygame.display.flip()


def draw_title(title: str):
    # A ract to remove prevoius texts
    pygame.draw.rect(screen, WHITE, 
                     (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS - 20, 100, 10)) 
    
    title_text = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE).render(title, True, LIGHT_GRAY)
    screen.blit(title_text, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS - 20))
    pygame.display.flip()


# Get the comment that the user typed will using Nitzagram and translate it
# to string
def read_from_user(title):
    """
    Read the comment the user type.
    :return: string
        return typed comment
    """
    pressed_enter = False
    new_comment = ""
    # Draw the rectangle where the user can see the comment he typed
    draw_text_box()
    draw_title(title)
    while not pressed_enter:
        # get the string for comment
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                draw_text_box()
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                # command to add len ! = 0
                elif event.key == pygame.K_BACKSPACE \
                        and not (len(new_comment) == 0):
                    new_comment = new_comment[:-1]
                else:
                    new_comment += event.unicode
                font2 = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=False)
                img2 = font2.render(new_comment, True, (50, 50, 50))
                screen.blit(img2,
                            (VIEW_MORE_COMMENTS_X_POS + 1,
                             VIEW_MORE_COMMENTS_Y_POS + 1))
                pygame.display.update()
    return new_comment


def center_text(num_of_rows, text_to_display, row_number):
    """
    center a sentence on screen
    :param num_of_rows: int
        number of sentences on screen
    :param text_to_display: string
        sentence to center
    :param row_number: int
        sentence row number in total text
    :return: tuple
        position of centered text
    """
    horizontal_margin = \
        (POST_HEIGHT - num_of_rows * TEXT_POST_FONT_SIZE) // 2
    # Get the text object size (height and width)
    text_rect = text_to_display.get_rect()
    # Center the text to the center of X axis
    text_rect.x = ((POST_WIDTH - text_rect.width) // 2) + 20
    # Center the text to the center of the post on Y axis
    text_rect.y = (POST_Y_POS + horizontal_margin +
                   row_number * TEXT_POST_FONT_SIZE)
    return text_rect


def load_and_scale(path: str, width: int, height: int):
    """
    Load and scale an image.
    
    :param path: str
        Image path on the project folder
    :param width: int
        Image new width
    :param height: int
        Image new height
    :return: Surface
        The element
    """
    image = pygame.image.load(path)
    return pygame.transform.scale(image,
                                        (width, height))


def put_like_sign():
    """
    Changes the like click sign (Red heart)
    :return: None
    """
    img = load_and_scale('NitzagramProject-main/Images/red-heart.png', LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    screen.blit(img, (LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS))
    

def resolve_phone_number(phone_num: str) -> str:
    """
    Resolves a phone num to IL's starting nums
    :param phone_num: int
        Phone num to resolve
    :return: int
        Resolved phone num
    """
    if phone_num.startswith("0"):  
        phone_num = "+972" + phone_num[1:]
        
    return phone_num
