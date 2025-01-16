from snake_view import draw_board
import random

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.direction='east'
    app.info_mode=True
    app.snake_size=3
    app.head_pos=(3,4)
    app.state='active'
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
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if not app.info_mode and app.state=='active':
        move_snake(app)

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    if event.key=='i':
        app.info_mode=not app.info_mode
    
    if app.state=='active':
        if event.key=='Up':
            app.direction='north'
        elif event.key=='Down':
            app.direction='south'
        elif event.key=='Left':
            app.direction='west'
        elif event.key=='Right':
            app.direction='east'
        elif event.key=='Space':
            move_snake(app)


def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    if app.info_mode:
        canvas.create_text(
        app.width // 2, 10,  #midten, altså deler bredden på 2
        text=f'{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}', 
        font='Arial 14', 
        fill='black', 
    )
        
    if app.state=='active':
        draw_board(canvas,25,25,app.width-25,app.height-25,app.board,app.info_mode)
    if app.state=="gameover":
        canvas.create_text(app.width / 2, app.height / 2, text="Game Over", font=("Helvetica", 24), fill="red")
    
def move_snake(app):
    app.head_pos=get_next_head_position(app.head_pos, app.direction)
    new_row, new_col=app.head_pos

    if not is_legal_move(app.head_pos, app.board):
        app.state="gameover"
        return 


    if app.board [new_row][new_col]== -1:
        app.snake_size +=1
        
        app.board [new_row][new_col] = app.snake_size
        
        row, col =app.head_pos
        app.board [row][col]=0
        
        add_apple_at_random_location(app.board)

    else:
        subtract_one_from_all_positives(app.board)
    
    app.board[new_row][new_col] = app.snake_size


def get_next_head_position(head_pos, direction):
    row, col = head_pos  # Nåværende posisjon (rad, kolonne)
    
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
