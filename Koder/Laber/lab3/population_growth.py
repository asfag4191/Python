#1. Leser inn tre tall
#2. For hvert år skal programmet skrive ut estimatet av de nye befolkningstørrelsen, rundet ned til nærmeste heltall.
#3. Til slutt skal programmet skrive ut totalveksten av startbefolkningen i prosent med to desimalers nøyaktighet
# Må da bruke formel for vekstrate

#Definerer funksjonen
def population_growth(population, growth_rate, years): 
    print(f'Befolkning: {population}')
    print(f'Årlig vekstrate (i prosent): {growth_rate}')
    print(f'Antall år: {years}')
    start_population=population #start populasjonen
    growth_rate=growth_rate/100 
    for i in range(1,years+1):
        population+=int(population*growth_rate) #Oppdatere nye befolkningstørrelsen, viktig med int for å runde ned slik man får hele personer. 
        print(f'Befolkningen etter {i} år er {int(population)}')

    #Regner ut totalveksten
    final_growth=round(((population-start_population)/start_population)*100,2) #round for å få 2 desimaler
    print(f'Total vekst etter {years} år er (i prosent) {final_growth}')
    return final_growth,

#Hovedprogrammet, sikrer at koden kun kjøres direkte (kan ikke importeres som en modul)
if __name__ == '__main__':
    population = int(input('Befolkning: '))
    growth_rate = float(input('Årlig vekstrate (i prosent): '))
    years = int(input('Antall år: '))
    
    population_growth(population, growth_rate, years) #kaller funksjonen

    










