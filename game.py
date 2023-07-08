import pygame
import random
import webbrowser
import time

from pygame import font

from monster import Monster
from question import Question
from dropdown import DropDown
from character_design import User



pygame.init()

### Defining variables
## Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (75, 135, 255)
BLUE = (108, 207, 255)

## Dropdown Colors
COLOR_INACTIVE = PURPLE
COLOR_ACTIVE = PURPLE
COLOR_LIST_INACTIVE = BLUE
COLOR_LIST_ACTIVE = PURPLE

## Fonts
FONT_TEXT_BUTTON = pygame.font.SysFont("Verdana", 25)
FONT_QUESTION_TITLE = pygame.font.SysFont("Verdana", 30)

## Constants
INITIAL_WINDOW_WIDTH = 1200
INITIAL_WINDOW_HEIGHT = 800
MAX_FPS = 60

# Background Texture
BACKGROUND = pygame.image.load('sources/bg/backgroundColorDesert.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))

# Other Globals
question_object = Question()



# just assign the next number available when adding new scene here
# 
# Next available number: 11
SCENE_INTRO_Q1 = 8
SCENE_INTRO_Q2 = 9
SCENE_RATE_ISSUE = 10
SCENE_TRAVELLING = 6
SCENE_FIGHTING = 0
SCENE_SHOW_INFO = 7
SCENE_ACTIVITY = 1
SCENE_YES_COMPLETE = 2
SCENE_NO_COMPLETE = 3
SCENE_NEXT_MONSTER = 4
SCENE_GAME_OVER = 5
SCENE_MAILING_LIST = 11


### COMMON FUNCTIONS
# make text fit window size
def display_text_section(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


def display_text(screen, text, color, x, y):
    screen.blit(FONT_QUESTION_TITLE.render(text, True, color), (x, y))


# displays the text centered along the x axis
def display_center_text(screen, text, color, y):
    text = FONT_QUESTION_TITLE.render(text, True, color)
    text_rect = text_rect = text.get_rect(center=(INITIAL_WINDOW_WIDTH/2, y))
    screen.blit(text, text_rect)



# creates a button at (x,y) that's width*height
# button is labeled with text
# upon clicking the button, run onClick
def create_button(screen, event, x, y, width, height, text, onClick, addedWidth=0):
    pygame.draw.rect(screen, BLUE, [x, y, width, height], border_radius=20)
    screen.blit(FONT_TEXT_BUTTON.render(text, True, WHITE), (x + addedWidth, y+height*0.2))
    
    # checking for clicks
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        
        if x <= pos[0] and pos[0] <= x + width:
            if y <= pos[1] and pos[1] <= y + height:
                return onClick()



# draws the BACKGROUND image
def display_background(screen):
    screen.blit(BACKGROUND, (0, 0))



# creates a radio at (x,y) that's width*height
# button is labeled with text above it
# checked = input an array of 10 booleans,
# assumes the input value is an integer
#   which represent the checked status of each of the 10 buttons
def create_radio_button(screen, event, x, y, radius, text, value, checked):
    # checking for clicks
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        
        if x - radius <= pos[0] and pos[0] <= x + radius:
            if y - radius <= pos[1] and pos[1] <= y + radius:
                checked[checked.index(True)] = False
                checked[value] = True
        
    # changing the colour if this button is selected    
    if checked[value]:
        pygame.draw.circle(screen, PURPLE, (x,y), radius)
    else:
        pygame.draw.circle(screen, BLACK, (x,y), radius)
        
    display_text(screen, text, BLACK, x-10, y - radius*2 - 20)
    
    return checked



### SCENES
# no args needed, this is the first scene
def intro_q1(screen, args):                
    fps_cap = 60
    player = "Timmy"
    clock   = pygame.time.Clock()
    
    display_background(screen)
    

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)
            
            answers = question_object.get_answers()
            text = question_object.get_opening_question()
            display_center_text(screen, text, BLACK, 100)

            
            def clickedOption1():
                return SCENE_INTRO_Q2, {}
            def clickedOption2():
                return SCENE_INTRO_Q2, {}
            def clickedOption3():
                return SCENE_INTRO_Q2, {}
            
                
              
            scene_switch = create_button(screen, event, 250, 250, 200, 60, answers[0], clickedOption1, 65)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 500, 250, 200, 60, answers[1], clickedOption2, 75)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 740, 250, 200, 60, answers[2], clickedOption3, 40)
            if scene_switch != None:
                return scene_switch
           


        # Update the game.
        pygame.display.update()



# required args: nothing
def intro_q2(screen, args):
    fps_cap = 60
    player = "Timmy"
    clock   = pygame.time.Clock()
    
    display_background(screen)
    list1 = DropDown([COLOR_INACTIVE, COLOR_ACTIVE],[COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],500, 250, 200, 50, pygame.font.SysFont(None, 30), "Select Problem", ["Depression", "Self-Harm", "Anxiety"])

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        event_list = pygame.event.get()
        
        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.main = list1.options[selected_option]
    
        for event in event_list:
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)

            #answers = question_object.get_answers()
            #text = question_object.get_opening_question()
            text = "Which mental health issue are you facing?"
            display_center_text(screen, text, BLACK, 100)
            
            def submit():
                # return list1.main when actually doing this
                return SCENE_RATE_ISSUE, {"issues": ["anxiety"]}
            state_info = create_button(screen, event, 500, 500, 200, 50, "Submit", submit, 55)
            if state_info != None:
                return state_info

        
        # Update the game.
        list1.draw(screen)

        pygame.display.flip()
        pygame.display.update()



# required args: "issues"
def rate_issue(screen, args):
    # Initialize game variables as the player, enemies and such.
    fps_cap = 60
    clock = pygame.time.Clock()
    
    
    checked = [False]*10
    checked[4] = True
    display_background(screen)

    # Game loop.
    while True:
        
        # Time management.
        clock.tick(fps_cap)
        

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)
            
            # making radio buttons for scale 1-10
            for i in range(10):
                checked = create_radio_button(screen, event, 350 + 60*i, 250, 15, str(i+1), i, checked)
            
            def submit():
                return SCENE_TRAVELLING , {"issues": args.get("issues"), "rating": (checked.index(True) + 1)}
            
            scene_switch = create_button(screen, event, 500, 400, 250, 50, "Submit", submit, 80)
            if scene_switch != None:
                return scene_switch
            
        # draw screen
        display_center_text(screen, f"How do you feel about your {args.get('issues')[0]} at the moment?", BLACK, 50)
        
        
        
        pygame.display.update()



# required args: "issues", "rating"
def travelling(screen, args):
    # Sprite textures
    char_img = pygame.image.load('sources/sprites/character_maleAdventurer_walk0.png')
    mon_img = pygame.image.load('sources/sprites/character_zombie_idle.png')
    char_size = char_img.get_size()
    mon_size = mon_img.get_size()
    char_img = pygame.transform.scale(char_img, (char_size[0] * 2, char_size[1] * 2))
    mon_img = pygame.transform.scale(mon_img, (mon_size[0] * 2, mon_size[1] * 2))
    
    # Initialize game variables as the player, enemies and such.
    fps_cap = 60
    clock = pygame.time.Clock()
    
    
    # Initialise movement event variables
    y = INITIAL_WINDOW_HEIGHT * 0.6
    x_mon_init = INITIAL_WINDOW_WIDTH * 0.7
    x_char_pos = [INITIAL_WINDOW_WIDTH * 0.1]
    
    # Function for animation of character moving to monster
    def movement_scene(x):
        display_background(screen)
        screen.blit(mon_img, (x_mon_init , y))
        if abs(x[-1] - x_mon_init) > 100:
            x.append(x[-1] + 2)
            screen.blit(char_img, (x[-1], y))
            x.remove(x[-2])
        else:
            screen.blit(char_img, (x[-1], y))

    # Game loop.
    while True:
        # Time management.
        clock.tick(fps_cap)
        
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        movement_scene(x_char_pos)
        if abs(x_char_pos[-1] - x_mon_init) <= 100:
            return SCENE_FIGHTING, {"issues": args.get("issues"), "rating": args.get("rating")}
        
        pygame.display.update()




# required args: "issues", "rating"
def fighting(screen, args):
    # Chooses a monster to face based on the list of issues the user is experiencing
    # Input: An array of strings
    # Output: A monster 
    #   returns None if monster not found
    def choose_monster(issues):
        monsters_of_issues = {
            "depression": [Monster("depression", "depression")],
            "anxiety": [Monster("anxiety", "anxiety")],
        }
        
        issue = random.choice(issues)
        monsters = monsters_of_issues.get(issue)
        if monsters == None:
            print("Error: User's issue does not have any monsters listed")
            return None
        else:
            return random.choice(monsters)



    # Initialize game variables as the player, enemies and such.
    fps_cap = 60
    player  = 'Ted'
    clock   = pygame.time.Clock()
    
    # importing images
    char_img = pygame.image.load('sources/sprites/character_maleAdventurer_walk0.png')
    mon_img = pygame.image.load('sources/sprites/character_zombie_idle.png')
    
    # choosing a monster and getting moves to do
    monster = choose_monster(args.get("issues"))
    moves = monster.sorted_self_care_activities()
    
    # displaying background and characters
    display_background(screen)
    DEFAULT_IMAGE_SIZE = (300, 400)
    image_char = pygame.transform.scale(char_img, DEFAULT_IMAGE_SIZE)
    image_mons = pygame.transform.scale(mon_img, DEFAULT_IMAGE_SIZE)
    
    screen.blit(image_char, (200,200))
    screen.blit(image_mons, (700,200))


    # Game loop.
    while True:
        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            
            # displaying optional moves
            def clickedOption1():
                return SCENE_SHOW_INFO, {"activity": moves[0], "issue": monster.issue, "issues": args.get("issues"), "rating": args.get("rating")}
            def clickedOption2():
                return SCENE_SHOW_INFO, {"activity": moves[1], "issue": monster.issue, "issues": args.get("issues"), "rating": args.get("rating")}   
            def clickedOption3():
                return SCENE_SHOW_INFO, {"activity": moves[2], "issue": monster.issue, "issues": args.get("issues"), "rating": args.get("rating")}   
            def clickedOption4():
                return SCENE_SHOW_INFO, {"activity": moves[3], "issue": monster.issue, "issues": args.get("issues"), "rating": args.get("rating")}   
                

            scene_switch = create_button(screen, event, 150, 720, 450, 60, moves[0], clickedOption1, 50)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 150, 620, 450, 60, moves[1], clickedOption2, 50)

            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 700, 620, 450, 60, moves[2], clickedOption3, 50)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 700, 720, 450, 60, moves[3], clickedOption4, 50)

            if scene_switch != None:
                return scene_switch

        display_center_text(screen, f"What move will you use to defeat {monster.name}?", BLACK, 120)
        
        # Draw your game.
        pygame.display.update()



# required args: "issues", "activity", "rating"
def show_info(screen, args):    
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()
    
    display_background(screen)
    
    #dict of lists of info for activities
    #   where the first value in the array is a website url
    info = {
        "do a breathing exercise": [
            "https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/breathing-exercises-for-stress/",
            "https://www.youtube.com/watch?v=JRP3RLm8rYs&t=1s",
            "Take some time to just breathe..."    
        ],
        "listen to relaxing music": [
            "https://www.quora.com/Where-can-I-listen-to-relaxing-music",
            "https://www.youtube.com/watch?v=JRP3RLm8rYs&t=1s",
            "Find something slow and chill"
        ],
        "do yoga": [
            "https://www.nytimes.com/guides/well/beginner-yoga",
            "https://www.youtube.com/watch?v=JRP3RLm8rYs&t=1s",
            "Relaxing and bendy!"
        ],
        "walk for 10 minutes": [
            "https://frodshamfestivalofwalks.uk/15-things-to-do-and-think-about-while-you-are-walking/2021/",
            "https://www.youtube.com/watch?v=JRP3RLm8rYs&t=1s",
            "Go at a slow and stead pace"
        ]
    }

    # Game loop.
    while True:
        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)
            activity = args.get("activity")
            pygame.draw.rect(screen, WHITE, [300, 40, 600, 440], border_radius=20)
            display_center_text(screen, f"Information about: {activity}", BLACK, 80)
            
            #displaying info
            if activity in info:
                infos = info.get(activity)
                def visit_website():
                    webbrowser.open(infos[0])
                create_button(screen, event, 500, 100, 200, 60, "Visit Website", visit_website, 20)
                def visit_youtube():
                    webbrowser.open(infos[1])
                create_button(screen, event, 500, 180, 200, 60, "Watch Video", visit_youtube, 20)
                if len(infos) >= 3:
                    text = "\n".join(infos[2:])
                    display_text_section(screen, text, BLACK, [400, 280, 400, 200], FONT_TEXT_BUTTON)
            
            def cancel():
                return SCENE_FIGHTING, {"issues": args.get("issues"), "rating": args.get("rating")}
            def ok():
                return SCENE_ACTIVITY, {"activity": activity, "issue": args.get("issue"), "rating": args.get("rating")}
                
            scene_switch = create_button(screen, event, 400, 370, 150, 60, "Cancel", cancel, 45)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 650, 370, 150, 60, "Next", ok,35)
            if scene_switch != None:
                return scene_switch

        pygame.display.update()




# required args: "activity", "issue", "rating"
# "activity" is a self care move
# "issue" is whatever the person is dealing with
def activity(screen, args):    
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()
    
    completed_activity = None    

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)
            
            
            def clickedYes():
                return SCENE_YES_COMPLETE, {"activity": args.get("activity"), "issue": args.get("issue"), "rating": args.get("rating")}
            def clickedNo():
                return SCENE_NO_COMPLETE, {"activity": args.get("activity"), "issue": args.get("issue"), "rating": args.get("rating")}
            
            
            display_center_text(screen, f"Have you finished your task: {args.get('activity')}?", BLACK, 80)
            scene_switch = create_button(screen, event, 400, 300, 150, 60, "Yes", clickedYes, 45)
            if scene_switch != None:
                return scene_switch
            scene_switch = create_button(screen, event, 650, 300, 150, 60, "No", clickedNo, 45)
            if scene_switch != None:
                return scene_switch
        
        pygame.display.update()



# required args: "issue", "rating"
# "issue" is the mental health issue the person is currently dealing with
def yes_complete(screen, args):
    # creates a radio at (x,y) that's width*height
    # button is labeled with text above it
    # checked = input an array of 10 booleans,
    # assumes the input value is an integer
    #   which represent the checked status of each of the 10 buttons
    def create_radio_button(event, x, y, radius, text, value, checked):
        # checking for clicks
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            if x - radius <= pos[0] and pos[0] <= x + radius:
                if y - radius <= pos[1] and pos[1] <= y + radius:
                    checked[checked.index(True)] = False
                    checked[value] = True
            
        # changing the colour if this button is selected    
        if checked[value]:
            pygame.draw.circle(screen, PURPLE, (x,y), radius)
        else:
            pygame.draw.circle(screen, BLACK, (x,y), radius)
            
        display_text(screen, text, BLACK, x - 10, y - radius*2 - 20)
        
        return checked
    
    
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()
    
    
    checked = [False]*10
    checked[4] = True
    display_background(screen)

    # Game loop.
    while True:
        
        # Time management.
        clock.tick(fps_cap)
        

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            display_background(screen)
            
            # making radio buttons for scale 1-10
            for i in range(10):
                checked = create_radio_button(event, 350 + 60*i, 250, 15, str(i+1), i, checked)
            
            def submit():
                return SCENE_GAME_OVER, {}
            
                # This is not being implemented in this prototype
                #if length(args.get("issues")) > 0:
                #    return SCENE_NEXT_MONSTER
                #else:
                #    return SCENE_GAME_OVER
            
            scene_switch = create_button(screen, event, 500, 400, 250, 50, "Submit", submit, 80)
            if scene_switch != None:
                return scene_switch
            
        # draw screen
        display_center_text(screen, f"How do you feel about your {args.get('issue')} now?", BLACK, 50)
        display_center_text(screen, f"You previously rated this as a {args.get('rating')}", BLACK, 80)
        
        
        pygame.display.update()



# required args: "activity"
def no_complete(screen, args):
    # creates a width*height text input area at (x,y)
    # returns whether or not it's active and the current text string
    def create_text_input(event, x, y, width, height, active, text):
        # checking for clicks
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if x <= pos[0] and pos[0] <= x + width and y <= pos[1] and pos[1] <= y + height:
                active = True
            else:
                active = False
        # checking for keyboard input
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        
        # displaying text and text box
        pygame.draw.rect(screen, WHITE, [x, y, width, height], border_radius=20)
        display_text_section(screen, text, BLACK, [x+10, y+10, width-20, height-20], FONT_QUESTION_TITLE)   
        
        return active, text
        
                
        
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()
    
    display_background(screen)

    active = True
    text = ""
    
    # Game loop.
    while True:
        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            active, text = create_text_input(event, 380, 100, 400, 200, active, text)
            
            def submit():
                # TODO upload the reason that the user input
                return SCENE_GAME_OVER, {}
            
            scene_switch = create_button(screen, event, 500, 400, 250, 50, "Submit", submit, 80)
            if scene_switch != None:
                return scene_switch


        # Draw the scene
        display_center_text(screen, f"Why did you not {args.get('activity')}?", BLACK, 50)
        pygame.display.update()



def game_over(screen, args):
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()
    
    # display user feedback
    stu1 = User()
    feedback = stu1.generateFeedback()
    feedback = feedback.replace("\n", " ")
    display_background(screen)

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            
            def cont():
                return SCENE_MAILING_LIST, {}
            seq = create_button(screen, event, 525, 400, 150, 50, "Continue", cont)
            if seq != None:
                return seq

        
        # display user feedback
        rect = pygame.Rect(20, 100, 650, 500)
        display_text_section(screen, feedback, BLACK, rect, FONT_QUESTION_TITLE, aa=False, bkg=None)


        pygame.display.update()
        


def mailing_list(screen, args):
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    clock = pygame.time.Clock()

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            display_background(screen)  
        
            def sign_up():
                print("sign up thing here")
            create_button(screen, event, 525, 300, 150, 50, "Sign Up!", sign_up)
        display_center_text(screen, "Do you want to sign up for our mailing list?", BLACK, 100)
        
        

        pygame.display.update()




def main():
    screen = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))
    pygame.display.set_caption("Journey of Self-Care")  # TODO replace this with cool title
    scene = SCENE_INTRO_Q1
    args = {}
    while True:
        if scene == SCENE_INTRO_Q1:
            scene, args = intro_q1(screen, args)
        elif scene == SCENE_INTRO_Q2:
            scene, args = intro_q2(screen, args)
        elif scene == SCENE_RATE_ISSUE:
            scene, args = rate_issue(screen, args)
        elif scene == SCENE_TRAVELLING:
            scene, args = travelling(screen, args)
        elif scene == SCENE_FIGHTING:
            scene, args = fighting(screen, args)
        elif scene == SCENE_SHOW_INFO:
            scene, args = show_info(screen, args)
        elif scene == SCENE_ACTIVITY:
            scene, args = activity(screen, args)
        elif scene == SCENE_YES_COMPLETE:
            scene, args = yes_complete(screen, args)
        elif scene == SCENE_NO_COMPLETE:
            scene, args = no_complete(screen, args)
        # Not being implemented in this prototype
        #elif scene == SCENE_NEXT_MONSTER:
        #    scene, args = next_monster(screen, args)
        elif scene == SCENE_GAME_OVER:
            scene, args = game_over(screen, args)
        elif scene == SCENE_MAILING_LIST:
                scene, args = mailing_list(screen, args)

main()
