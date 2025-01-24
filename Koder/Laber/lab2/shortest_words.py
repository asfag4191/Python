word1=str(input('Skriv et ord:\n'))
word2=str(input('Skriv et annet ord:\n'))
word3=str(input('Skriv et siste ord:\n'))

print(' ')

shortest= min(len(word1),len(word2),len(word3))
if shortest==len(word1):
    print (word1)
if shortest==len(word2):
    print(word2)
if shortest==len(word3):
    print(word3)
