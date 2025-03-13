
#Vet ikke på forhånd hvor mange tall man må itere gjennom så bruker while-løkke
def cross_sum(x):
    total=0
    while x!=0:
        total+=x % 10 #Finner det siste tallet
        x//= 10 #Fjerner det siste tallet
    return total


def test_cross_sum():
    print('Tester cross_sum... ', end='')
    assert 6 == cross_sum(123)
    assert 7 == cross_sum(34)
    assert 0 == cross_sum(0)
    assert 1 == cross_sum(100)
    print('OK')

if __name__ == '__main__':
    test_cross_sum()

#Igjen bruker man while-løkker
#def nth_cross_sum(n,x):

