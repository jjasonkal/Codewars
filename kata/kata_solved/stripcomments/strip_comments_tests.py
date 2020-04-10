import unittest
from kata_solved.stripcomments.strip_comments import solution


class MyTestCase(unittest.TestCase):
    def test_comments(self):
        self.assertEqual(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
        self.assertEqual(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
        self.assertEqual(solution('lemons watermelons oranges apples pears\napples apples pears lemons avocados\nstrawberries # !\n- apples\nbananas bananas oranges avocados ?', ['@']), 'lemons watermelons oranges apples pears\napples apples pears lemons avocados\nstrawberries # !\n- apples\nbananas bananas oranges avocados ?')
        self.assertEqual(solution("#", ['#', '!']), "")


if __name__ == '__main__':
    unittest.main()
