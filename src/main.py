from pathlib import Path

from log_parser.parser import parse_log
from log_parser.reader import read_log_file


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


def main() -> None:
    lines = read_log_file(SAMPLE_LOG)

    entries = parse_log(lines)

    print(f"Total entries: {len(entries)}")
    print()

    for entry in entries:
        print(entry)


if __name__ == "__main__":
    main()