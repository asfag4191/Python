x = 10  # Global variabel

def lokal_funksjon():
    y = 5  # Lokal variabel (skjuler den globale x inne i funksjonen)
    print("Lokal y:", y)

def endre_global():
    x = 20  # Kan ikke endre den globale
    print("Prøver å endre global:", x) 

print("Global x før endring:", x)
endre_global()
print("Global x ett prøvd endring:", x)

#kan ikke printes her, kaller på en lokal funksjon
#lokal_funksjon()
#print("Lokal y:", y)




#hvis man skal hopppe over resten av koden hvis man finner en gitt betingelse
l=5
while l>0:
    l-=1
    if l==2:
        continue #Hopper over når x==2
    print(l)

#finne første 2
x = 5
while x > 0:
    if x == 2:
        break  # Hopper ut når x == 2
    print(x)
    x -= 1


new=5
while new>0:
    if new==2:
        continue #Hopper over når x==2
    print(new)
    new-=1
#evig løkke, når den treffer 2, ingenting som øker eller minker

