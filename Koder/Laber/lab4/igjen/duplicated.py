def duplicated(items):
    new_list=[]
    for i in range(0,len(items)):
        new_list.append(items[i]*2)
    return new_list

def test_duplicated():
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

if __name__ == '__main__':
   test_duplicated()