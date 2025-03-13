
def curzon_number(num):
    if ((2**num)+1)%(2*num+1)==0:
        return True
    else:
        return False
    


def test_curzon_number():
    assert(curzon_number(5), True)
    assert(curzon_number(10), False)
    assert(curzon_number(14), True)
    assert(curzon_number(86), True)
    assert(curzon_number(90), True)
    assert(curzon_number(115), False)
    assert(curzon_number(120), False)
    assert(curzon_number(194), True)
    assert(curzon_number(293), True)
    print('OK')

if __name__ == '__main__':
    test_curzon_number()