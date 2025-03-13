def find_treasure(grid, target_sum):
    treasure=[] #koordinatene til skattene
    rows=len(grid) #antall rader
    cols=len(grid[0]) #antall kolonner

    for row in range(rows): #iterer over radene, for hver rad må man iterer over kolonnene
        for col in range(cols): #iterer over alle kolonnene på den raden vi er på
            value=grid[row][col] #henter ut verdi på posisjonen vi er på
            if row+col+value==target_sum: #legger sammen raden, kolonnen og den verdien som er i rutenettet.
                treasure.append([row, col]) #legger til kun den raden og kolonnen vi er på.
    return treasure


def test_find_treasure():
  print("Testing find_treasure... ", end="")
  # Test 1
  grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]
  target_value = 5
  actual = find_treasure(grid, target_value)
  expected = [[0, 2], [1, 0]]
  assert expected == actual

  # Test 2
  actual = find_treasure([[1, 2], [3, 4]], 3)
  expected = [[0, 1]]
  assert expected == actual

  # Test 3
  actual = find_treasure([[1, 2], [3, 4]], 1)
  expected = [[0, 0]]
  assert expected == actual

  # Test 4
  actual = find_treasure([[1, 2], [3, 4]], 1000)
  expected = []
  assert expected == actual

  print("OK")


if __name__ == '__main__':
    test_find_treasure()