from math import sqrt
from uib_inf100_graphics.simple import canvas, display
import random

def draw_dots(canvas, num_dots):
    """Tegner prikker og teller hvor mange som treffer sirkelen."""
    center_x, center_y = 200, 200  # Sirkelsentrum
    radius = 200  # Radius på sirkelen
    
    count = 0  # Teller hvor mange punkter som er innenfor sirkelen
    for _ in range(num_dots):  
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        
        # Beregn avstand fra senteret (200, 200) til punktet (x, y)
        d = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        
        if d <= radius:
            color = 'orange'  # Punktet er innenfor sirkelen
            count += 1
        else:
            color = 'grey'  # Punktet er utenfor sirkelen

        canvas.create_oval(x-5, y-5, x+5, y+5, fill=color)

    # Tegn en tekstboks som viser hvor mange prikker som traff sirkelen
    message = f'{count}/{num_dots} prikker traff sirkelen'
    canvas.create_rectangle(100, 180, 300, 220, fill='white')
    canvas.create_text(200, 200, text=message, fill='blue')

# Tegn en stor sirkel med sentrum i (200, 200) og radius 200
canvas.create_oval(0, 0, 400, 400, outline='black', width=2)

# Tegn 1000 tilfeldige prikker, med farge basert på om de er i sirkelen eller ikke
draw_dots(canvas, 1000)


# Vis resultat
display(canvas)

