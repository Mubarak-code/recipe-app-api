from django.test import SimpleTestCase
from app import calc


class CalcTestcase(SimpleTestCase):
    def test_add_numbers(self):
        """" Add two number test """
        res = calc.add(2, 3)
        self.assertEqual(res, 5)
