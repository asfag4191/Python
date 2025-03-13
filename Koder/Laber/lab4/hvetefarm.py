import random


MAX_GROWTH = 8

# bruk denne for å se jordet etter hver iterasjon om du ønsker
def print_field(field):
    line = "+---+---+---+---+"
    for row in field:
        print(line)
        for cell in row:
            print(f"| {cell} ", end="")
        print("|")
    print(line)

def simulate_wheat_farm(field, seeds, iterations):
    rows = len(field)
    cols = len(field[0])
    wheat = 0
    for _ in range(iterations):

        for row in range(rows):
            for col in range(cols):
                growth_stage = field[row][col]
                if (growth_stage == 0) and (seeds > 0):   # Plant et frø
                    field[row][col] =1
                    seeds-=1
                    
                elif 1 <= growth_stage < MAX_GROWTH:       # Vokse planten
                    field[row][col] += 1 #må fikse plassen i mappet og ikke bare growth 
                
                elif growth_stage == MAX_GROWTH:      # Høst en ferdig plante
                    wheat += 1
                    field[row][col] = 0
                    seeds += random.randint(1, 4)
        # print_field(field)
    return wheat, seeds



def test_simulate_wheat_farm():
    print("Testing simulate_wheat_farm()... ", end="")
    field = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    random.seed(1689)
    wheat, seeds = simulate_wheat_farm(field, 1, 10)
    assert wheat == 1
    assert seeds == 0
    
    field = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    random.seed(1689)
    wheat, seeds = simulate_wheat_farm(field, 7, 100)
    assert wheat == 167
    assert seeds == 245
    print("OK")


if __name__ == '__main__':
    test_simulate_wheat_farm()
 
