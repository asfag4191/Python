class Resturant:
  name = '' #string
  category = '' #string
  rating = 0.0 #float
  delivery = True #bool

#creating an object
bobs_burgers=Resturant()

#access and edit attributes

bobs_burgers.name='Bob\'s Burgers'
bobs_burgers.category='American Diner'
bobs_burgers.rating=4.7
bobs_burgers.delivery=False

#Can chech all attributes with vars()

print(vars(bobs_burgers))

#Can give all the attributes in a single line
#self representthe object we create out of the class when on a line
class Student: 
  def __init__(self, name, year, gpa, enrolled):
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)

print(vars(daniel))
