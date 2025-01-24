from uib_inf100_graphics.simple import canvas, display

#beholder den forrige stickmanen, og endrer på den med å legge til ny x og y verdi for at propisjonen skal bli riktig. 
def draw_stickmen(canvas,x,y):
    canvas.create_oval(60 + x, 80 + y, 140 + x, 160 + y)   # Head
    canvas.create_line(100 + x, 160 + y, 100 + x, 280 + y) # Body
    canvas.create_line(50 + x, 180 + y, 150 + x, 180 + y)  # Arms
    canvas.create_line(100 + x, 280 + y, 50 + x, 330 + y)  # Left leg
    canvas.create_line(100 + x, 280 + y, 150 + x, 330 + y) # Right leg

draw_stickmen(canvas, 100, 100)  # First stickman, moved by (50, 50)
draw_stickmen(canvas, 200, 50) # Second stickman, moved by (200, 50)

display(canvas)
