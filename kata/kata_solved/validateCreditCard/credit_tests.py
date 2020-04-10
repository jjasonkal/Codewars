import unittest
from kata_solved.validateCreditCard.credit import validate


class MyTestCase(unittest.TestCase):
    def test_credit(self):
        self.assertEqual(validate(123), False)
        self.assertEqual(validate(2121), True)
        self.assertEqual(validate(1230), True)
        self.assertEqual(validate(4111111111111111), True)
        self.assertEqual(validate(922030), False)


if __name__ == '__main__':
    unittest.main()
