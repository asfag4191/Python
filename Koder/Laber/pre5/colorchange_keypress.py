from uib_inf100_graphics.event_app import run_app

#beholder for alle variablene, som til sammen beskriver tilstanden for programet
def app_started(app):
    app.color='yellow'

#kalles hver gang vi trykker på en tast
def key_pressed(app, event):
    if event.key=='r':
        app.color='red'
    elif event.key=='g':
        app.color='green'
    elif event.key=='b':
        app.color='blue'
    elif event.key=='y':
        app.color='yellow'
    else:
        app.color='black'

def redraw_all(app, canvas):
    # tegn firkanten
    canvas.create_rectangle(
        25, 25, app.width - 25, app.height - 25,
        fill=app.color,
    )

run_app(width=400, height=150)
