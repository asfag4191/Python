from uib_inf100_graphics.simple import canvas, display

# Fjes (hode)
canvas.create_oval(50, 50, 360, 360, fill='beige')

# Øyne
# Venstre øye
canvas.create_oval(120, 120, 180, 180, fill='white')  
# Høyre øye
canvas.create_oval(230, 120, 290, 180, fill='white')  

# Pupiller
canvas.create_oval(145, 145, 155, 155, fill='black')  
canvas.create_oval(255, 145, 265, 155, fill='black') 

# Nese
canvas.create_polygon(190, 190, 210, 190, 200, 220, fill='pink', outline='black')

# Munn
canvas.create_arc(140, 220, 280, 300, start=0, extent=-180, fill='', outline='purple', width=2)

# Vis canvas
display(canvas)