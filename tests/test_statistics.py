from pathlib import Path
import unittest

from log_parser.detector import detect_events
from log_parser.models import EventType
from log_parser.parser import parse_log
from log_parser.reader import read_log_file
from log_parser.statistics import generate_statistics


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


class TestStatistics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lines = read_log_file(SAMPLE_LOG)
        entries = parse_log(lines)
        cls.entries = detect_events(entries)

    def test_total_logs(self):
        statistics = generate_statistics(self.entries)

        self.assertEqual(statistics.total_logs, 5)

    def test_failed_login_count(self):
        statistics = generate_statistics(self.entries)

        self.assertEqual(
            statistics.event_counts[EventType.FAILED_LOGIN],
            2,
        )


if __name__ == "__main__":
    unittest.main()