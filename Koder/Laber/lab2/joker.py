import random

list=[]
tall1=int(input("tall1 = "))
list.append(tall1)

tall2=int(input("tall2 = "))
list.append(tall2)

tall3=int(input("tall3 = "))
list.append(tall3)

tall4=int(input("tall4 = "))
list.append(tall4)

tall5=int(input("tall5 = "))
list.append(tall5)


for num in list: 
    if num<5:
        print('opp')
    if num>=5:
        print('ned')




