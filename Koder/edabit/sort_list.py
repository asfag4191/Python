
def asc_des_none(lst, s):
#asc returnerer liste i stigende rekkefølge
    if s=="Asc":
        lst.sort() #sorter listen på plass
        return lst #returnerer den sorterte lsiten
    #returnerer i synkende rekkefølge.
    elif s=="Des":
        lst.sort(reverse=True)
        return lst
    else:
        return lst
    
print(asc_des_none([7, 8, 11, 66], "Des"))


    
