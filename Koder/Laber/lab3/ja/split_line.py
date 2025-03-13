def get_endpoints(i, n, x_lo, x_hi):
    length = x_hi - x_lo
    length_bit = length / n
    xi_lo = x_lo + i * length_bit  # Nedre grense
    xi_hi = xi_lo + length_bit  # Øvre grense
    return xi_lo, xi_hi  # Returnerer start- og sluttpunktet for bit i

if __name__ == '__main__':
    x_lo = float(input())  
    x_hi = float(input())  
    n = int(input())  

    print(f'x_lo= ')
    print(f'x_hi= ')
    print(f'n= ')

    for i in range(n):
        xi_lo, xi_hi = get_endpoints(i, n, x_lo, x_hi)  
        print(f'{xi_lo} {xi_hi}')  # Sørger for at tallene skrives ut riktig


