def filter_dangerous(plants, dangerous_plants):
    safe_plants=[]
    for char in plants:
       if char not in dangerous_plants:
          safe_plants.append(char)
    return safe_plants



    #for i in range(0,len(plants)):
       # for j in range(i+1,len(dangerous_plants)):
           # if dangerous_plants[j] != plants[i]:
               # safe_plants.append(plants[i])
   # return safe_plants

def test_filter_dangerous():
  print("Testing filter_dangerous... ", end="")
  assert ["rose", "daisy", "lily", "tulip"] == filter_dangerous(["rose", "daisy", "lily", "tulip", "dandelion"], ["dandelion", "poison ivy"])
  assert ["minalia", "cherluvia", "kirina", "ajisai"] == filter_dangerous(["minalia", "cherluvia", "kirina", "ajisai", "evil_plant", "raa"], ["evil_plant", "raa"])
  assert ["pythonium"] == filter_dangerous(["pythonium", "haskelia", "shakersperia"], ["haskelia", "jaskria", "shakersperia"])
  print("OK")

if __name__ == '__main__':
    test_filter_dangerous()