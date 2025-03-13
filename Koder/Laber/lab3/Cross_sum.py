
#Gjø rom til en str, legger til hvert element i en liste. 
#Deretter hente ut dette tallet på plassen til indeksen og plusser sammen
#på denne måten kan vi hente ut et og et tall. 
def cross_sum(x):
    x=str(x)
    list=[]
    count=0
    for i in range(len(x)):
        list.append(x[i])
        count+=int(x[i])
    return count

#En annen metode: 
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

#n'te tallet med tverrsum x
#f.eks tverrsum 7 er n=1, andre er 16
def nth_cross_sum(n, x): 
    count = 0  # Teller hvor mange tall vi har funnet med tverrsum x
    num = 0    # Starter søket fra 0

    while count < n:
        num += 1  # Øker tallet vi sjekker, sjekker 1 og 1 tall, helt til vi finner
        #f.eks det tredje tallet som har en tverrsum med 7
        tverrsum = cross_sum(num)  # Beregner tverrsummen av dette tallet, har jo forrige funksjon

        print(f"Sjekker {num}: tverrsum = {tverrsum}")  # Debugging: viser hva som skjer

        if tverrsum == x:  # Sjekker om tverrsummen er lik x, altså 25 sin tverrsum=7
            count += 1  # Øker telleren når vi finner et gyldig tall

            print(f"Fant {count}. tall med tverrsum {x}: {num}")  # Viser hvilke tall som finnes

    return num  # Returnerer det n-te tallet med tverrsum x
       


def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    #assert nth_cross_sum(2, 10) == 28
    #assert nth_cross_sum(10, 2) == 2000
    print('OK')

if __name__ == '__main__':
    test_nth_cross_sum()
    





