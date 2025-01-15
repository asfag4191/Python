from uib_inf100_graphics.simple import canvas, display

# Figure 1
canvas.create_oval(60, 80, 140, 160)   # Head
canvas.create_line(100, 160, 100, 280) # Body
canvas.create_line(50, 180, 150, 180)  # Arms
canvas.create_line(100, 280, 50, 330)  # Left leg
canvas.create_line(100, 280, 150, 330) # Right leg

# Figure 2 
#only need to adjust the x parameters because the horzontal position
canvas.create_oval(230, 80, 310, 160)  # Head 
canvas.create_line(270, 160, 270, 280) # Body
canvas.create_line(220, 180, 320, 180) # Arms
canvas.create_line(270, 280, 220, 330) # Left leg
canvas.create_line(270, 280, 320, 330) # Right leg
display(canvas)



