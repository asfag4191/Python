def area_triangle(base,height):
    return (base*height)/2


import unittest

class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area_triangle(3, 2), 3)
        self.assertEqual(area_triangle(5, 4), 10)
        self.assertEqual(area_triangle(10, 10), 50)
        self.assertEqual(area_triangle(0, 60), 0)
        self.assertEqual(area_triangle(12, 11), 66)

if __name__ == "__main__":
    unittest.main()