"""
this is a game where you have to 
"""
from microbit import *

row_num = [0,1,2,3,4]
left_columns = [0,1]
right_columns = [3,4]
score = 0
side_on = ""
#turns on far 2 columns based on 1st parameter 
#input left_parameter for left, right_parameter for right
def turn_on_side(side):
    for column in side: 
        for row in row_num:
            led.plot(column,row)
            
    if side == left_columns:
        side_on = "left"
    else:
        side_on = "right"

#turns off all lights
def turn_off_all():
    for row in row_num:
        for column in row_num: 
            led.unplot(row, column)

#picks either the list left_columns or right_columns randomly
def random_side():
    random = randint(0, 1)
    return random



input_window = 2000
time_decay = 50
minimim_time = 500
game_over = False
button_pressed = 69
score = 0
round_time = 0

#badd while loop
while True:
    random = random_side()
    if random == 1:
        turn_on_side(left_columns)
    else:
        turn_on_side(right_columns)
    button_pressed = 96
    round_time = input.running_time() + input_window

    #checks for input or if input window passed
    if random == 1:
        while random == 1:
            if input.button_is_pressed(Button.A):
                game_over = False
                random = -1
                
            elif input.button_is_pressed(Button.B):
                game_over = True
                random = -1
            elif input.running_time() >= round_time:
                game_over = True
                random = -1
    elif random == 0:
        while random == 0:
            if input.button_is_pressed(Button.A):
                game_over = True
                random = -1
            elif input.button_is_pressed(Button.B):
                game_over = False
                random = -1
            elif input.running_time() >= round_time:
                game_over = True
                random = -1
    #score
    score += 1

    #time decay
    if input_window > 500:
        input_window -= time_decay
    turn_off_all()
                
"""
    #checks for game_over
    if game_over:
        turn_off_all() 
        basic.show_number(score)


#displays score
basic.show_number(score)
"""