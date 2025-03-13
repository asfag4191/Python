from snake_view import draw_board 
import random 

def app_started(app):
    app.state='start'
    app.direction='east'
    app.info_mode=True
    app.snake_size=3
    app.head_pos=(3,4)
    app.timer_delay = 200
    app.board=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def timer_fired(app):
    if app.state == 'active':
        if not app.info_mode:
            move_snake(app)

def key_pressed(app, event):
    if app.state == 'start':
        if event.key.lower() == 'p':
            app.state = 'active'
        return 

    if event.key == 'i':
        app.info_mode = not app.info_mode
    elif event.key == 'Space':
        move_snake(app)
    
    if app.state=='active':
        if event.key=='Up':
            app.direction='north'
        elif event.key=='Down':
            app.direction='south'
        elif event.key=='Left':
            app.direction='west'
        elif event.key=='Right':
            app.direction='east'

def redraw_all(app, canvas):
    if app.state == 'start':
        canvas.create_text(
            app.width / 2, app.height / 2 - 50,
            text="Snake",
            font="Arial 36",
            fill="black"
        )
        canvas.create_text(
            app.width / 2, app.height / 2,
            text="Press 'P' to Play,'i' to turn of info modus.",
            font="Arial 24",
            fill="black"
        )
        canvas.create_text(
            app.width / 2, app.height / 2 + 50,
            text="Control the hungry snake and catch apples.",
            font="Arial 16",
            fill="gray"
        )

        canvas.create_text(
            app.width / 2, app.height / 2 + 70,
            text="Use arrow keys to change direction.",
            font="Arial 16",
            fill="gray"
        )

        canvas.create_text(
            app.width / 2, app.height / 2 + 90,
            text="If you press space when active, you can move faster!",
            font="Arial 16",
            fill="gray"
        )

    elif app.state == 'active':
        draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.info_mode)
        if app.info_mode:
            canvas.create_text(
                app.width // 2, 10,
                text=f'{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}',
                font='Arial 14',
                fill='black'
            )
    elif app.state == "gameover":
        canvas.create_text(
            app.width / 2, app.height / 2,
            text="Game Over",
            font=("Helvetica", 24),
            fill="red"
        )
    
def move_snake(app):
    app.head_pos=get_next_head_position(app.head_pos, app.direction)
    new_row, new_col=app.head_pos

    if not is_legal_move(app.head_pos, app.board):
        app.state="gameover"
        return


    if app.board [new_row][new_col]== -1:
        app.snake_size +=1
        app.board [new_row][new_col] = app.snake_size
        add_apple_at_random_location(app.board)

    else:
        subtract_one_from_all_positives(app.board)
    
    app.board[new_row][new_col] = app.snake_size


def get_next_head_position(head_pos, direction):
    row, col = head_pos  
    
    if direction == 'east':
        new_row, new_col= row, col + 1
    elif direction == 'west':
        new_row, new_col=row, col - 1
    elif direction == 'north':
        new_row, new_col=row - 1, col
    elif direction == 'south':
        new_row, new_col=row + 1, col
    
    return new_row, new_col
    
def subtract_one_from_all_positives(grid):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] > 0:
                grid[row][column] -= 1

                
def add_apple_at_random_location(grid):
    empty_positions=[]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                empty_positions.append((row, col))
    
    if empty_positions:
        row,col=random.choice(empty_positions)
        grid[row][col]=-1

def is_legal_move(pos, board):
    row,col=pos
    if (0 <= row < len(board)) and (0 <= col < len(board[0])):
        if board[row][col] == 0 or board[row][col] == -1:
            return True
    return False 


if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=400, title='Snake')
