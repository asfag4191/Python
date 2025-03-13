def threes_removed(a):
    b=list(a) #kopiering slik det ikke blir destruktivt, hvis b=a blir det destruktivt
    while 3 in b:
        b.remove(3)
    return b

print('Tester threes_removed... ', end='')
# Test 1
a = [1, 2, 3, 4]
actual = threes_removed(a)
expected = [1, 2, 4]
assert expected == actual   # Sjekker at returverdien er som ønsket
assert [1, 2, 3, 4] == a    # Sjekker at input (a) ikke har blitt mutert

# Test 2
a = [1, 2, 3, 3]
actual = threes_removed(a)
expected = [1, 2]
assert expected == actual
assert [1, 2, 3, 3] == a

# Test 3
a = [3, 3, 1, 3, 2, 4, 3, 3, 3]
actual = threes_removed(a)
expected = [1, 2, 4]
assert expected == actual
assert [3, 3, 1, 3, 2, 4, 3, 3, 3] == a

# Test 4
a = [3, 3]
actual = threes_removed(a)
expected = []
assert expected == actual
assert [3, 3] == a
print('OK')






