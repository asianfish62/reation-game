let random: number[];
/** this is a game where you have to */
let row_num = [0, 1, 2, 3, 4]
let left_columns = [0, 1]
let right_columns = [3, 4]
let score = 0
let side_on = ""
// turns on far 2 columns based on 1st parameter 
// input left_parameter for left, right_parameter for right
function turn_on_side(side: number[]) {
    let side_on: string;
    for (let column of side) {
        for (let row of row_num) {
            led.plot(column, row)
        }
    }
    if (side == left_columns) {
        side_on = "left"
    } else {
        side_on = "right"
    }
    
}

// turns off all lights
function turn_off_all() {
    for (let row of row_num) {
        for (let column of row_num) {
            led.unplot(row, column)
        }
    }
}

// picks either the list left_columns or right_columns randomly
function random_side(): number[] {
    let random = randint(0, 1)
    if (random == 1) {
        return left_columns
    } else {
        return right_columns
    }
    
}

input.runningTime()
input.buttonIsPressed(Button.A)
let input_window = 2000
let time_decay = 50
let minimim_time = 500
let game_over = false
while (true) {
    random = random_side()
    turn_on_side(random)
    basic.pause(input_window)
    // checks for game_over
    if (game_over == true) {
        break
    }
    
    // time decay
    if (input_window > 500) {
        input_window -= time_decay
    }
    
    turn_off_all()
}
