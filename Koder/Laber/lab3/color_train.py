def color_train_A(canvas, x, y, colors):
    for i in range(0,len(colors)):
        canvas.create_rectangle(x + i * 15, y, x + (i + 1) * 15, y + 10, fill=colors[i])

#x startposisjon, i er indeksen til vognen
#i=1
#Startpunkt: x + i * 15 → 50 + 1 * 15 = 65
#Sluttpunkt: x + (i + 1) * 15 → 50 + (1 + 1) * 15 = 80

#y er 10, endrer seg ikke nedover


def color_train_B(canvas, x, y, width, height, colors):
    l_bit = width / len(colors) #lengden på hver bit
    for i in range(0,len(colors)):
        xi_lo=x+i*l_bit
        xi_hi=xi_lo+l_bit 
        canvas.create_rectangle(xi_lo,y,xi_hi,y+height,fill=colors[i])
        #canvas.create_rectangle()

def color_train_C(canvas, x1, y1, x2, y2, colors):
    width = x2 - x1  # Total bredde
    l_bit = width / len(colors)  # Lengden på hver vogn
    for i in range(len(colors)):
        xi_lo = x1+i*l_bit  # Startpunkt for vognen
        xi_hi = x1+(i + 1)*l_bit  # Sluttpunkt for vognen
        canvas.create_rectangle(xi_lo, y1, xi_hi, y2, fill=colors[i])


