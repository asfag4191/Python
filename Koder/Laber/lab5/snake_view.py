def draw_board(canvas, x1,y1,x2,y2,board,info_mode):
    rows=len(board) #antall rader
    cols=len(board[0]) #antall kolonner basert på første raden

    total_width= x2-x1
    cell_width=total_width/cols

    total_height= y2-y1
    cell_height=total_height/rows

    
    #Hver celle (row,column) tegnes en etter en. 
    for row in range(rows): #håndterer rader
        for col in range (cols): #håndterer kolonner
            #Tegn en celle
            #venstre og høyre kant
            #col er hvilken kolonne man befinner oss i
            x_left=x1+col*cell_width
            x_right=x_left+cell_width
            #Topp og bunn
            y_top=y1+row*cell_height
            y_bottom=y_top+cell_height

            value=board[row][col]
            color = get_color(value)

            canvas.create_rectangle(x_left, y_top, x_right, y_bottom, fill=color)

            if info_mode:
                text = f'{row}, {col}\n {board [row][col]}'
                cell_mid_x=(x_left+x_right) /2
                cell_mid_y=(y_top+y_bottom) /2
                canvas.create_text(cell_mid_x, cell_mid_y, text=text)


#fargene bestemmes på fargene i brettet
def get_color(value): 
    if value==0:
        return 'lightgray'
    if value>0:
        return 'orange'
    if value <0:
        return 'cyan'
    

if __name__ == '__main__':
    from uib_inf100_graphics.simple import canvas, display

    test_board = [
        [1, 2, 3, 0, 5, 4,-1,-1, 1, 2, 3],
        [0, 4, 0, 7, 0, 3,-1, 0, 0, 4, 0],
        [0, 5, 0, 8, 1, 2,-1,-1, 0, 5, 0],
        [0, 6, 0, 9, 0, 0, 0,-1, 0, 6, 0],
        [0, 7, 0,10,11,12,-1,-1, 0, 7, 0],
    ]

    draw_board(canvas, 25, 80, 375, 320, test_board, True)
    display(canvas)