#Skriv en funskjon som tar inn en liste med binærtall 0 og 1, 
# og returnerer True hvis kun det første tallet i listen er 1.

def only_first_is_one(list_of_digits):
    x = list_of_digits[0]
    if x==0:
        return False #må returnere False slik man sjekker resten av listen og, hvis returnere true, vil den hoppe ut.
    for d in list_of_digits[1:]:
        if d == 1:
            return False
    return True

print(only_first_is_one([1,0,0,0,0]))

print(only_first_is_one([1,1,0,0,0]))

