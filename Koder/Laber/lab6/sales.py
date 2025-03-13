from pathlib import Path  # Korrekt import


def total_income(path):
    #leser inn csv-filen manuelt
    content=Path(path).read_text(encoding='utf-8')
    content_lines=content.splitlines()
    table=[]
    total=0
    for line in content_lines:
        row=line.split(',')
        table.append(row)
    #print(table)
    for i in range(1,len(table)):
        name, production_cost, price, sold=table[i] #pakker ut verdiene fra hver linje
        production_cost=int(production_cost) #de er i formatet som streng så må gjøre om til int. 
        price=int(price)
        sold=int(sold)
        price=sold*(price-production_cost)
        total+=price
    return total

def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('Koder/Laber/lab6/sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')


if __name__=='__main__':
    test_total_income()