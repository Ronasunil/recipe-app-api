from django.test import SimpleTestCase
from config.calc import add

class CalcTest (SimpleTestCase):

    def test_add(self):
        result = add(5,5)
        self.assertEqual(result, 10)

