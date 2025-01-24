def volume_of_box(w, h, d):
    volum=w*h*d
    return volum

print('Testing volume of box... ', end='')
assert 30 == volume_of_box(2, 3, 5)
assert 1 == volume_of_box(1, 1, 1)
print('OK')