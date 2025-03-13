
#letter er bokstavsamling slik som scrabble
#returnere liste med alle de ordene man kan lage med de gitte ordene
#Det er ikke lov å bruke samme bokstav i ordene du returnerer flere ganger enn den opptrer i letters.

#må splitte opp hund og itere gjennom karakterene, sjekke om jeg kan lage de kombinasjonene
def possible_words_from_file(path, letters):
    with open (path, 'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
        content=content.splitlines() #returnere ny liste der hver linje er nå en streng
    
    best_list=[] #listen jeg skal returnere med de ordene jeg kan lage med ordet letters

    #jeg starter med å iterere over hver linje i content 
    for line in content:
        #jeg lager en midlertidig letters, som gjør at hvis en bokstav stemmer så fjerner jeg den
        #slik jeg ikke kan sjekke en bokstav med den flere ganger
        temp_letters=list(letters)
        valid_word=True #Antar ordet i content er et gyldig ord

        #må itere over hver karakter i linjen 
        for char in line:
            #må sjekke om karakteren i line er i temp_letters
            if char in temp_letters:
                temp_letters.remove(char)
            else:
                valid_word=False #hvis bokstaven ikke finnes har vi et ugyldig ord
                break #og da må ma jo stoppe løkken
        
        #hvis ordet er gyldig legger vi det til i listen vi skal returnere
        #denne må være innenfor den ytterste løkken siden vi vil gjøre sjekken for hver iterasjon
        if valid_word:
            best_list.append(line)
    return best_list
    


def test_possible_words_from_file():
    print('Tester possible_words_from_file... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file('nsf2022.txt', 'hund'))

     #Ekstra test for varianten hvor det er wildcard i bokstavene
    #assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
          #   == possible_words_from_file('Koder/Laber/lab6/nsf2022.txt', 'c*'))
    print('OK')

if __name__ == '__main__':
    test_possible_words_from_file()
    #path='Koder/Laber/lab6/nsf2022.txt'
    #letters='hund'
    #possible_words_from_file(path, letters)

