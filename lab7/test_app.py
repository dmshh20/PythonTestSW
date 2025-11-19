import unittest
from random import choice, randint

from app import Figure

class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")

    def test_obj_invalid(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)  # недозволений тип -> AssertionError

if __name__ == '__main__':
    unittest.main()
