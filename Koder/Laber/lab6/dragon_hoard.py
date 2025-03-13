from fantasy_game_inventory import display_inventory 

from fantasy_game_inventory import display_inventory 

def add_to_inventory(inventory, added_items):
    new_dict = inventory.copy()  # Lager en kopi for å unngå destruktive endringer
    print("Inventory")

    for item in added_items:  # Går gjennom listen med nye elementer
        if item in new_dict:
            new_dict[item] += 1  # Øker antallet hvis elementet allerede finnes
        else:
            new_dict[item] = 1  # Legger til nytt element hvis det ikke finnes

    return new_dict  # Returnerer den oppdaterte inventory

# Testdata
inv = {"gold coin": 42, "rope": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
updated_inv = add_to_inventory(inv, dragon_loot)

# Skriv ut inventaret etter oppdatering
print(display_inventory(updated_inv))
