def count_xs(s):
    x_count=0
    for char in s: #Itere direkte over strengen s
        if char=='x': #sjekker om karakteren er en x og øker tellingen
            x_count+=1
    return x_count

print('Tester count_xs... ', end='')
assert 0 == count_xs('foo bar hei')
assert 1 == count_xs('x')
assert 4 == count_xs('xxCoolDragonSlayer99xx')
print('OK')

