#Write a function that takes an integer minutes and converts it to seconds.
import unittest

def minutes_to_seconds(x):
    return x*60


class TestMinutesToSeconds(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(minutes_to_seconds(6), 360)
        self.assertEqual(minutes_to_seconds(4), 240)
        self.assertEqual(minutes_to_seconds(8), 480)
        self.assertEqual(minutes_to_seconds(60), 3600)

if __name__ == '__main__':
    unittest.main()

