#String til liste med tall
def compress(raw_binary):
    count=1
    count_list=[]

    if raw_binary[0]=='1': #hvis første tegnet er 1, skal den starte med 0. 
        count_list.append(0)

    for i in range(0,len(raw_binary)-1): #iterer over lengden til strengen. 
        if raw_binary[i]==raw_binary[i+1]: #sjekker om tallene som forekommer er lik det forrige, isåfall legger til i count
            count+=1
        else:
            count_list.append(count) #hvis ikke legger vi til tallet i en liste og starter count på nytt
            count=1

    #for-løkken kjører ikke else delen på den siste iterasjonen, vanlig praksis
    #else-blokken kjøres hvis for-løkka fullføres normalt uten at den blir avbrutt av en break-setning.
    #else-blokken kjører ikke for hver iterasjon eller som en avslutning på hver iterasjon.
    count_list.append(count) #legger til siste telleren
    return count_list

print(compress('110111111110'))
def test_compress():
    print('Tester compress... ', end='')
    assert([2, 3, 4, 4] == compress('0011100001111'))
    assert([0, 2, 1, 8, 1] == compress('110111111110'))
    assert([4] == compress('0000'))
    print('OK')

if __name__ == '__main__':
    test_compress()

#DelB
#Liste til string
def decompress(compressed_binary):
    compressed_string='' #legger til resultatet

    for i in range(len(compressed_binary)): #iterer over lengden til listen, inkludere alle tallene.
        n=compressed_binary[i]
        if i % 2==0:
            compressed_string+=("0"*n)
        else:
            compressed_string+=("1"*n)
    return compressed_string

print(decompress([2, 3, 4, 4]))

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')

if __name__ == '__main__':
    test_decompress()

