from uib_inf100_graphics.simple import canvas, display

# Figure 1
canvas.create_oval(60, 80, 140, 160)   
canvas.create_line(100, 160, 100, 280) 
canvas.create_line(50, 180, 150, 180)  
canvas.create_line(100, 280, 50, 330)  
canvas.create_line(100, 280, 150, 330) 

# Figure 2 
#justerer kun x siden det er horisontale linjen
canvas.create_oval(230, 80, 310, 160)  
canvas.create_line(270, 160, 270, 280) 
canvas.create_line(220, 180, 320, 180) 
canvas.create_line(270, 280, 220, 330) 
canvas.create_line(270, 280, 320, 330)
display(canvas)



