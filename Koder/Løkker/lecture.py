num_of_students=0
just_arrived=1

#Bruker ikke break siden betingelsen blir false når just_arrived er 0, altså 0 studenter har akk kommet. 
while just_arrived>0:
    just_arrived=int(input("Hvor mange kom inn døren?"))
    print(f'Det har kommet {just_arrived} studenter på forelesning')
    num_of_students+=just_arrived
print(f'Det har kommet totalt {num_of_students} på forelesning')
