def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    stripe_width = (x2 - x1) / len(colors)  # Calculate the width of each stripe

    for i in range(len(colors)):  # Loop through the index instead of using enumerate()
        stripe_x1 = x1 + i * stripe_width  # Start of stripe
        stripe_x2 = stripe_x1 + stripe_width  # End of stripe

        canvas.create_rectangle(stripe_x1, y1, stripe_x2, y2, fill=colors[i], outline=colors[i])  # Use colors[i]


