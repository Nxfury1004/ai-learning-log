import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        """Test that city_country() returns a correctly formatted string."""
        formatted_string = city_country('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_cyprus(self):
        """Test that city_country() returns a correctly formatted string."""
        formatted_string = city_country('nicosia', 'cyprus')
        self.assertEqual(formatted_string, 'Nicosia, Cyprus')


if __name__ == '__main__':
    unittest.main()