import unittest
from kata_solved.trailingzeros.trailing0s import zeros


class MyTestCase(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(zeros(0), 0, "Testing with n = 0")
        self.assertEqual(zeros(6), 1, "Testing with n = 6")
        self.assertEqual(zeros(30), 7, "Testing with n = 30")
        self.assertEqual(zeros(1000), 249, "Testing with n = 1000")
        self.assertEqual(zeros(100000), 24999, "Testing with n = 100000")
        self.assertEqual(zeros(463432478), 115858112, "Testing with n = 463432478")


if __name__ == '__main__':
    unittest.main()
