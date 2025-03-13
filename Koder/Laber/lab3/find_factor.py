#Største tallet (faktor) et tall er delelig på
def largest_factor_of(x):
    list=[]
    for i in range(1,x):
        if x % i == 0:
            list.append(i)
    if list:
        return max(list) 
    #utfor løkken, kjøres når hele iterasjonen er fullført.
    else:
        return 1

print(largest_factor_of(6))

def test_largest_factor_of():
    print('Testing largest_factor_of... ', end='')
    assert 3 == largest_factor_of(6)
    assert 1 == largest_factor_of(7)
    assert 4 == largest_factor_of(8)
    print('OK')




