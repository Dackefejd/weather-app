import unittest
from weather import celsius_to_fahrenheit

class TestWeather(unittest.TestCase):
    def test_conversion(self):
        # 0 C är 32 F
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # 100 C är 212 F
        self.assertEqual(celsius_to_fahrenheit(100), 212)

if __name__ == '__main__':
    unittest.main()