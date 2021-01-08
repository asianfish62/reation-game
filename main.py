"""
this is a game where you have to 
"""
row_num = [0,1,2,3,4]
left_columns = [0,1]
right_columns = [3,4]
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
        
def turn_off_all():
    for row in row_num:
        for column in row_num: 
            led.unplot(row, column)

turn_on_side(left_columns)
basic.pause(1000)
turn_off_all()

input_window = 2000
time_decay = 50
minimim_time = 500
while True:
    input.button_is_pressed(Button.A)
