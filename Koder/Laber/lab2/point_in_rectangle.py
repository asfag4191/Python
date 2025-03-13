def point_in_rectangle(x1, y1, x2, y2, xp, yp):
#sjekker rekkefølgen til to motsatte hjørner
#må jo finne høyre, og venstre siden til rektangelet og hvor høyt det er for å se om punktet er innafor. 
    x_left = min(x1, x2)
    x_right = max(x1, x2)
    y_top=min(y1,y2)
    y_bottom=max(y1,y2)
    if x_left<=xp and xp<=x_right and y_top<=yp and yp<=y_bottom:
        return True
    else:
        return False

def test_point_in_rectangle():
    print('Tester point_in_rectangle... ', end='')
    assert point_in_rectangle(0, 0, 5, 5, 3, 3) is True # Midt i
    assert point_in_rectangle(0, 5, 5, 0, 5, 3) is True # På kanten
    assert point_in_rectangle(0, 0, 5, 5, 6, 3) is False # Utenfor
    print('OK')

if __name__ == '__main__':
    test_point_in_rectangle()


