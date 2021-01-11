"""
this is a game where you have to 
"""
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
round_start_time = 0

input.on_button_pressed(Button.A, a_pressed)
def a_pressed():
    button_pressed = 0
input.on_button_pressed(Button.B, b_pressed)
def b_pressed():
    button_pressed = 1

while True:
    random = random_side()
    if random == 1:
        turn_on_side(left_columns)
    else:
        turn_on_side(right_columns)
    button_pressed = 96
    round_start_time = input.running_time()

    #checks for input or if input window passed
    while True:
        if button_pressed == random:
            game_over = False
            break
        elif button_pressed != random: 
            game_over = True
            break
        elif (round_start_time + input_window) >= input.running_time():
            game_over = True
            break
        
    
    
    #checks for game_over
    if game_over:
        turn_off_all()
        
        break

    #score
    score += 1

    #time decay
    if input_window >500:
        input_window -= time_decay
    turn_off_all()
    

#displays score
basic.show_number(score)