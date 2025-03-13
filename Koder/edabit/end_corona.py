#vet ikke hvor lenge løkken vil vare, men vil vare så lenge active_cases er større enn 0 
def end_corona(recovers, new_cases, active_cases):
    #to round up 
    day=0
    while active_cases>0:
        active_cases+=new_cases-recovers
        day+=1
    return day


def end_corona_test():
    assert end_corona(4000, 2000, 77000) == 39
    assert end_corona(3000, 2000, 50699) == 51
    assert end_corona(30000, 25000, 390205) == 79
    assert end_corona(260000, 255000, 20511691) == 4103
    print('OK')

if __name__ == '__main__':
    end_corona_test()
