befolkning=(int(input('Befolkning: ')))
vekstrate=(float(input('Årlig vekstrate (i prosent): ')))
vekstrate=vekstrate/100 #må omgjør vekstrate til prosent
år=(int(input('Antall år: ')))

#oppretter liste slik jeg kan regne ut hvor stor vekst det er
#ved å hente ut via indeks fra listen.
befolkning_list=[]
befolkning_list.append(befolkning) #legger til veksten før vi starter å regne

for i in range(1,år+1): #inkluderer det siste åre
    befolkning+=befolkning*vekstrate #regner ut veksten
    befolkning=int(befolkning) #runder befolkningen med int

    befolkning_list.append(befolkning) #legger til for hver iterasjon befolkningen i list
    print(f'Befolkningen etter {i} år er {befolkning}') #printer i hver løkke

siste=befolkning_list[-1]
#print(siste)
første=befolkning_list[0]
#print(første)
#prosent andel for å beregne veksten
#når vi bruker round, vil vi avrude til slutt. 
total=round(((siste - første) / første) * 100, 2) #hvordan regne vekst!
print(f'Total vekst etter {år} år er (i prosent) {total}')