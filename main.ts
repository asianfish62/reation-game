/** this is a game where you have to */
let row_num = [0, 1, 2, 3, 4]
let left_columns = [0, 1]
let right_columns = [3, 4]
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

function turn_off_all() {
    for (let row of row_num) {
        for (let column of row_num) {
            led.unplot(row, column)
        }
    }
}

turn_on_side(left_columns)
basic.pause(1000)
turn_off_all()
let input_window = 2000
let time_decay = 50
let minimim_time = 500
while (true) {
    input.buttonIsPressed(Button.A)
}
