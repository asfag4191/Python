
#tar inn en fil og returnerer et oppslagsverk
def get_word_count(path):
    with open(path,'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
        content=content.split(' ') #splitter basert på mellomrom
    #tomt oppslagsverk 
    dict={}
    for i in range(len(content)): #iterer gjennom filen
        content[i]=content[i].lower().strip(",.!?") #strip fjerner spesifikke tegn
        if content[i] not in dict: 
            dict[content[i]]=1
        else:
            dict[content[i]]+=1
    return dict
    

def test_get_word_count():
    print('Tester get_word_count... ', end='')
    expected = {
        'det': 1,
        'var': 3,
        'en': 2,
        'katt': 2,
        'som': 1,
        'het': 1,
        'pusur': 3,
        'snill': 1
    }
    actual = get_word_count('Koder/Laber/lab6/pusur.txt')
    assert(actual == expected)
    print('OK')

#B

#fjerner det mest vanlige ordet. 
def pop_most_common_word(word_count):
    max_word=0
    word_b=""
    for word in word_count:
        if word_count[word]>max_word: #må hente ut verdien til nøkkelen og sjekke
            max_word=word_count[word] #oppdaterer hvis dette holder
            word_b=word #legger til i den strengen vi vil returnere som beste ord
        elif word_count[word]==max_word and word<word_b: #Sjekker alfabetisk rekkefølge
            word_b=word #oppdaterer til ordet som kommer først
    else:
        word_count.pop(word_b) #fjerner den mest vanlige nøkkelen (dette ville returnert verdi),
        #men det gjør vi ikke her, returner ikke noe
    return word_b #returnerer kun det beste ordet

def test_pop_most_common_word():
    print('Tester pop_most_common_word... ', end='')
    my_word_count = {
        'som': 1,
        'pusur': 3,
        'var': 3,
        'katt': 2,
        'het': 1,
        'snill': 1,
        'en': 2,
        'det': 1
    }

    # Test 1
    expected = 'pusur'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'pusur' not in my_word_count, "'pusur' fortsatt her etter test 1"

    # Test 2
    expected = 'var'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'var' not in my_word_count, "'var' fortsatt her etter test 2"

    # Test 3
    expected = 'en'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'en' not in my_word_count, "'en' fortsatt her etter test 3"

    print('OK')


#C

#returnere de n mest vanlige ordene
def n_common_words (word_count, n):
    best_words=[] #plassholder for ordene
    #iterere n ganger, slik man kaller n ganger på forrige funksjon
    for _ in range(n):
        best_word = pop_most_common_word(word_count)  # Finn og fjern det mest vanlige ordet
        best_words.append(best_word)
    return best_words
        
    


def test_n_common_words():
    print('Tester n_common_words... ', end='')
    my_word_count = {
        'som': 1,
        'pusur': 3,
        'var': 3,
        'katt': 2,
        'het': 1,
        'snill': 1,
        'en': 2,
        'det': 1
    }

    # Test 1
    expected = ['pusur', 'var']
    # Vi bruker en kopi (lages med dict()) for å unngå mutasjon
    actual = n_common_words(dict(my_word_count), 2) 
    assert actual == expected

    # Test 2
    expected = ['pusur', 'var', 'en', 'katt', 'det', 'het', 'snill', 'som']
    actual = n_common_words(dict(my_word_count), 8)
    assert actual == expected

    print('OK')
    

#D

#Slår sammen funksjonene
def common_words(path,n):
    word_count=get_word_count(path)
    best_words=n_common_words (word_count, n)
    return best_words

def test_common_words():
    print('Tester common_words... ', end='')
    # Test 1
    expected = ['pusur', 'var']
    actual = common_words('Koder/Laber/lab6/pusur.txt', 2)
    assert actual == expected

    # Test 2
    expected = ['pusur', 'var', 'en', 'katt', 'det', 'het', 'snill', 'som']
    actual = common_words('Koder/Laber/lab6/pusur.txt', 8)
    assert actual == expected

    print('OK')


if __name__=='__main__':
    path='Koder/Laber/lab6/pusur.txt'
    get_word_count(path)
    test_get_word_count()
    test_pop_most_common_word()
    test_n_common_words()
    test_common_words()
    

    word_count = {
    'som': 1,
    'pusur': 3,
    'var': 3,
    'katt': 2,
    'het': 1,
    'snill': 1,
    'en': 2,
    'det': 1
}
    n=2
    
    n_common_words (word_count, n)
    #pop_most_common_word(my_word_count)
    