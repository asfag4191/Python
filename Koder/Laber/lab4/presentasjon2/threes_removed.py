def threes_removed(a):
    list=[]
    for i in range(len(a)):
        if a[i]!=3:
            list.append(a[i])
    return list


b=[1,2,3,4,5,5,4]
for i in (b):
    if i==3:
        b.remove(i)
print(b)

def threes_removed1(a):
    b=list(a) #kopiering slik det ikke blir destruktivt, hvis b=a blir det destruktivt
    while 3 in b: #kjører så lenge vi har 3 i koden, altså så lenge betingelsen er sann. 
        b.remove(3)
    return b






def test_threes_removed():
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


if __name__ == '__main__':
    test_threes_removed()
