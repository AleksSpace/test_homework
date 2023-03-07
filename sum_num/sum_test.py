import unittest

from .sum import sum_num


class TestSumNum(unittest.TestCase):

    def test_sum(self):
        n = [12, 10, 5, 3, 56, 45]
        result = sum_num(n)
        self.assertEqual(result, 75)

        n2 = [13, 14, 6, 4, 5, 3]
        result2 = sum_num(n2)
        self.assertEqual(result2, 14)

        n3 = [1, 2, 4, 7, 8]
        result3 = sum_num(n3)
        self.assertEqual(result3, 0)
