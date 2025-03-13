def get_endpoints(i, n, x_lo, x_hi):
    i=int(i)
    n=int(n)
    x_lo=float(x_lo)
    x_hi=float(x_hi)

    length=x_hi-x_lo
    length_bit=length/n
    xi_lo=x_lo+i*length_bit #nedre grense
    xi_hi=xi_lo+length_bit #øvre grense
    
    return xi_lo,xi_hi


def almost_equals(a, b):
    return abs(a - b) < 0.0000000001

print('Testing get_endpoints... ', end='')
start, end = get_endpoints(1, 4, 50.0, 150.0)
assert almost_equals(75, start)
assert almost_equals(100, end)

start, end = get_endpoints(3, 4, 50.0, 150.0)
assert almost_equals(125, start)
assert almost_equals(150, end)

start, end = get_endpoints(0, 3, -30, 60)
assert almost_equals(-30, start)
assert almost_equals(0, end)
print('OK')

if __name__ == '__main__':
    x_lo=float(input('x_lo = '))
    x_hi=float(input('x_hi = '))
    n=int(input('n = '))
    #skal beregne start og sluttpunkt for hver del i,
    #deler inn i n deler
    for i in range(n):
        xi_lo, xi_hi = get_endpoints(i, n, x_lo, x_hi) 
        #sender xi_lo og xi_hi som parametere siden
        #funksjonen returnerer disse punktene.
        #sender med funkjsonen, siden er dette som 
        #blir brukt til å regne. 
        print(xi_lo, xi_hi)
