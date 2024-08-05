from django.test import SimpleTestCase
from app import calc


class CalcTestcase(SimpleTestCase):
    def test_add_numbers(self):
        """" Add two number test """
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """" Subtract two number test """
        res = calc.subtract(10, 6)
        self.assertEqual(res, 4)
