gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

#Question 1
print("Do you like Dawn or Dusk?")
answer=int(input("1. Dawn\n2. Dusk\n"))
if answer==1:
    gryffindor+=1
    ravenclaw+=1
elif answer==2:
    hufflepuff+=1
    slytherin+=1
else:
    print("Wrong input")

#Question 2
print("When I'm dead I want people to remember me as:\n1)The God\n2)The Great\n3)The Wise\n4)The Bold")
answer_2=int(input("Enter your answer 1-4: "))
if answer_2==1:
    hufflepuff+=2
elif answer_2==2:
    slytherin+=2
elif answer_2==3:
    ravenclaw+=2
elif answer_2==4:
    gryffindor+=2
else:
    print("Wrong input")

#Question 3
print("Which kind of instrument most pleases your ear?\n1)The violin\n2)The trumpet\n3)The piano\n4)The drum")
answer_3=int(input("Enter your answer 1-4: "))
if answer_3==1:
    slytherin+=4
elif answer_3==2:
    hufflepuff+=4
elif answer_3==3:
    ravenclaw+=4
elif answer_3==4:
    gryffindor+=4
else:
    print("Wrong input")

print(f'Point per house is:\n Gryffindor:{gryffindor}\n Hufflepuff:{hufflepuff}\n Ravenclaw:{ravenclaw}\n Slytherin:{slytherin}')

#Print out the house with the most points
most_points=max(gryffindor,slytherin,ravenclaw,hufflepuff)

if gryffindor == most_points:
  print(f'Gryffindor! with {most_points} points')
elif ravenclaw == most_points:
  print(f'Ravenclaw !with {most_points} points')
elif hufflepuff == most_points:
  print(f'Hufflepuff!with {most_points} points')
else:
  print(f'Slytherin! with {most_points} points')

