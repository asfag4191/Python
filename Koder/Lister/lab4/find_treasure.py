def find_treasure(grid,target_sum):
    treasures=[]
    rows=len(grid) #antall rader
    #cols=len(grid[0])
    for i in range(rows): #må ha en for-løkke for å iterere over antall rader å lage kolonnene for hver rad. Altså i-ende rad
        cols=len(grid[i])
    
    for row in range(rows): #iterer over hver rad indeks
        for col in range(cols): #for hver rad indeks iterer den over hver kolonne-indeks
            value = grid[row][col] #henter ut verdien på posisjonen
            if value+row+col==target_sum:
                treasures.append([row, col]) #legger til kordinatene for row og col, hvis summen er lik target sum. 
    return treasures

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


