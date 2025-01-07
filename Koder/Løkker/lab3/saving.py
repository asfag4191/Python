#Returnere antall måneder det tar å spare opp nok egenkapital, 0.25 av total kostnad. 
#Etter hver måned utbetalt r/12 renter. Har en årlig rente på 0.04
def saving(annual_salary, savings, total_cost):
    equity_capital=0.25*total_cost #Egenkapitalen man må ha
    monthly_savings=(annual_salary/12)*(savings/100) #Hvor mye som blir spart i måneden
    month_count=0 #Teller måneder
    total_savings=0 #hva som er totalt spart, starter med 0kr spart. 

    while total_savings<equity_capital:
        total_savings += monthly_savings  # Legger til månedlig sparing
        total_savings += total_savings * (0.04 / 12)  # Legger til månedlig rente
        #må ha to linjer slik at rentene regnes ut korrekt på det oppdaterte beløpet. 
        month_count+=1
    return month_count
    
print("Tester saving... ", end="")
assert saving(500000, 20, 3000000) == 79
assert saving(900000, 10, 5000000) == 133
print("OK")



