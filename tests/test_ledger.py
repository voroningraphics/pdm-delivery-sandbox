"""Versioned delivery smoke cases; no credentials, network or dependencies."""

import copy
import unittest

from ledger import summarize_entries


class LedgerTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(summarize_entries([]), {})

    def test_normalization_and_totals(self):
        self.assertEqual(
            summarize_entries(
                [
                    {"category": " Work ", "cents": 2},
                    {"category": "work", "cents": -3},
                    {"category": "home", "cents": 0},
                ]
            ),
            {"work": {"count": 2, "total": -1}, "home": {"count": 1, "total": 0}},
        )

    def test_blank_categories(self):
        self.assertEqual(summarize_entries([{"category": " ", "cents": 99}]), {})

    def test_input_is_unchanged(self):
        entries = [{"category": " X ", "cents": 7}]
        original = copy.deepcopy(entries)
        summarize_entries(entries)
        self.assertEqual(entries, original)


if __name__ == "__main__":
    unittest.main()
