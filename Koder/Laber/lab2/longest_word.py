word1=str(input('Skriv et ord:\n'))
word2=str(input('Skriv et annet ord:\n'))
word3=str(input('Skriv et siste ord:\n'))

print(' ')

longest= max(len(word1),len(word2),len(word3))
if longest==len(word1):
    print (word1)
elif longest==len(word2):
    print(word2)
else:
    print(word3)