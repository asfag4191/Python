#sjekker om ordet word kan bli laget av strengen med letters
def can_be_made_of_letters(word, letters):
    for letter in word:  #iterer over hver bokstav i word
        if word.count(letter)>letters.count(letter): #word.counter(letter) teller hvor mange ganger letter (den bokstaven vi er på
            # i iterasjonen forekommer. Hvis den forekommer flere ganger i word enn i letters er dette en feil og vi returnerer False.
            return False #avbryter når vi finner en feil.
    else: #hvis det ikke er funnet noen problemer returnerer vi True
        return True



print(can_be_made_of_letters('halla', 'halaaaa'))

def test_can_be_made_of_letters():
    print('Tester can_be_made_of_letters... ', end='')
    assert can_be_made_of_letters('emoji', 'abcdefghijklmno') is True
    assert can_be_made_of_letters('smilefjes', 'abcdefghijklmnopqrs') is False
    assert can_be_made_of_letters('smilefjes', 'abcdeeefhijlmnopsss') is True
    assert can_be_made_of_letters('lese', 'esel') is True
    print('OK')

if __name__ == '__main__':
    test_can_be_made_of_letters()


#DELB
#liste med strenger og bokstvaer vi har
#returnere liste med alle ord fra wordlist som kan lages med bokstavene i letters
def possible_words(wordlist, letters):
    #sjekker ordene i wordlist om de kan bli laget med letters
    possible_word=[] #liste hvor vi legger de mulige ordene i
    for word in wordlist: #iterer over hvert ord i listen
        if can_be_made_of_letters(word,letters): #bruker funksjonen for å sjekke om vi kan lage dette ordet med letters, altså kaller på den tidligere
            #funksjonen med det nye ordet vi er på og de gitte bokstavene.
            possible_word.append(word) #legger til i en ny liste
    return possible_word
    
def test_possible_words():
    print('Tester possible_words... ', end='')
    hundsk =['tur', 'mat', 'kos', 'hent', 'sitt', 'dekk', 'voff']
    kattsk =['kos', 'mat', 'pus', 'mus', 'purr', 'mjau', 'hiss']
    assert(['kos', 'sitt'] == possible_words(hundsk, 'fikmopsttuv'))
    assert(['kos', 'pus', 'mus'] == possible_words(kattsk, 'fikmopsttuv'))
    print('OK')

if __name__ == '__main__':
    test_possible_words()
