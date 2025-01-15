def smallest_absolute_difference(a):
    sorted_list=sorted(a)
    least_difference=float('inf') #uendelig høy verdi, sammenligner mot denne
    for i in range(len(sorted_list)): #går gjennom alle indeksene fra 0-lengen av listen, iterer over alle i
        for j in range(i+1,len(sorted_list)):  #iterer over alle påfølgende elementene til i, altså j+1. Sammenligner i med j.
            difference=abs(sorted_list[j]-sorted_list[i]) #bruekr abs() slik jeg får returnert et positivt tall, rekkefølge på i og j har ingenting å si.
            if difference<least_difference:
                least_difference=difference #oppdaterer den minste forskjellen
    return least_difference 

#ikke destruktiv og mindre kjøretid
def smallest_absolute_difference2(a):
    sorted_list=sorted(a) #Ikke destruktiv, lager en kopi, sortert liste, lettere å sammenligne
    least_difference=float('inf') #Uendelig høy verdi, sammenligner mot
    for i in range(len(sorted_list-1)): #enkel for-løkke opp til nest siste element
        difference=abs(sorted_list[i+1]-sorted_list[i]) #tar jo da en verdi større enn den indeksen vi er ppå, minus den vi er på for å finne forskjellen
        if difference<least_difference:
            least_difference=difference #oppdaterer least_difference
    return least_difference



def test_smallest_absolute_difference():
    print('Tester smallest_absolute_difference... ', end='')
    assert 1 == smallest_absolute_difference([1, 20, 4, 19, -5, 99])  # 20-19
    assert 6 == smallest_absolute_difference([67, 19, 40, -5, 1])  # 1-(-5)
    assert 0 == smallest_absolute_difference([2, 1, 4, 1, 5, 6])  #1-1
    a = [50, 40, 70, 33]
    assert 7 == smallest_absolute_difference(a)
    assert [50, 40, 70, 33] == a  # Sjekker at funksjonen ikke er destruktiv
    print('OK')

def test_smallest_absolute_difference2():
    print('Tester smallest_absolute_difference2... ', end='')
    assert 1 == smallest_absolute_difference([1, 20, 4, 19, -5, 99])  # 20-19
    assert 6 == smallest_absolute_difference([67, 19, 40, -5, 1])  # 1-(-5)
    assert 0 == smallest_absolute_difference([2, 1, 4, 1, 5, 6])  #1-1
    a = [50, 40, 70, 33]
    assert 7 == smallest_absolute_difference(a)
    assert [50, 40, 70, 33] == a  # Sjekker at funksjonen ikke er destruktiv
    print('OK')

if __name__ == '__main__':
    test_smallest_absolute_difference()
    test_smallest_absolute_difference2()




