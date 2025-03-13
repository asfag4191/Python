from math import sqrt


def circle_or_square(rad,area):
    #returns true if circle greater than area
    circle=2*3.14*rad
    square=sqrt(area)*4
    if circle>square:
        return True
    else: 
        return False
    


def test():  
    assert circle_or_square(16, 625) == True
    assert circle_or_square(8, 144) == True
    assert circle_or_square(15, 400) == True
    assert circle_or_square(5, 100) == False
    assert circle_or_square(18, 900) == False
    assert circle_or_square(1, 4) == False
    print('OK')

if __name__ == '__main__':
    test()