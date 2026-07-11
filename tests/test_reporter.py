from pathlib import Path
import json
import unittest

from log_parser.detector import detect_events
from log_parser.parser import parse_log
from log_parser.reader import read_log_file
from log_parser.reporter import (
    generate_json_report,
    generate_text_report,
)
from log_parser.statistics import generate_statistics


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


class TestReporter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lines = read_log_file(SAMPLE_LOG)
        entries = parse_log(lines)
        cls.entries = detect_events(entries)
        cls.statistics = generate_statistics(cls.entries)

    def test_text_report(self):
        report = generate_text_report(
            self.entries,
            self.statistics,
        )

        self.assertIsInstance(report, str)
        self.assertIn("Linux Log Analysis Report", report)
        self.assertIn("Event Summary", report)

    def test_json_report(self):
        report = generate_json_report(
            self.entries,
            self.statistics,
        )

        data = json.loads(report)

        self.assertEqual(data["total_logs"], 5)
        self.assertIn("event_summary", data)
        self.assertIn("process_summary", data)


if __name__ == "__main__":
    unittest.main()