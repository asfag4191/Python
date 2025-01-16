from uib_inf100_graphics.event_app import run_app

def app_started(app):
    app.square_left = app.width//2
    app.square_top = app.height//2
    app.square_size = 25
    app.dx = -4
    app.timer_delay = 25 # millisekunder

    app.debug_mode=False

def key_pressed(app, event):
    if event.key == "Left":
        app.dx = -4
    elif event.key == "Right":
        app.dx = 4
    elif event.key == "d":
        app.debug_mode = not app.debug_mode #her endres app.debug_mode, (True -> False, eller False -> True)
    elif app.debug_mode and event.key == "Space":
        do_step(app) # Kjører kun hvis app.debug_mode er True og Space trykkes


def timer_fired(app):
    # Denne funksjonen kalles periodisk av selve uib_inf100_graphics
    # -rammeverket. Hvor ofte bestemmes av verdien i app.timer_delay.
    if not app.debug_mode: #sjekker om debug_mode er false, altså av da kalles det som er inne i if-setningen.
        do_step(app) #kalles do step når den er av


def do_step(app):
    # Flytt horisontalt
    app.square_left += app.dx

    # Sjekk om firkanten har gått utenfor lerretet, og hvis ja, snu
    # retning; men flytt også firkanten til kanten (i stedet for å gå
    # forbi). Merk: det finnes andre, mer sofistikerte måter å håndtere
    # at rektangelet går forbi kanten...
    if app.square_left < 0:
        # snu retningen!
        app.square_left = 0
        app.dx = -app.dx
    elif app.square_left > app.width - app.square_size:
        app.square_left = app.width - app.square_size
        app.dx = -app.dx

def redraw_all(app, canvas):
    # tegn firkanten
    canvas.create_rectangle(
        app.square_left,
        app.square_top,
        app.square_left + app.square_size,
        app.square_top + app.square_size,
        fill="yellow",
    )


run_app(width=400, height=150)
