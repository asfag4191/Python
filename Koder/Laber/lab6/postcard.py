def symbol_count(path):
    with open(path, 'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
        content=''.join(content.split())
    dict={} #tomt oppslagsverk
    #nøkkel skal være inneholdet i filen, og verdien er antall forekomster av nøklene. 
    for i in range(len(content)):
        if content[i] not in dict:
            dict[content[i]]=1 #legger til innholdet i content som nøkkel og gir den verdi, 
            #altså antall ganger det forekommer
        else:
            dict[content[i]]+=1
    return dict

def test_count_letters():
    print('Tester count_letters... ', end='')
    expected = {
        'K': 2, 'j': 1, 'æ': 1, 'r': 10, 'e': 15, 'v': 3, 'n': 10, ',': 2,
        'S': 2, 'a': 3, 't': 2, 'y': 3, '.': 2, '"': 2, 'F': 2, 'i': 3,
        ':': 1, 'B': 1, 'o': 2, 'd': 2, 'J': 1, 'u': 1, "'": 1, 's': 4,
        'E': 1, 'p': 1, '!': 1, 'l': 2, 'm': 3,
    }
    actual = symbol_count('postcard.txt')
    assert 'æ' in actual, 'æ mangler, har du husket utf-8 encoding?'
    assert expected == actual
    print('OK')

if __name__=='__main__':
    test_count_letters()


        