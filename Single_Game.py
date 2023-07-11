import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# functions
def text(font_size, hieght, wieth, txt):
    font = pygame.font.Font(None, font_size)
    text = font.render(txt, True, BLACK)
    global text_rect
    text_rect = text.get_rect()
    text_rect.center = (wieth, hieght)
    screen.blit(text, text_rect)

    return text_rect

def chance(C):
    if C % 2 == 0:
        screen.blit(background_image_2, (280, 235))
    
    if C % 2 == 1:
        screen.blit(background_image_1, (260, 220))

# Creating a computer turn
def Computer_turn():
    available_circles = []
    for o in range(len(circles)):
        if not status[o]:
            available_circles.append(circles[o])
    if available_circles:
        c_choice = random.choice(available_circles)
        for o in range(len(circles)):
            if c_choice == circles[o]:
                return o
    return -1

        
def checker(status, nobat, R, B):
    global red_emtiaz, blue_emtiaz
    
    if (status[0] == status[1] == status[2] == 1) and (nobat[0] == False):
        red_emtiaz += 1
        nobat[0] = True
        return "b"
    if (status[0] == status[1] == status[2] == 2) and (nobat[0] == False) :
        blue_emtiaz += 1
        nobat[0] = True
        return "r"

    if (status[0] == status[3] == status[6] == 1) and (nobat[1] == False) :
        red_emtiaz += 1
        nobat[1] = True
        return "b"
    if (status[0] == status[3] == status[6] == 2) and (nobat[1] == False) :
        blue_emtiaz += 1
        nobat[1] = True
        return "r"

    if (status[0] == status[9] == status[21] == 1) and (nobat[2] == False):
        red_emtiaz += 1
        nobat[2] = True
        return "b"
    if (status[0] == status[9] == status[21] == 2) and (nobat[2] == False):
        blue_emtiaz += 1
        nobat[2] = True
        return "r"

    if (status[3] == status[4] == status[5] == 1) and (nobat[3] == False):
        red_emtiaz += 1
        nobat[3] = True
        return "b"
    if (status[3] == status[4] == status[5] == 2) and (nobat[3] == False):
        blue_emtiaz += 1
        nobat[3] = True
        return "r"

    if (status[3] == status[10] == status[18] == 1) and (nobat[4] == False):
        red_emtiaz += 1
        nobat[4] = True
        return "b"
    if (status[3] == status[10] == status[18] == 2) and (nobat[4] == False):
        blue_emtiaz += 1
        nobat[4] = True
        return "r"

    if (status[6] == status[7] == status[8] == 1) and (nobat[5] == False):
        red_emtiaz += 1
        nobat[5] = True
        return "b"
    if (status[6] == status[7] == status[8] == 2) and (nobat[5] == False):
        blue_emtiaz += 1
        nobat[5] = True
        return "r"
    
    if (status[6] == status[11] == status[15] == 1) and (nobat[6] == False):
        red_emtiaz += 1
        nobat[6] = True
        return "b"
    if (status[6] == status[11] == status[15] == 2) and (nobat[6] == False):
        blue_emtiaz += 1
        nobat[6] = True
        return "r"

    if (status[15] == status[16] == status[17] == 1) and (nobat[7] == False):
        red_emtiaz += 1
        nobat[7] = True
        return "b"
    if (status[15] == status[16] == status[17] == 2) and (nobat[7] == False):
        blue_emtiaz += 1
        nobat[7] = True
        return "r"

    if (status[8] == status[12] == status[17] == 1) and (nobat[8] == False):
        red_emtiaz += 1
        nobat[8] = True
        return "b"
    if (status[8] == status[12] == status[17] == 2) and (nobat[8] == False):
        blue_emtiaz += 1
        nobat[8] = True
        return "r"

    if (status[5] == status[13] == status[20] == 1) and (nobat[9] == False):
        red_emtiaz += 1
        nobat[9] = True
        return "b"
    if (status[5] == status[13] == status[20] == 2) and (nobat[9] == False):
        blue_emtiaz += 1
        nobat[9] = True
        return "r"

    if (status[2] == status[14] == status[23] == 1) and (nobat[10] == False):
        red_emtiaz += 1
        nobat[10] = True
        return "b"
    if (status[2] == status[14] == status[23] == 2) and (nobat[10] == False):
        blue_emtiaz += 1
        nobat[10] = True
        return "r"

    if (status[18] == status[19] == status[20] == 1) and (nobat[11] == False):
        red_emtiaz += 1
        nobat[11] = True
        return "b"
    if (status[18] == status[19] == status[20] == 2) and (nobat[11] == False):
        blue_emtiaz += 1
        nobat[11] = True
        return "r"

    if (status[21] == status[22] == status[23] == 1) and (nobat[12] == False):
        red_emtiaz += 1
        nobat[12] = True
        return "b"
    if (status[21] == status[22] == status[23] == 2) and (nobat[12] == False):
        blue_emtiaz += 1
        nobat[12] = True
        return "r"

    if (status[1] == status[4] == status[7] == 1) and (nobat[13] == False):
        red_emtiaz += 1
        nobat[13] = True
        return "b"
    if (status[1] == status[4] == status[7] == 2) and (nobat[13] == False):
        blue_emtiaz += 1
        nobat[13] = True
        return "r"

    if (status[2] == status[5] == status[8] == 1) and (nobat[14] == False):
        red_emtiaz += 1
        nobat[14] = True
        return "b"
    if (status[2] == status[5] == status[8] == 2) and (nobat[14] == False):
        blue_emtiaz += 1
        nobat[14] = True
        return "r"

    if (status[9] == status[10] == status[11] == 1) and (nobat[15] == False):
        red_emtiaz += 1
        nobat[15] = True
        return "b"
    if (status[9] == status[10] == status[11] == 2) and (nobat[15] == False):
        blue_emtiaz += 1
        nobat[15] = True
        return "r"

    if (status[15] == status[18] == status[21] == 1) and (nobat[16] == False):
        red_emtiaz += 1
        nobat[16] = True
        return "b"
    if (status[15] == status[18] == status[21] == 2) and (nobat[16] == False):
        blue_emtiaz += 1
        nobat[16] = True
        return "r"

    if (status[16] == status[19] == status[22] == 1) and (nobat[17] == False):
        red_emtiaz += 1
        nobat[17] = True
        return "b"
    if (status[16] == status[19] == status[22] == 2) and (nobat[17] == False):
        blue_emtiaz += 1
        nobat[17] = True
        return "r"

    if (status[17] == status[20] == status[23] == 1) and (nobat[18] == False):
        red_emtiaz += 1
        nobat[18] = True
        return "b"
    if (status[17] == status[20] == status[23] == 2) and (nobat[18] == False):
        blue_emtiaz += 1
        nobat[18] = True
        return "r"

    if (status[12] == status[13] == status[14] == 1) and (nobat[19] == False):
        nobat[19] = True
        return "b"
    if (status[12] == status[13] == status[14] == 2) and (nobat[19] == False):
        blue_emtiaz += 1
        nobat[19] = True
        return "r"

# Set screen dimensions
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 650

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball number
RED_BALL = 12
BLUE_BALL = 12

# Emtiaz 
red_emtiaz = 0
blue_emtiaz = 0

# Variable chance
CHANCE = 1

# Load images
background_image_1 = pygame.image.load("C:\\Users\\esmai\\OneDrive\\Desktop\doz\\Iranian_doz_game\\b1.png")
background_image_2 = pygame.image.load("C:\\Users\\esmai\\OneDrive\\Desktop\doz\\Iranian_doz_game\\b2.png")
main_background_image = pygame.image.load("C:\\Users\\esmai\\OneDrive\\Desktop\doz\\Iranian_doz_game\\p.png")
logo = pygame.image.load("C:\\Users\\esmai\\OneDrive\\Desktop\doz\\Iranian_doz_game\\logo.jpg")

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the screen
pygame.display.set_caption("Simple Game")

# Actrion ball
# code

# Display the background images
screen.blit(main_background_image, (0, 0))
screen.blit(background_image_1, (790, 200))
screen.blit(background_image_2, (810, 400))
screen.blit(logo, (750, 20))

b = text(38, 360, 880, f" X {BLUE_BALL}")
r = text(38, 550, 880, f" X {RED_BALL}")

e_b = text(45, 285, 885, f"{blue_emtiaz}")
e_r = text(45, 470, 885, f"{red_emtiaz}")


# Action Circle
circles = [
    pygame.draw.circle(screen,  (255, 0, 0), (60, 35), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (353, 33), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (660, 33), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (173, 139), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (353, 136), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (531, 138), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (263, 223), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (353, 218), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (438, 218), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (58, 311), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (170, 311), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (262, 311), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (438, 310), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (531, 310), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (658, 308), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (263, 399), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (352, 401), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (438, 399), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (172, 485), 16, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (353, 488), 17, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (532, 483), 15, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (59, 594), 14, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (350, 594), 16, 1),
    pygame.draw.circle(screen,  (255, 0, 0), (658, 594), 16, 1),
]
status = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
colors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nobat = [False] * len(circles)

# Game loop
while True:
    chance(CHANCE)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif CHANCE % 2 == 0 and RED_BALL > 0:
            c_n = Computer_turn()
            pygame.draw.circle(screen, (255, 0, 0), circles[c_n].center, 14)
            RED_BALL -= 1
            screen.fill(WHITE, r)
            text(38, 550, 880, f" X {RED_BALL}")
            status[c_n] = True
            colors[c_n] = 1
            check = checker(colors, nobat, RED_BALL, BLUE_BALL)
            screen.fill((228,32,32), e_r)
            text(45, 470, 885, f"{red_emtiaz}")

            if check == "b":
                BLUE_BALL -= 1
                screen.fill(WHITE, b)
                text(38, 360, 880, f" X {BLUE_BALL}")
                screen.fill((228,32,32), e_r)
                text(45, 470, 885, f"{red_emtiaz}")

                CHANCE += 2
            else:
                CHANCE += 1
            

        elif event.type == pygame.MOUSEBUTTONDOWN and BLUE_BALL > 0:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            for i, v in enumerate(circles):
               if v.collidepoint(mouse_pos) and status[i] == False:
                    # Check if the mouse clicked on the red ball
                    pygame.draw.circle(screen, (0, 0, 255), v.center, 14)
                    BLUE_BALL -= 1
                    screen.fill(WHITE, b)
                    text(38, 360, 880, f" X {BLUE_BALL}")
                    status[i] = True
                    colors[i] = 2
                    check = checker(colors, nobat, RED_BALL, BLUE_BALL)
                    screen.fill((81,57,202), e_b)
                    text(45, 285, 885, f"{blue_emtiaz}")
                    if check == "r":
                        RED_BALL -= 1
                        screen.fill(WHITE, r)
                        text(38, 550, 880, f" X {RED_BALL}")
                        screen.fill((81,57,202), e_b)
                        text(45, 285, 885, f"{blue_emtiaz}")
                        CHANCE += 2

                    else:
                        CHANCE += 1


    pygame.display.update()
    
