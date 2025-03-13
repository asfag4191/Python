funA_is_destructive = True
funA_description = 'Destruktiv siden vi henter inn en liste, og endrer direkte i listen, altså fjerner alle tall som er 3' # Skriv din forklaring inne i strengen

funB_is_destructive = False
funB_description = '''Ikke destruktiv siden vi henter inn en liste a, og oppretter to tomme. Iterer over a, og sjekker for hver iterasjon om
denne verdine er mindre enn 10, hvis den er det legges den til i den nye listen, a forblir uendret. '''

funC_is_destructive = True
funC_description = '''Destruktiv, iterer over lengden på listen, men henter deretter ut på indeks i listen a, og tilordner denne en ny variabel
endrer den opprinnelige listen, ingen kopi'''

funD_is_destructive = False
funD_description = 'Ikke destruktiv'

funE_is_destructive = True
funE_description = 'Destruktiv, bruker pop, fjerner element på en spesifik posisjon fra listen a.'

funF_is_destructive = False
funF_description = 'Ikke destruktiv, bruker a som en sjekk og fyller opp mi=None, den har ikke noe konkret verdi'


def funE(a):
    mi = None
    for x in a:
        if mi is None or x < mi:
            mi = x
    return mi #må ha en retur verdi hvis vi skal få ut den minste verdien

#a=(1,2,3,4)
#print(funE(a))
