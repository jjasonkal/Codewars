import unittest
from kata_solved.Rot13.rot13 import rot13


class MyTestCase(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot13("test"), "grfg")
        self.assertEqual(rot13("Test"), "Grfg")
        self.assertEqual(rot13("Codewars"), 'Pbqrjnef')
        self.assertEqual(rot13("10+2 is twelve."), '10+2 vf gjryir.')


if __name__ == '__main__':
    unittest.main()
