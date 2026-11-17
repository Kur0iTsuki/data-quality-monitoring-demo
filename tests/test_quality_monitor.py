import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from quality_monitor import assess_records


class QualityMonitorTests(unittest.TestCase):
    def test_assess_records_reports_valid_invalid_and_duplicate_rows(self):
        records = [
            {"order_id": "1001", "event_time": "2026-11-01T10:00:00Z", "amount_cents": 1200, "currency": "USD"},
            {"order_id": "1001", "event_time": "2026-11-01T10:00:00Z", "amount_cents": 1200, "currency": "USD"},
            {"order_id": "1002", "event_time": "2026-11-01T10:05:00Z", "amount_cents": -50, "currency": "USD"},
            {"order_id": "1003", "event_time": "", "amount_cents": 700, "currency": "USD"},
        ]

        report = assess_records(records)

        self.assertEqual(report["total_records"], 4)
        self.assertEqual(report["valid_records"], 1)
        self.assertEqual(report["duplicate_records"], 1)
        self.assertEqual(report["invalid_records"], 2)
        self.assertEqual(report["quality_status"], "needs_attention")

    def test_assess_records_passes_clean_input(self):
        records = [
            {"order_id": "1001", "event_time": "2026-11-01T10:00:00Z", "amount_cents": 1200, "currency": "USD"},
            {"order_id": "1002", "event_time": "2026-11-01T10:05:00Z", "amount_cents": 700, "currency": "USD"},
        ]

        report = assess_records(records)

        self.assertEqual(report["quality_status"], "passed")
        self.assertEqual(report["total_amount_cents"], 1900)


if __name__ == "__main__":
    unittest.main()
