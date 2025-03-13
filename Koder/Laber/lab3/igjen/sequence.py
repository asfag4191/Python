#def sequence_for(n):
#    streng=""
#    for i in range(0,n+1):
 #       streng+=f'{i} '
  #  return streng

def sequence_for(n):
    streng=""
    for i in range(0,n+1):
        streng+=str(i) + " "
    return streng




print("Tester sequence_for... ", end="")
assert "0 1 2 3 4 5 " == sequence_for(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
assert "0 " == sequence_for(0)
print("OK")

def sequence_while(n):
    streng=""
    i=0
    while i<=n:
        streng+=str(i)+ " "
        i+=1 #må øke telleren
    return streng

print("Tester sequence_while... ", end="")
assert "0 1 2 3 4 5 " == sequence_while(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
assert "0 " == sequence_while(0)
print("OK")
 
    