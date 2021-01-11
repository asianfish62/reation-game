let random: number;
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
function random_side(): number {
    let random = randint(0, 1)
    return random
}

let input_window = 2000
let time_decay = 50
let minimim_time = 500
let game_over = false
let button_pressed = 69
score = 0
let round_start_time = 0
input.onButtonPressed(Button.A, function a_pressed() {
    let button_pressed = 0
})
input.onButtonPressed(Button.B, function b_pressed() {
    let button_pressed = 1
})
while (true) {
    random = random_side()
    if (random == 1) {
        turn_on_side(left_columns)
    } else {
        turn_on_side(right_columns)
    }
    
    button_pressed = 96
    round_start_time = input.runningTime()
    // checks for input or if input window passed
    while (true) {
        if (button_pressed == random) {
            game_over = false
            break
        } else if (button_pressed != random) {
            game_over = true
            break
        } else if (round_start_time + input_window >= input.runningTime()) {
            game_over = true
            break
        }
        
    }
    // checks for game_over
    if (game_over) {
        turn_off_all()
        break
    }
    
    // score
    score += 1
    // time decay
    if (input_window > 500) {
        input_window -= time_decay
    }
    
    turn_off_all()
}
// displays score
basic.showNumber(score)
