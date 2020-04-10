import unittest
from kata_solved.josephus.josephus_survivor import josephus_survivor


class MyTestCase(unittest.TestCase):
    def test_jos(self):
        self.assertEqual(josephus_survivor(7, 3), 4)
        self.assertEqual(josephus_survivor(11, 19), 10)
        self.assertEqual(josephus_survivor(1, 300), 1)
        self.assertEqual(josephus_survivor(14, 2), 13)
        self.assertEqual(josephus_survivor(100, 1), 100)
        self.assertEqual(josephus_survivor(3613, 2812), 3056)
        self.assertEqual(josephus_survivor(4743, 1986), 2820)


if __name__ == '__main__':
    unittest.main()
