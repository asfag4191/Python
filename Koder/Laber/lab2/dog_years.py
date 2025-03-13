def human_to_dog_years(x):
    dog = 0
    if x <= 2:
        dog= x * 10.5
    else:
        dog= 2 * 10.5
        dog += (x-2) * 4 #de to første hundeårene er allerede håndtert sepereat
        #de to første er allerede regnet, er kun resten vi skal regne som 4 nå. 
    return dog

    
def almost_equals(a, b):
    return abs(a - b) < 0.00000001

def test_human_to_dog_years():
    print('Tester human_to_dog_years... ', end='')
    assert almost_equals(15.75, human_to_dog_years(1.5))
    assert almost_equals(21.00, human_to_dog_years(2))
    assert almost_equals(57.00, human_to_dog_years(11))
    print('OK')

if __name__ == '__main__':
    test_human_to_dog_years()