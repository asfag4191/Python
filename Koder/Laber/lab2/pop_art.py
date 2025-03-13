from uib_inf100_graphics.simple import canvas, display

#inspirasjon fra marilyn.py
def pop_art(canvas, x, y, background_color, detail_color):

    # Background
    canvas.create_rectangle(x, y, x+100, y+100, fill=background_color)

    # House
    canvas.create_rectangle(x+20, y+30, x+80, y+90, fill=detail_color, outline="")

    # Windows
    canvas.create_rectangle(x+30, y+40, x+45, y+55, fill="white", outline="")
    canvas.create_rectangle(x+55, y+40, x+70, y+55, fill="white", outline="")

    # Door (placed at the bottom)
    canvas.create_rectangle(x+45, y+70, x+55, y+90, fill="brown", outline="")

    # Roof (triangle)
    canvas.create_polygon(x+20, y+30, x+50, y+10, x+80, y+30, fill="darkred", outline="")


# Drawing four houuses
pop_art(canvas, 50, 50, background_color='red', detail_color='yellow')
pop_art(canvas, 250, 50, background_color='blue', detail_color='pink')
pop_art(canvas, 50, 250, background_color='green', detail_color='purple')
pop_art(canvas, 250, 250, background_color='light blue', detail_color='orange')

display(canvas)
