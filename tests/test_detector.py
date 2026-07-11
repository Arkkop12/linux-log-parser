from pathlib import Path
import unittest

from log_parser.detector import detect_event
from log_parser.models import EventType
from log_parser.parser import parse_line
from log_parser.reader import read_log_file


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


class TestDetector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines = read_log_file(SAMPLE_LOG)

    def test_failed_login_detection(self):
        entry = parse_line(self.lines[0])

        detect_event(entry)

        self.assertEqual(entry.event_type, EventType.FAILED_LOGIN)

    def test_successful_login_detection(self):
        entry = parse_line(self.lines[2])

        detect_event(entry)

        self.assertEqual(entry.event_type, EventType.SUCCESSFUL_LOGIN)

    def test_sudo_detection(self):
        entry = parse_line(self.lines[3])

        detect_event(entry)

        self.assertEqual(entry.event_type, EventType.SUDO_COMMAND)


if __name__ == "__main__":
    unittest.main()