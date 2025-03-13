#DEl A
def shopping_list_to_dict(shopping_list): 
    dict={} #oppretter et tomt dictionary
    #vil splitte strengen basert på linjer
    split_list=shopping_list.splitlines()
    #print(split_list)
    for line in split_list: #vil jo iterer gjennom hver rad i shipping list. 
        num, food_name=line.split(" ")
        dict[food_name]=int(num) #viktig at num ikke er en string
    #print (dict)
    return dict


def test_shopping_list_to_dict():
    print('Tester shopping_list_to_dict... ', end='')
    arg = '2 brød\n3 pizza\n10 poteter\n1 kaffe\n1 ost\n14 epler\n'
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 14,
    }
    actual = shopping_list_to_dict(arg)
    assert expected == actual
    print('OK')



#DEL B
def shopping_list_file_to_dict(path):
    #dict_txt={}
    with open(path,'rt', encoding='utf-8') as fileobj:
        content=fileobj.read()
        #content=content.splitlines() #deler opp at hver linje blir en streng
        #print(content)
    #for line in content:
       # num,food_name=line.split(" ") #henter ut de forskjellige tall og avn i en streng, basert på mellomrom
       # dict_txt[food_name]=int(num)
    #return dict_txt
    #kan kalle på forrige oppgave
    return shopping_list_to_dict(content) 




def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('Koder/Laber/lab6/handleliste.txt')
    assert expected == actual
    print('OK')

if __name__ == '__main__':
    #shopping_list='2 brød\n3 pizza\n10 poteter\n1 kaffe\n1 ost\n14 epler\n'
    #shopping_list_to_dict(shopping_list)
    test_shopping_list_to_dict()
    #path='Koder/Laber/lab6/handleliste.txt'
    #shopping_list_file_to_dict(path)
    test_shopping_list_file_to_dict()
