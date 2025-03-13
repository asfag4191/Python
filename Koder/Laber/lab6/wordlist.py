def filter_wordlist(path, search_string):
    with open(path, 'rt', encoding='utf-8') as fileobj:
        content = fileobj.read().splitlines()

    words = []
    for char in content:
        if search_string in char: #skal bare sjekke om strengen er en del av ordet, ikke likt. 
            #hvis dette er sant så blir ordet lagt til i listen
            words.append(char)
    
    return words

def test_filter_wordlist():
    print('Testing filter_wordlist... ', end='')

    # Test 1
    expected = ['database', 'baser']
    actual = filter_wordlist('Koder/Laber/lab6/sample.txt', 'base')
    assert expected == actual, f"Test 1 failed: {expected} != {actual}"

    # Test 2
    expected = [
        'småstad', 'småstaden', 'småstas', 'småstasen', 'småstat', 'småstaten',
        'småstatene', 'småstater',
    ]
    actual = filter_wordlist('Koder/Laber/lab6/nsf2022.txt', 'småsta')
    assert expected == actual, f"Test 2 failed: {expected} != {actual}"

    # Test 3
    expected = [
        'stjerneskudd', 'stjerneskudda', 'stjerneskuddene', 'stjerneskuddet',
    ]
    actual = filter_wordlist('Koder/Laber/lab6/nsf2022.txt', 'stjerneskudd')
    assert expected == actual, f"Test 3 failed: {expected} != {actual}"

    print('OK')

if __name__ == '__main__':
    test_filter_wordlist()
