import unittest
from kata_solved.lastdigit.last_digit import last_digit


class MyTestCase(unittest.TestCase):
    def test_small(self):
        test_data = [
            ([], 1),
            ([0, 0], 1),
            ([0, 0, 0], 0),
            ([1, 2], 1),
            ([3, 4, 5], 1),
            ([4, 3, 6], 4),
            ([7, 6, 21], 1),
            ([12, 30, 21], 6),
            ([2, 2, 2, 0], 4)]
        for test_input, test_output in test_data:
            self.assertEqual(last_digit(test_input), test_output)

    def test_medium(self):
        test_data = [
            ([937640, 767456, 981242], 0),
            ([123232, 694022, 140249], 6),
            ([499942, 898102, 846073], 6)]
        for test_input, test_output in test_data:
            self.assertEqual(last_digit(test_input), test_output)

    def test_big(self):
        test_data = [
            ([818278, 360080, 102165, 248891], 6),
            ([818278, 360080, 102165, 248891, 427700], 6),
            ([818278, 360080, 102165, 248891, 427700, 123514, 682563, 394199], 6),
            ([818278, 360080, 102165, 248891, 427700, 123514, 682563, 394199, 257250, 428607], 6),
            ([2, 2, 0, 2, 2, 1, 0, 0, 2, 0], 2),
            ([0, 1, 0, 2, 1, 0, 0, 2, 0, 0], 0)]
        for test_input, test_output in test_data:
            self.assertEqual(last_digit(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
