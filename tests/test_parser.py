from pathlib import Path
import unittest

from log_parser.models import LogEntry
from log_parser.parser import parse_line
from log_parser.reader import read_log_file


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.line = read_log_file(SAMPLE_LOG)[0]

    def test_parse_line_returns_log_entry(self):
        entry = parse_line(self.line)

        self.assertIsInstance(entry, LogEntry)

    def test_parse_line_process(self):
        entry = parse_line(self.line)

        self.assertEqual(entry.process, "sshd")

    def test_parse_line_pid(self):
        entry = parse_line(self.line)

        self.assertEqual(entry.pid, 2154)


if __name__ == "__main__":
    unittest.main()