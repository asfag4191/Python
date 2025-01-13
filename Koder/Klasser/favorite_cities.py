class City:
    def __init__(self, name, country, population, landmark):
        self.name = name
        self.country = country
        self.population = population
        self.landmark = landmark

# Creating different City objects
stavanger = City('Stavanger', 'Norge', 10000, ['Kyst', 'Kirke'])
oslo = City('Oslo', 'Norge', 700000, ['Opera House', 'Vigeland Park'])
bergen = City('Bergen', 'Norge', 280000, ['Bryggen', 'Mount Fløyen'])

# Print details of each city
print(vars(stavanger))  
print(vars(oslo))      
print(vars(bergen))   

