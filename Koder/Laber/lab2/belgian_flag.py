#tegner et kvadrat for hver farge
def draw_belgian_flag(canvas, x1, y1, x2, y2):
    width = (x2 - x1) / 3

    canvas.create_rectangle(x1, y1, x1 + width, y2, fill="black", outline="")
    canvas.create_rectangle(x1 + width, y1, x1 + 2 * width, y2, fill="yellow", outline="")
    canvas.create_rectangle(x1 + 2 * width, y1, x2, y2, fill="red", outline="")


