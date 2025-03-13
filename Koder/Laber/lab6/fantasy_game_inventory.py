def display_inventory(d):
    count = 0
    output = "Inventory:\n"  # Lager en streng som skal returneres
    for item, amount in d.items():
        count += amount
        output += f"{amount} {item}\n"  # Legger til hver linje i output-strengen
    output += f"\nTotal number of items: {count}"  # Legger til totalsum
    return output  # Returnerer hele output-strengen

# Testkjøring
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
print(display_inventory(stuff))  # Nå skrives alt ut korrekt)
