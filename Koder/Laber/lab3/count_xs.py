def count_xs(s):
    count=0
    for char in s:
        if char=='x':
            count+=1
    return count


def test_count_xs():
    print('Tester count_xs... ', end='')
    assert 0 == count_xs('foo bar hei')
    assert 1 == count_xs('x')
    assert 4 == count_xs('xxCoolDragonSlayer99xx')
    print('OK')

if __name__ == '__main__':
    test_count_xs()
