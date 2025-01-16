def is_leap_year(year):
    if year%4==0 and year%100!=0:
        return True
    if year%100==0 and year%400==0:
        return True
    else:
        return False

def main():
    user=is_leap_year(user_year)
    if user==True:
        print(f'{user_year} er et skuddår')
    else:
        print(f'{user_year} er ikke et skuddår')
    
    

if __name__ == "__main__":
    user_year=(int(input("Skriv inn ett årstall:\n")))
    main()


