import unittest
from kata_authored.courier.cour import courier


class MyTestCase(unittest.TestCase):
    def test_ip(self):
        arr1 = ["s2", "s1", "w5", "w7"]
        self.assertEqual(courier(arr1, 2), 30)
        self.assertEqual(courier(arr1, 3), 30)
        self.assertEqual(courier(arr1, 4), 28)

        arr2 = ["w10", "e5", "n7", "s5", "s1", "w10"]
        self.assertEqual(courier(arr2, 2), 72)
        self.assertEqual(courier(arr2, 3), 70)

        # The example of the description
        arr3 = ["w3", "e5", "n7", "s2", "s1", "w5", "e7", "n13", "w6", "e2", "e4", "e1", "n9"]
        self.assertEqual(courier(arr3, 3), 96)
        self.assertEqual(courier(arr3, 5), 88)
        self.assertEqual(courier(arr3, 13), 84)
        self.assertEqual(courier(arr3, 16), 84)

        # empty array: minutes=0
        self.assertEqual(courier([], 10), 0)


if __name__ == '__main__':
    unittest.main()
