from pathlib import Path

from log_parser.detector import detect_events
from log_parser.parser import parse_log
from log_parser.reader import read_log_file
from log_parser.statistics import generate_statistics


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = PROJECT_ROOT / "assets" / "sample_logs" / "auth.log"


def main() -> None:
    lines = read_log_file(SAMPLE_LOG)

    entries = parse_log(lines)

    entries = detect_events(entries)

    statistics = generate_statistics(entries)

    print(f"Total Logs: {statistics.total_logs}")
    print()

    print("Event Summary")
    print("-" * 30)

    for event_type, count in statistics.event_counts.items():
        print(f"{event_type.value:<20}: {count}")

    print("Process Summary")
    print("-" * 30)

    for process, count in statistics.process_counts.items():
        print(f"{process:<20}: {count}")


if __name__ == "__main__":
    main()