#A

def get_stringsum(s):
    s=s.split(" ")
    count=0
    for i in range(len(s)):
        try:
            if int(s[i]):
                count+=int(s[i])
        except ValueError:
            continue
    #print(count)
    return count


           
    


def test_get_stringsum():
    print('Testing get_stringsum... ', end='')
    assert 6 == get_stringsum('4 2')
    assert 9 == get_stringsum('5 -1 3 +2')
    assert 11 == get_stringsum('5 - 1 3 + 2')
    assert 42 == get_stringsum('42')
    assert 42 == get_stringsum('forty-one 42 førtitre')
    assert 42 == get_stringsum('foo2 42 2qux 3x1')
    assert 0 == get_stringsum('')
    assert 0 == get_stringsum('foo bar qux')
    assert 0 == get_stringsum('-9- 3+2')
    print('OK')



#B
def get_line_with_highest_stringsum(s):
    s = s.split('\n') #splitter basert på lijer 
    count = 0  
    i = 1  
    r = ""  
    t = 0  

    for n in range(len(s)): #iterer gjennom hver linje
        numbers = s[n].split()  # Splitter linjen i ord/tall
        new_count = 0  #nullstille summen for hver linje

        for k in numbers:  # Itererer gjennom ordene/tallene i linjen
            try:
                new_count += int(k) #prøver å konvertere for hvert tall/ord til heltall
            except ValueError:
                continue  #hopper over hvis det ikke er et tall

        if new_count > count:  #sjekker om høyeste sum, og oppdaterer variablene. 
            count = new_count
            i = n + 1
            r = s[n]
            t = count  

    return i, t, r





    

def test_get_line_with_highest_stringsum():
    print('Testing get_line_with_highest_stringsum... ', end='')

    arg = '4 2\n3 3\n6 6 6 6 12 6\n'
    assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

    arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
    assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

    arg = '4 2\n3 3\n'
    assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

    print('OK')



#C

def main():
    path=('Koder/Laber/lab6/stringsums_file.txt')
    with open(path,'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
    best_line, highest_sum, line_number = get_line_with_highest_stringsum(content)  # Kaller funksjonen
    print(f'Høyeste strengsum er {highest_sum}, funnet først på linje {best_line}:"{line_number}"')



if __name__=='__main__':
    #s=('5 -1 3 +2')
    #get_stringsum(s)
    #s='4 2\n3 3\n6 6 6 6 12 6\n'
    #get_line_with_highest_stringsum(s)
    test_get_stringsum()
    test_get_line_with_highest_stringsum()
    main()


