def alternate_sign_sum(nums):
    total_sum=0
    for i in range(0,len(nums)):
        if i%2==0: #kan ikke bruke nums[i] siden det er ikke sikkert at annenhvert tall vil være partall og oddetall.
            #nums[i] sjekker verdien på indeksen og ikke indeksen selv.  
            #Bruker i, for vil jo alternaterende, altså når i=1, ikke partall, i=2 partall, får da annenhver. 
            total_sum+=nums[i]
        else:
            total_sum-=nums[i]
    return total_sum

def test_alternate_sign_sum():
    print('Tester alternate_sign_sum... ', end='')
    assert 3 == alternate_sign_sum([1, 2, 3, 4, 5])
    assert 30 == alternate_sign_sum([10, 20, 30, 40, 50])

    a = [-10, 20, -30, 40, -50]
    assert -150 == alternate_sign_sum([-10, 20, -30, 40, -50])
    assert [-10, 20, -30, 40, -50] == a # Sjekk at funksjon ikke er destruktiv
    print('OK')

if __name__ == '__main__':
    test_alternate_sign_sum()

