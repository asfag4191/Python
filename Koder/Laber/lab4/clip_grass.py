def clip_grass(heights,max_heights):
    for i in range(len(heights)): #vet jo at vi skal iterere gjennom hele listen, og bruker indeks basert. Vil bytte
        #på de spesifiserte indeksene. 
        if heights[i]>max_heights: #hvis høyden som er på indeks i er større enn max høyden, må vi gi den da denne høyden
            #klipper den. 
            heights[i]=max_heights 
    return heights
            

def test_clip_grass():
    print('Testing clip_grass... ', end='')
    # Case 1
    heights = [1, 2, 3, 4, 5]
    clip_grass(heights, 3)
    assert [1, 2, 3, 3, 3] == heights

    # Case 2
    heights = [1, 2, 3, 3, 3]
    clip_grass(heights, 3)
    assert [1, 2, 3, 3, 3] == heights

    # Case 3
    heights = [10, 20, 200, 20, 400]
    clip_grass(heights, 25)
    assert [10, 20, 25, 20, 25] == heights
    print('OK')

if __name__ == '__main__':
    test_clip_grass()
