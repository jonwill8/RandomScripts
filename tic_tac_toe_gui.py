# importing the nessacary modules

import pygame
from pygame.locals import *

# initializing pygame
pygame.init()

# creating screen & giving it name
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height,))
pygame.display.set_caption('Tic Tac Toe Game')


# drawing grid of tic tac toe board
def draw_grid():
    rbg = (112, 51, 173)
    screen.fill(rbg)
    grid_color = (0, 0, 0)
    line_width = 6
    for x in range(1, 3):
        # drawing horzontial lines on screen (screen_var,RGB color tuple,(start pos),(end pos))
        pygame.draw.line(screen, grid_color, (0, x * 100), (screen_width, x * 100), line_width)
        # drawing vertical lines on screen
        pygame.draw.line(screen, grid_color, (x * 100, 0), (x * 100, screen_height), line_width)


# defining some global variables which will be used in game
clicked = False
pos = []
player = 1
markers = []
green = (0, 255, 0)  # X color
red = (255, 0, 0)  # Y color
blue = (170, 206, 226)
pink = (255, 89, 143)
orange = (243, 135, 47)
font = pygame.font.SysFont(None, 40)
winner = None
game_over = False
# creating play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2 + 4, 160, 50)

# filling our markers lis:
for x in range(3):
    row = [0] * 3
    markers.append((row))


def draw_markers():
    x_pos = 0
    line_width = 6
    for row in markers:
        y_pos = 0
        for cell in row:  # iterating over every cell
            if cell == 1:  # player 1 has clicked
                # draw green x
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if cell == -1:
                # draw red circle
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1  # incrementng our y position so that it will draw in the correct box
        x_pos += 1  # incrementing our x position so that it will draw in the correct box


def check_winner():
    global winner
    global game_over
    # checking rows for winner
    for row in markers:
        if sum(row) == 3:
            winner = 1
            game_over = True
        elif sum(row) == -3:
            winner = 2
            game_over = True
    # checking cols for winner
    for i in range(3):
        col = [markers[row][i] for row in range(3)]
        if sum(col) == 3:
            winner = 1
            game_over = True
        elif sum(col) == -3:
            winner = 2
            game_over = True
    # checking diag slice one (top left ---> bottom right) for winners
    diag_slice_one = [markers[i][i] for i in range(3)]
    if sum(diag_slice_one) == 3:
        winner = 1
        game_over = True
    elif sum(diag_slice_one) == -3:
        winner = 2
        game_over = True
    # checking diag slice two (bottom left --> top right) for winners
    ind_sum = len(markers) - 1  # =2 on a 3x3 board
    diag_slice_two = [markers[ind_sum - i][i] for i in range(3)]
    if sum(diag_slice_two) == 3:
        winner = 1
        game_over = True
    elif sum(diag_slice_two) == -3:
        winner = 2
        game_over = True


def draw_winner(tied_cond):
    if tied_cond == True:
        win_prompt = 'Nobody won!'
    else:
        # making our win text
        win_prompt = f"Player {winner} wins!"

    # converting our win text to an image to be displayed
    win_img = font.render(win_prompt, True, blue)
    pygame.draw.rect(screen, pink, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 48))
    # printing our win prompt
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
    # play again functionality
    again_txt = 'Play Again?'
    again_img = font.render(again_txt, True, blue)
    pygame.draw.rect(screen, pink, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


def check_tie():
    tied = True
    for row in markers:
        for num in row:
            if num == 0:  # game is not tied, empty spot in grid
                tied = False
                return tied
    return tied


# game loop
running = True
while running:
    draw_grid()
    draw_markers()
    # adding event handlers to run our game
    for event in pygame.event.get():
        # adding event for clicking on exit button
        if event.type == pygame.QUIT:
            running = False
        if game_over == False and check_tie() == False:  # keep reading input while game is not over and not tied
            # adding event for clicking on the board
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:  # we have completed a click cycle
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:  # if board not filled at this position
                    markers[cell_x // 100][cell_y // 100] = player  # assign board to either player 1/-1
                    player *= -1  # this flips between player 1/2 (1/-1)
                    check_winner()

    if game_over == True or check_tie() == True:
        draw_winner(check_tie())
        # check for mouseclick to see id use clicked play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            # resetting the game
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                player = 1
                markers = []
                pos = []
                game_over = False
                winner = 0
                # resetting markers
                for x in range(3):
                    row = [0] * 3
                    markers.append((row))
            else:
                pygame.quit()

    # this method is called at the end of every iteration of our for loop so that
    # anything that occurs on the screen is updated to the screen widow
    pygame.display.update()

pygame.quit()  # quitting pygame after kicking out of loop
