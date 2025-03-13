#Tallrekke med for-løkke
def sequence_for(n): #Tar inn et heltall n
    numbers="" #Initialisere en tom streng
    for i in range(0,n+1): #Må plusse n med 1 for å inkludere det gitte tallet
        numbers+=f'{i} ' #Legger til hvert tall etterfulgt av mellomrom
        #numbers+=str(i)+' ' #må konvertere i til en string
    return numbers

print("Tester sequence_for... ", end="")
assert "0 1 2 3 4 5 " == sequence_for(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
assert "0 " == sequence_for(0)
print("OK")

#Tallrekke med while-løkke
def sequence_while(n):
    numbers=""
    num=0
    while num<=n: #Kjører så lenge betingelsen er sann
        numbers+=f'{num} '
        num += 1 #Viktig å øke for å unngå evigvarende loop
    return numbers

print("Tester sequence_while... ", end="")
assert "0 1 2 3 4 5 " == sequence_while(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
assert "0 " == sequence_while(0)
print("OK")


