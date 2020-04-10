import unittest
from kata_solved.intervalsum.sumofinterval import sum_of_intervals


class MyTestCase(unittest.TestCase):
    def test_small(self):
        test_data = [
            ([(1, 5)], 4),
            ([(1, 5), (6, 10)], 8),
            ([(1, 4), (7, 10), (3, 5)], 7),
            ([(-358, 313), (476, 488)], 683)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(sum_of_intervals(test_input), test_output)
    def test_large(self):
        test_data = [
            ([(192, 259), (466, 496), (-263, 92), (-25, 91), (-318, 448), (-202, 231)], 796),
            ([(-86, -30), (352, 438), (-456, 12), (-112, 459), (288, 326), (133, 165), (33, 354), (124, 376), (471, 485), (203, 249), (-377, 261), (246, 365), (184, 321), (445, 453), (377, 473), (-460, 3), (-62, 307)], 945),
            ([(-383, 300), (-273, 346), (-32, 376), (-226, 327), (-479, -213), (98, 338), (-119, 93), (497, 500), (-370, -279), (263, 464), (-321, -202), (381, 459)], 946)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(sum_of_intervals(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
