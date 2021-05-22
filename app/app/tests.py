from django.test import TestCase

from app.calc import add_numbers, subtract


class CalcTest(TestCase):

    def test_add_numbers(self) -> None:
        """
        Test for add two numbers function
        """
        self.assertEqual(add_numbers(1, 4), 5)

    def test_subtract_numbers(self) -> None:
        """
        Test for subtract values
        """
        self.assertEqual(subtract(5, 11), 6)
