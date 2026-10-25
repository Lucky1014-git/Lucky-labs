import unittest

from features import reports


class TestAverageScore(unittest.TestCase):
    def test_average_of_several_scores(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)

    def test_average_is_rounded_to_one_decimal(self):
        self.assertEqual(reports.average_score({"history": [1, 2, 2]}), 1.7)

    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)


if __name__ == "__main__":
    unittest.main()
