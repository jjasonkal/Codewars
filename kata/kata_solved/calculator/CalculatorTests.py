import unittest
from kata_solved.calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        test_data = [
            ('1.1 + 2.2 + 3.3', 6.6),
            ('2 + 3', 5),
            ('2 + 2 + 2 + 2', 8)]
        for test_input, test_output in test_data:
            self.assertEqual(Calculator().evaluate(test_input), test_output)

    def test_minus(self):
        test_data = [
            ('2 - 3 - 4', -5),
            ('2 - 3', -1),
            ('2 - 2 - 2 - 2', -4)]
        for test_input, test_output in test_data:
            self.assertEqual(Calculator().evaluate(test_input), test_output)

    def test_mul(self):
        test_data = [
            ('2 * 3 * 4', 24),
            ('2 * 2', 4),
            ('2 * 2 * 2 * 2', 16)]
        for test_input, test_output in test_data:
            self.assertEqual(Calculator().evaluate(test_input), test_output)

    def test_div(self):
        test_data = [
            ('2 / 4', 0.5),
            ('2 / 2', 1),
            ('2 / 2 / 2 / 2', 0.25)]
        for test_input, test_output in test_data:
            self.assertEqual(Calculator().evaluate(test_input), test_output)

    def test_complex(self):
        test_data = [
            ('2 + 3 * 4 / 3 - 6', 0),
            ('10 * 5 / 2', 25),
            ('1 / 2 * 4 + 2', 4),
            ('1 + 1 / 2 * 4 + 2 * 5', 13)]
        for test_input, test_output in test_data:
            self.assertEqual(Calculator().evaluate(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
