from pathlib import Path
import unittest

from log_parser.reader import read_log_file


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


class TestReader(unittest.TestCase):
    def test_read_log_file_returns_list(self):
        lines = read_log_file(SAMPLE_LOG)

        self.assertIsInstance(lines, list)
        self.assertGreater(len(lines), 0)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_log_file(Path("does_not_exist.log"))


if __name__ == "__main__":
    unittest.main()