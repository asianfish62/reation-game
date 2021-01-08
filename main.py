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
    if random == 1:
        return left_columns
    else:
        return right_columns


input.running_time()
input.button_is_pressed(Button.A)

input_window = 2000
time_decay = 50
minimim_time = 500
game_over = False
while True:
    random = random_side()
    turn_on_side(random)
    basic.pause(input_window)
    
    
    #checks for game_over
    if game_over == True:
        break

    #time decay
    if input_window >500:
        input_window -= time_decay
    turn_off_all()
        