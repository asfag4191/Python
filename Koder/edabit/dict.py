#Luke Skywalker has family and friends. Help him remind them who is who. 
# Given a string with a name, return the relation of that person to Luke.

def relation_to_luke(name):
    #creating a dictianory
    relations={
        'Darth Vader':'father',
        'Leia':'sister',
        'Han':'brother in law',
        'R2D2':'droid'
        }
    
    return 'Luke, I am your ' + relations[name] + '.'

print(relation_to_luke('Darth Vader'))

import unittest

class TestRelationToLuke(unittest.TestCase):
    def test_relation_to_luke(self):
        self.assertEqual(relation_to_luke("Darth Vader"), "Luke, I am your father.")
        self.assertEqual(relation_to_luke("Leia"), "Luke, I am your sister.")
        self.assertEqual(relation_to_luke("Han"), "Luke, I am your brother in law.")
        self.assertEqual(relation_to_luke("R2D2"), "Luke, I am your droid.")

if __name__ == "__main__":
    unittest.main()

# Author : Jeroen Ndh