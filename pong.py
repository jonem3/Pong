import pygame
import time
import random

pygame.init()

display_width = 900
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

BAT_WIDTH = 25
BAT_HEIGHT = 100
BALL_WIDTH = 10
BALL_HEIGHT = 10

BAT_SPEED = 15
BALL_SPEED = 10

MAIN_FONT = "comicsansms"


game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong 2.0')
clock = pygame.time.Clock()
def quitgame():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))

    smallText = pygame.font.SysFont(MAIN_FONT, 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def render_score(text, left):
    large_text = pygame.font.SysFont(MAIN_FONT, 20)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.left = left
    text_rect.top = 0
    # text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)
def scores(score1, score2):
    player1 = "Player1: "+str(score1)
    player2 = "Player2: " + str(score2)
    render_score(player1, 20)
    render_score(player2, display_width-120)

def ball_direction():
    global ball_direction
    global ball_speed
    #ballxdirection_choice = random.randint(0, 1)

    delta_x = BALL_SPEED if random.randrange(2) == 0 else -BALL_SPEED
    delta_y = random.randint(-5,5)
    if delta_y == 0:
        delta_y+=1
    ball_speed = [delta_x, delta_y]

def paddle (x, y):
    pygame.draw.rect(game_display, white, [x, y, BAT_WIDTH, BAT_HEIGHT])
def balldraw(x, y):
    pygame.draw.rect(game_display, white, [x, y, BALL_WIDTH, BALL_HEIGHT])

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(black)
        largeText = pygame.font.SysFont(MAIN_FONT, 115)
        TextSurf, TextRect = text_objects("PONG 2.0", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(TextSurf, TextRect)
        button("GO!", 100, 600, 200, 100, green, bright_green, game_loop)
        button("Quit", 600, 600, 200, 100, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        largeText = pygame.font.SysFont(MAIN_FONT, 115)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(TextSurf, TextRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        button("Continue", 100, 600, 200, 100, green, bright_green, unpause)
        button("Quit", 600, 600, 200, 100, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

def display_win(player):
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(black)
        largeText = pygame.font.SysFont(MAIN_FONT, 115)
        TextSurf, TextRect = text_objects(player +" WINS", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(TextSurf, TextRect)
        button("Quit", 600, 600, 200, 100, red, bright_red, quitgame)
        button("Restart", 100, 600, 200, 100, green, bright_green, game_loop)
        pygame.display.update()
        clock.tick(15)

def win_screen(player1, player2):
    if  player1 >= 11:
        display_win("Player 1")

    elif  player2 >= 11:
        display_win("Player 2")

    else:
        pass



def game_loop():
    bat_1_x = 50
    bat_1_y = (display_height / 2)
    bat_2_x = display_width - (50 + BAT_WIDTH)
    bat_2_y = (display_height / 2)

    ballx = (display_width / 2) - BALL_WIDTH
    bally = (display_height / 2) + BALL_HEIGHT

    bat_1_y_delta = 0
    bat_2_y_delta = 0

    global ball_direction
    global ball_speed
    global pause
    global BALL_SPEED

    ball_direction()

    player1 = 0
    player2 = 0



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bat_2_y_delta = -BAT_SPEED
                if event.key == pygame.K_DOWN:
                    bat_2_y_delta = BAT_SPEED
                if event.key == pygame.K_w:
                    bat_1_y_delta = -BAT_SPEED
                if event.key == pygame.K_s:
                    bat_1_y_delta = BAT_SPEED
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    bat_2_y_delta = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    bat_1_y_delta = 0

        bat_2_y += bat_2_y_delta
        bat_1_y += bat_1_y_delta

        game_display.fill(black)

        bat1 = paddle(bat_1_x, bat_1_y)
        bat2 = paddle(bat_2_x, bat_2_y)

        ball = balldraw(ballx, bally)
        ballx += ball_speed[0]
        bally += ball_speed[1]

        if bally < 0 and ball_speed[1] < 0:
            ball_speed[1] = -ball_speed[1]

        if bally + BALL_HEIGHT > display_height and ball_speed[1] > 0:
            ball_speed[1] = -ball_speed[1]

        if ballx < bat_1_x + BAT_WIDTH and \
                        ballx > bat_1_x and \
                        bally < bat_1_y + BAT_HEIGHT and \
                                bally + BALL_HEIGHT > bat_1_y :
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = (bally-(bat_1_y+(BAT_HEIGHT/2)))/2

        if ballx+BALL_WIDTH>bat_2_x and \
                                ballx + BALL_WIDTH < bat_2_x+BAT_WIDTH and \
                        bally < bat_2_y + BAT_HEIGHT and \
                                bally + BALL_HEIGHT > bat_2_y:

            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = (bally - (bat_2_y + (BAT_HEIGHT / 2)))/2


        if ballx > display_width:
            player1+= 1
            ballx = (display_width / 2) - BALL_WIDTH
            bally = (display_height / 2) + BALL_HEIGHT

            ball_direction()
        if ballx < 0:
            player2 += 1
            ballx = (display_width / 2) + BALL_WIDTH
            bally = (display_height / 2) + BALL_HEIGHT



            ball_direction()

        scores(player1, player2)

        pygame.draw.line(game_display, white, [(display_width/2)-2, display_height], [(display_width / 2)-2, 0], 5)

        win_screen(player1, player2)

        pygame.display.update()
        clock.tick(30)
        #Uncomment line below for increasing difficulty per frame
        #BALL_SPEED += 0.01
game_intro()
game_loop()