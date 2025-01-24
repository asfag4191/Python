#tegner et kvadrat for hver farge
def draw_belgian_flag(canvas, x1, y1, x2, y2):
    # Beregn bredden på hvert felt
    #siden x2 er nederste hjørenet lengst borte, og x1 er øverste. 
    width = (x2 - x1) / 3

    #det svarte og gule feltet må skrives fra det første punktet. start: svart:/x1,y1 slutt: x1+width,y2
    #
    # Tegn det svarte feltet
    canvas.create_rectangle(x1, y1, x1 + width, y2, fill="black", outline="black")
    
    #start:x1+width,y1 slutt: x1+2*width
    # Tegn det gule feltet
    canvas.create_rectangle(x1 + width, y1, x1 + 2 * width, y2, fill="yellow", outline="yellow")
    
    #det røde feltet slutter på gitt sluttpunkt
    # Tegn det røde feltet
    canvas.create_rectangle(x1 + 2 * width, y1, x2, y2, fill="red", outline="red")

# belgian_flag_test.py
from uib_inf100_graphics.simple import canvas, display
from belgian_flag import draw_belgian_flag

draw_belgian_flag(canvas, 125, 135, 275, 265)
draw_belgian_flag(canvas, 10, 10, 40, 36)
draw_belgian_flag(canvas, 10, 340, 390, 360)

display(canvas)