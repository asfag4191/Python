
#Årslønn, Prosentandel av lønnen som skal spare, 
#Totalkostnaden for drømmeboligen.

#Tjener 0.04 årlig på penger spart
def saving(yearly_salary, savings, total_cost):
    monthly_salary=(yearly_salary/12) #måneder
    savings=savings/100 #prosent
    ek=total_cost*0.25 #hva jeg må spare, egenkapital
    montly_r=0.04/12 #penger spart er denne renten

    money_saved=0
    month=0

    #kjører så lenge true, altså helt til money_saved er ikke mindre enn ek.
    while money_saved<ek:
        money_saved+=monthly_salary*savings #sparing
        money_saved+=money_saved*montly_r #renter på sparing
        month+=1

    return month
    
print("Tester saving... ", end="")
assert saving(500000, 20, 3000000) == 79
assert saving(900000, 10, 5000000) == 133
print("OK")


