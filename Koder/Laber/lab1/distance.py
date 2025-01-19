from math import sqrt

x1=int(input('x1 = \n'))
y1=int(input('y1 = \n'))
x2=int(input('x2 = \n'))
y2=int(input('y2 = \n'))
#x1=int(input("X-koordinatet til første punkt: "))
#y1=int(input("Y-koordinatet til første punkt: "))
#x2=int(input("X-koordinatet til andre punkt: "))
#y2=int(input("Y-koordinatet til andre punkt: "))
d=sqrt(((abs(x1-x2))**2)+(abs(y1-y2)**2))
print(f'Avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er {d}')