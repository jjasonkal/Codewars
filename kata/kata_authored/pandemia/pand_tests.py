import unittest
from kata_authored.pandemia.pand import infected


class MyTestCase(unittest.TestCase):
    def test_ip(self):
        map1 = "01000000X000X011X0X"
        self.assertAlmostEqual(infected(map1), 73.33333333333333)
        map2 = "01X000X010X011XX"
        self.assertAlmostEqual(infected(map2), 72.72727272727273)
        map3 = "XXXXX"
        self.assertAlmostEqual(infected(map3), 0)
        map4 = "0000000010"
        self.assertAlmostEqual(infected(map4), 100)
        map5 = "X00X000000X10X0100"
        self.assertAlmostEqual(infected(map5), 42.857142857142854)
        map6 = "00000X0X0000000000000100X0000X0000000001000010X00000X001X01X00010000XX0001100000X0X00X0000"
        self.assertAlmostEqual(infected(map6), 71.42857142857143)


if __name__ == '__main__':
    unittest.main()
