# pig_main.py
from uib_inf100_graphics.simple import canvas, display

from pig_body import draw_body
from pig_head import draw_head

# TODO: kall på funksjonene draw_body og draw_head

if __name__ == '__main__':
    #hjørnene til 'firkanten'
    draw_body(canvas, 50, 100, 250, 250)
    
    #det siste tallet er radiusen på hodet
    #x er frem og tilbake (første tallet)
    #y er ned og opp (andre tallet)
    draw_head(canvas, 250, 150, 50)


display(canvas)

