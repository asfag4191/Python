def dis(price,discount):
    discount_p=discount/100
    price_p=price*discount_p
    final=price-price_p
    return round(final,2)


def test():
    assert dis(100, 75) == 25
    assert dis(211, 50) == 105.5
    assert dis(593, 61) == 231.27
    assert dis(1693, 80) == 338.6
    assert dis(700, 10) == 630
    print('OK')

if __name__ == "__main__":
    test()