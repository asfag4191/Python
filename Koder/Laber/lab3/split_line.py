#Starts in x_lo and ends in x_hi, split up in n. Want to know where i starts and ends. 
#Return star- and endpoint for i, when split up in n.

def get_endpoints(i,n,x_lo,x_hi):
    l_tot=x_hi-x_lo # Den totale lengden av linjestykket
    l_bit=l_tot/n # Lengden på hver bit
    xi_lo=x_lo+i*l_bit # Startpunktet (nedre grense) for bit nummer i
    xi_hi=xi_lo+l_bit  # Sluttpunktet (øvre grense) for bit nummer i
    return (xi_lo, xi_hi) # Returnerer start- og sluttpunktet for bit i



#Del B

if __name__ == '__main__':
    #Brukerinput
    x_lo= float(input())
    x_hi= float(input())
    n=int(input())

    print(f'x_lo={x_lo}\nx_hi={x_hi}\nn={n}')

    for i in range(n): #Bruker kun n, siden det er antall biter vi iterer over. 
        xi_lo, xi_hi = get_endpoints(i, n, x_lo, x_hi) 
        # Beregner start- og sluttpunktene for den nåværende biten (i) vi er på.
        # Når i=0, beregnes start- og sluttpunktet for den første biten.
        # Deretter fortsetter i=1, i=2, ..., helt til vi har beregnet alle n bitene.
        # Verdien av i øker med én for hver iterasjon.
        print(f'{xi_lo} {xi_hi}')


