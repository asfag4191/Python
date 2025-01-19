bugs = ['Marihøne', 'Sommarfugl', 'Fluge', 'Mygg']

print('Tilgjengelige insekt:')
print('1. ' + bugs[0])
print('2. ' + bugs[1])
print('3. ' + bugs[2])
print('4. ' + bugs[3])

print('Kva er favorittinsektet ditt? Svar med eit tal [1-4]')
i = int(input())
print('Ditt favorittinnsekt er:', bugs[i-1])
