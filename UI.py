### Importing libraries
import pygame
from question import Question



### Defining variables
## Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

## Constants
INITIAL_WINDOW_WIDTH = 1200
INITIAL_WINDOW_HEIGHT = 800
MAX_FPS = 60



# Background Texture
bg_img = pygame.image.load('sources/bg/backgroundColorDesert.png')
bg_img = pygame.transform.scale(bg_img, (INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))

# Sprite textures
char_img = pygame.image.load('sources/sprites/character_maleAdventurer_walk0.png')
mon_img = pygame.image.load('sources/sprites/character_zombie_idle.png')
char_size = char_img.get_size()
mon_size = mon_img.get_size()
char_img = pygame.transform.scale(char_img, (char_size[0] * 2, char_size[1] * 2))
mon_img = pygame.transform.scale(mon_img, (mon_size[0] * 2, mon_size[1] * 2))
### Functions

# creates a button at (x,y) that's width*height
# button is labeled with text
# upon clicking the button, run onClick
def create_button(event, x, y, width, height, text, onClick):
    text_btn_font = pygame.font.SysFont("Verdana", 25)
    pygame.draw.rect(screen, BLACK, [x, y, width, height])
    screen.blit(text_btn_font.render(text, True, WHITE), (x+20, y+15))
    
    # checking for clicks
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        
        if x <= pos[0] and pos[0] <= x + width:
            if y <= pos[1] and pos[1] <= y + height:
                onClick()



def print_text(x, y,text):
    question_title_font = pygame.font.SysFont("Verdana", 30)

    screen.blit(question_title_font.render(text, True, BLACK), (x, y))
   

# placeholder for the recommender function that gives a sorted list of recommended self care activities
def sorted_self_care_activities(issue):
    return ["Read a book", "Do a puzzle", "Take a 10 min walk", "Do some stretches", "Do a breathing exercise"]


new_question = Question()
def fighting_screen(event):
    moves = sorted_self_care_activities("depression")
    text = new_question.get_answers()
    text1 = text[0]
    text2 = text[1]
    text3 = text[2]
    text4 = text[3]
    def clickedOption1():
        # new_question.save_answer(text1)
        print("user is " + text1)
    def clickedOption2():
        # new_question.save_answer(text2)
        print("user is " + text2)
    def clickedOption3():
        # new_question.save_answer(text3)
        print("user is " + text3)
    def clickedOption4():
        # new_question.save_answer(text4)
        print("user is " + text3)
    
    create_button(event, 250, 720, 300, 60, text1, clickedOption1)
    create_button(event, 250, 620, 300, 60, text2, clickedOption2)
    create_button(event, 700, 620, 300, 60, text3, clickedOption3)
    create_button(event, 700, 720, 300, 60, text4, clickedOption4)

    text = new_question.get_opening_question()
    print_text(350,540,text)


def movement_scene(event, x):
    # Function for character moving to monster
    screen.blit(mon_img, (x_mon_init , y))
    if abs(x[-1] - x_mon_init) > 100:
        x.append(x[-1] + 2)
        screen.blit(char_img, (x[-1], y))
        x.remove(x[-2])
    else:
        screen.blit(char_img, (x[-1], y))



### Main
pygame.init()

# Creating pygame window
size = (INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Fighting a monster")

# Initialise movement event variables
y = INITIAL_WINDOW_HEIGHT * 0.6
x_mon_init = INITIAL_WINDOW_WIDTH * 0.7
x_char_pos = [INITIAL_WINDOW_WIDTH * 0.1]

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

screen.fill(WHITE)

font = pygame.font.SysFont("Arial", 14)

# -------- Main Program Loop -----------
carryOn = True
while carryOn:
    screen.blit(bg_img, (0, 0))
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False

    movement_scene(event, x_char_pos)
    if abs(x_char_pos[-1] - x_mon_init) <= 100:
        screen.blit(bg_img, (0,0))
        DEFAULT_IMAGE_SIZE = (300, 400)
        image_char = pygame.transform.scale(char_img, DEFAULT_IMAGE_SIZE)
        image_mons = pygame.transform.scale(mon_img, DEFAULT_IMAGE_SIZE)

        screen.blit(image_char, (200,200))
        screen.blit(image_mons, (700,200))
        fighting_screen(event)
    # Initial positions

    pygame.display.flip()   # updates screen to include anything new that was drawn
    clock.tick(MAX_FPS)     # sets the fps

pygame.quit()