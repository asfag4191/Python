def visible_light(unit,value):
    if unit=='THz':
        if value not in range(400,790):
            print(f'\n{value} thz er utenfor det synlige spekteret.')

        f=value*(10**12) #Skriver om til Hz
        value = int((3 * 10**8) / f * (10**9)) #regner om til nm, range fungerer kun med heltall!
        

    if unit=='nm' and value not in range(380,751):
            print(f'\n{value} nm er utenfor det synlige spekteret.')
            
    #vi kjører if, elif for begge unitene, etterom vi har gjort om value fra THz til nm. 
    if value in range(380,450):
        print('\nViolet')
    elif value in range(450,485):
        print('\nBlue')
    elif value in range(485,500):
        print('\nCyan')
    elif value in range(500,565):
        print('\nGreen')
    elif value in range(565,590):
        print('\nYellow')
    elif value in range(590,625):
        print('\nOrange')
    elif value in range(625,750):
        print('\nRed')

if __name__ == '__main__':
    unit=str(input("Angi enhet (nm eller THz):\n"))
    #må avslutte med en gang, hvis input ikke er det vi ønsker
    if unit!='nm' and unit!='THz':
            print(f'Enheten må være i nm eller THz, det kan ikke være {unit}.')
    else:
         value=int(input(f"Angi verdi i {unit}:\n"))
         visible_light=visible_light(unit,value)


#når man kjører if setninger, går den gjennom alle if setningene, elif avslutter når den finner den som er sann. 