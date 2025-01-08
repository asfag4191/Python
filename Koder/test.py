a = [3, 3, 2, 3, 4]
print("Først, a =", a)  # Før listen endres

# Mislykket forsøk på å fjerne alle 3'erne
def should_be_removed(x):
    return x == 3

for item in a:
    print(f"Itererer over item: {item}")  # Viser hvilket element vi ser på
    if should_be_removed(item):
        print(f"  {item} skal fjernes (a før fjerning: {a})")
        a.remove(item)
        print(f"  a etter fjerning: {a}")  # Listen etter fjerning
    else:
        print(f"  {item} beholdes (a: {a})")  # Listen forblir uendret

print("Etter, a =", a)  # Etter alle iterasjone