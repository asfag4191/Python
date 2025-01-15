def filter_dangerous(plants, dangerous_plants):
    safe_plants=[]
    for i in plants:
        if i not in dangerous_plants:
           safe_plants.append(i)
    return safe_plants


print("Testing filter_dangerous... ", end="")
assert ["rose", "daisy", "lily", "tulip"] == filter_dangerous(["rose", "daisy", "lily", "tulip", "dandelion"], ["dandelion", "poison ivy"])
assert ["minalia", "cherluvia", "kirina", "ajisai"] == filter_dangerous(["minalia", "cherluvia", "kirina", "ajisai", "evil_plant", "raa"], ["evil_plant", "raa"])
assert ["pythonium"] == filter_dangerous(["pythonium", "haskelia", "shakersperia"], ["haskelia", "jaskria", "shakersperia"])
print("OK")
