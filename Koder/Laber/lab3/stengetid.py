def get_hour(time_string):
    return int(time_string.split(":")[0])

closing_hour = 20
current_hour = 0
customers = 0 

while not (customers == 0 and current_hour >= closing_hour):  
    time_string = input("Kva er klokka? (Format HH:MM, for eksempel 20:00)\n")
    current_hour = get_hour(time_string)
    customers = int(input("Kor mange kundar er i butikken?\n"))

print("Du kan låse døra og gå heim. Jippi!")

