def good_style(source_code):
    source=str(source_code) #sikrer en streng
    source=source.splitlines() #deler opp i linjer

    for char in source: 
        if len(char)>79:
            return False
    else:
        return True #setter return til slutt, for dette vil stoppe løkken 
    #tar den til slutt for å sjekke at alle linjene blir kjørt ut 
    


def test_good_style():
    print('Tester good_style... ', end='')
    assert good_style('''\
def distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
''') is True
    assert good_style((('x' * 79) + '\n') * 20) is True
    assert good_style('x' * 80) is False
    assert good_style(
          (('x' * 79) + '\n') * 5
        + (('x' * 80) + '\n')
        + (('x' * 79) + '\n') * 5
    ) is False
    print('OK')



def good_style_from_file(filename):
    with open(filename, 'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
        #content=str(content)
    return good_style(content)


def test_good_style_from_file():
    print('Tester good_style_from_file... ', end='')
    assert good_style_from_file('test_file1.py') is True
    assert good_style_from_file('test_file2.py') is False
    assert good_style_from_file('test_file3.py') is False
    assert good_style_from_file('nice_style.py') is True
    print('OK')



if __name__ == '__main__':
    test_good_style()
    test_good_style_from_file()
