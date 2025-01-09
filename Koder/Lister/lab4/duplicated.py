def duplicated(items):
    items_2=[]
    for i in items: #bryr oss ikke om index da fungerer det bra å bruke for i in, siden det er elementene vi skal multiplisere
        items_2.append(i*2)
    return items_2


items=[1,2,3]
print(duplicated(items))

#hvis jeg hadde brukt for i in range må jeg bruke indeksen
def duplicated(items):
    items_2 = []
    for i in range(len(items)):  # Iterer over indeksene i listen
        items_2.append(items[i] * 2)  # Må få tilgang til hvert element på indeksen. 
    return items_2

print("Testing duplicate... ", end="")
# Første test
a = [1, 2, 3, 4, 5]
actual = duplicated(a)
expected = [2, 4, 6, 8, 10]
assert expected == actual    # Sjekker at returverdien er som ønsket
assert [1, 2, 3, 4, 5] == a  # Sjekker at input (a) ikke har blitt mutert

# Flere tester
assert [4, 8, 12, 16, 20] == duplicated([2, 4, 6, 8, 10])
assert [0, 0, 0, 0, 0] == duplicated([0, 0, 0, 0, 0])
assert [-2, 4, 2, 10, 100] == duplicated([-1, 2, 1, 5, 50])
print("OK")
