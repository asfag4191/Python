
#library er oppslagsverket, og book er en nøkkel som får verdien
#etter hvor mange av denne boken som finnes i oppslagsverket. 
def add_book (library,book):
    if book in library:
        library[book]+=1
    else:
        library[book]=1

def test_add_book():
    print('Tester add_book... ', end='')
    my_library = {
        'The Little Prince': 4,
        'The Hobbit': 2,
        'Norwegian Wood': 1
    }
    add_book(my_library, 'The Hobbit')
    add_book(my_library, 'Peter Pan')

    assert 3 == my_library['The Hobbit'], (
        f"Forventet 3 stk 'The Hobbit' men fant {my_library['The Hobbit']}"
    )
    assert 'Peter Pan' in my_library, "'Peter Pan' mangler i biblioteket"
    assert 1 == my_library['Peter Pan'], (
        f"Forventet 1 stk 'Peter Pan' men fant {my_library['Peter Pan']}"
    )
    print('OK')




def remove_book(library, book):
    #hvis boken finnes så fortsetter vi, viktig å sjekke dette først
    if book in library and library[book] >0:
        library[book]-=1
        #hvis antallet på boken er 0 etter reduksjon så fjerner vi den
        #vi gjør dette med et innrykk siden vi må iterere over dictinariet. 
        if library[book]==0:
            library.pop(book)

def test_remove_book():
    print('Tester remove_book... ', end='')
    my_library = {
        'Black Beauty': 1,
        'The Train': 5,
        'Fireworks in Winter': 3
    }
    remove_book(my_library, 'The Train')
    remove_book(my_library, 'The Train')
    remove_book(my_library, 'Black Beauty')

    assert 'The Train' in my_library, (
        "Forventet ikke at 'The Train' skulle forsvinne fra biblioteket"
    )
    assert 3 == my_library["The Train"], (
        f"Forventet 3 stk 'The Train' men fant {my_library['The Train']}"
    )
    assert 'Black Beauty' not in my_library, (
        "Forventet ikke at 'Black Beauty' fortsatt er i biblioteket"
    )
    # Sjekker at programmet ikke krasjer hvis vi prøver å fjerne en bok 
    # som ikke finnes i biblioteket
    remove_book(my_library, 'Black Beauty')
    print('OK')


#iterer over både nøkler og verdier, og henter ut verdier for
#hver nøkkel (bok)
def total_books(library):
    total_count=0
    for key in library:
        value=library[key]
        total_count+=value
    return total_count

def test_total_books():
    print('Tester total_books... ', end='')
    my_library = {
        'Apothecary Diaries Volume 1': 3,
        'Apothecary Diaries Volume 2': 200,
        'Apothecary Diaries Volume 3': 1,
        'Apothecary Diaries Volume 4': 0,
    }

    expected = 204
    actual = total_books(my_library)
    assert expected == actual, f'{expected=},  {actual=}'
    my_library['Apothecary Diaries Volume 4'] += 10

    expected = 214
    actual = total_books(my_library)
    assert expected == actual, f'{expected=},  {actual=}'

    print('OK')



if __name__ == '__main__':
    test_add_book()
    test_remove_book()
    test_total_books()



