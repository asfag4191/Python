from point_in_rectangle import point_in_rectangle
from distance import distance

def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    x1_left = min(x1, x2)
    x1_right = max(x1, x2)
    y1_top=min(y1,y2)
    y1_bottom=max(y1,y2)

    x2_left=min(x3,x4)
    x2_right=max(x3,x4)
    y2_top=min(y3,y4)
    y2_bottom=max(y3,y4)

    if x1_left<=x2_right and x2_left<=x1_right and y1_top<=y2_bottom and y2_top<=y1_bottom:
        return True
    else:
        return False


    #if x_left<=xp and xp<=x_right and y_top<=xp and yp<=y_bottom:

def test_rectangles_overlap():
    print('Tester rectangles_overlap... ', end='')
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
    print('OK')



def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
    x_left=min(x1,x2)
    x_right=max(x1,x2)
    y_top=min(y1,y2)
    y_bottom=max(y1,y2)
    
    x_left_ex=x_left-rc
    x_right_ex=x_right+rc
    y_top_ex=y_top-rc
    y_bottom_ex=y_bottom+rc

    #sjekker sirkelens sentrum 
    if point_in_rectangle(x1, y1, x2, y2, xc, yc): 
        return True
    #sjekker for om sentrum er utenfor det utvidete rektangelet
    elif not point_in_rectangle(x_left_ex, y_top_ex, x_right_ex, y_bottom_ex, xc, yc):
        return False
    # punkt er mellom venstre og høyresiden til rektangel (x-aksen) og y-akse
    if x_left <= xc <= x_right:
        return True
    # sjekker om punktet er mellom topp og bunn
    if y_top <= yc <= y_bottom:
        return True
    # sirkelen overlapper hjørnet oppe til venstre
    elif distance(x_left, y_top, xc, yc) <=rc:
        return True
    #oppe til høyre
    elif distance(x_right,y_top,xc,yc)<=rc:
        return True
    #sirkelen overlapper hjørnet nede høyre
    elif distance(x_right, y_bottom, xc,yc)<=rc:
        return True
    #nede venstre
    elif(distance(x_left,y_bottom,xc,yc))<=rc:
        return True
    else:
        return False
  
    


def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten
    print('OK')


if __name__ == '__main__':
    test_rectangles_overlap()
    test_circle_overlaps_rectangle()