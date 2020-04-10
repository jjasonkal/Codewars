import unittest
from kata_solved.extractDomainName.domain import domain_name


class MyTestCase(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("http://www.hsw3d2rcycgth50t6e7xgvlx4j.co.za/img/"), "hsw3d2rcycgth50t6e7xgvlx4j")
        self.assertEqual(domain_name("r1qnkdyyqejwz0jlstwrj.org/error"), "r1qnkdyyqejwz0jlstwrj")


if __name__ == '__main__':
    unittest.main()
