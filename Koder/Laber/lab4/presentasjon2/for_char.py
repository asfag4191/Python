def return_count_a(b):
    count=0
    for char in b:
        #char iterand, b er iterabel
        if char=='a':
            count+=1
    return count


b='hei alle sammen' #blir et element hvis gjør om til liste

print(return_count_a(b))

s=['h','e','i','a','a']
def return_count(s):
    count=0
    for i in range(len(s)):
        #i er iterand, iterer over hvert element, så langt lenden til s er
        if s[i]=='a':
            count+=1
    return count

print(return_count_a(s))


