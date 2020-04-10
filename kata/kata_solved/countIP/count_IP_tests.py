import unittest
from kata_solved.countIP.count_IP import ips_between


class MyTestCase(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)
        self.assertEqual(ips_between("113.236.231.108", "114.2.5.71"), 1383899)
        self.assertEqual(ips_between("165.204.219.41", "166.2.180.133"), 3529052)
        self.assertEqual(ips_between("2.151.173.55", "2.152.121.170"), 52339)


if __name__ == '__main__':
    unittest.main()
