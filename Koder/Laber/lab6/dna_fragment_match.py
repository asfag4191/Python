#skal aldri utfor, så må sjekke antall i slik at enden av sequence ikke kommer utfor genome

def best_alignment(genome, sequence):
    least_diff=float('inf') #uendelig høy least_diff, lettere å sammenligne
    best_start=0
    for k in range(len(genome)-len(sequence)+1): #range teller fra 0 til n-1, så må plusse på 1.
        diff = alignment_difference(genome, sequence, k) #kaller på hjelpefunksjonen, teller hvem som har mest forskjell
        if diff<least_diff:
            least_diff=diff
            best_start=k
    return best_start
            



def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    sequence = 'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, sequence)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    sequence =                     'CCGGGGATGT'
    assert 22 == best_alignment(genome, sequence)

    genome = 'TTTAAG'
    sequence = 'AAGT'
    assert 2 == best_alignment(genome, sequence)
    print(' OK')


def alignment_difference(genome, sequence, i):
    different_pos=0
    for n in range(len(sequence)): #iterer over lengden til sequence. 
        #if i+n>=len(genome): #sjekker at i+n ikke overskrider genome, sjekker for hver enkelt n.
           # return -1
        if genome[i+n]!=sequence[n]: ##tilsvarende posisjon i genome. 
            different_pos+=1
    return different_pos

#feil å skrive if genome[n] != sequence[n]
#genome[n] sammenligner fra start av genome hver gang. Skal sammenligne fra plass i. 

def test_aligment_difference():
    print('Testing alignment_difference...', end='')
    genome = 'AAACCC'
    sequence = 'ACC'
    assert 2 == alignment_difference(genome, sequence, 0)
    assert 1 == alignment_difference(genome, sequence, 1)
    assert 0 == alignment_difference(genome, sequence, 2)
    assert 1 == alignment_difference(genome, sequence, 3)
    #assert -1 == alignment_difference(genome, sequence,4)
    print(' OK')


def best_alignment_to_file(path,sequence):
    path='human_genome_excerpt.txt'
    with open(path, 'rt', encoding='utf-8' ) as fileobj:
        target=fileobj.read()
    return best_alignment(target, sequence) #må huske å returnere resultatet

    
def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

if __name__ == '__main__':
    #genome = 'AAACCC'
    #sequence = 'ACC'
    #i=1
    #alignment_difference(genome, sequence, i)
    test_aligment_difference()
    test_best_alignment()
    test_best_alignment_to_file()

