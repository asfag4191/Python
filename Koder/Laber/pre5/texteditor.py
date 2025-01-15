from uib_inf100_graphics.event_app import run_app

def app_started(app):
    app.text=' '

#legge til de vi trykker på bakerst, det er jo da en string
def key_pressed(app, event):
    if event.key == 'Space':
        app.text += ' '
    elif event.key in ['Enter', 'Return']:
        app.text += '\n'
    elif event.key.lower() == 'backspace':
        if len(app.text) > 0:
            app.text = app.text[:-1]
    elif event.key == 'Escape':
        app.text=' '
    else:
        app.text += event.key



def redraw_all(app, canvas):
    # tegn teksten
    canvas.create_text(
        20, 20,
        anchor='nw',
        text=app.text,
        font='Arial 14',
    )

run_app(width=400, height=400)