#Finne det største tallet x er delelig på, slik som 6 vil være delelig på 3,2,1, men størst er 3. 
def largest_factor_of(x):
    list=[]
    for i in range(1,x):
        if x % i == 0:
            list.append(i)
    if list:
        return max(list) #må ha denne utfor løkken, hvis den er inni vil den avslutte iterasjonen med en gang et tall er funnet.
    #når den plasseres utforbi kjøres hele funksjonen før løkken avsluttes. Før vi returnerer resultatet. 
    else:
        return 1

print(largest_factor_of(6))

def test_largest_factor_of():
    print('Testing largest_factor_of... ', end='')
    assert 3 == largest_factor_of(6)
    assert 1 == largest_factor_of(7)
    assert 4 == largest_factor_of(8)
    print('OK')




