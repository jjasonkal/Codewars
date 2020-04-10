import unittest
from kata_solved.diamond.diam import diamond


class MyTestCase(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(diamond(1), "*\n")
        self.assertEqual(diamond(2), None)
        self.assertEqual(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        self.assertEqual(diamond(11), '     *\n    ***\n   *****\n  *******\n *********\n***********\n *********\n  *******\n   *****\n    ***\n     *\n')


if __name__ == '__main__':
    unittest.main()
