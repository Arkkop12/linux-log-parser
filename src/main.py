from pathlib import Path

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

OUTPUT_DIR = PROJECT_ROOT / "outputs"

TEXT_REPORT = OUTPUT_DIR / "report.txt"
JSON_REPORT = OUTPUT_DIR / "report.json"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    lines = read_log_file(SAMPLE_LOG)

    entries = parse_log(lines)

    entries = detect_events(entries)

    statistics = generate_statistics(entries)

    text_report = generate_text_report(
        entries,
        statistics,
    )

    json_report = generate_json_report(
        entries,
        statistics,
    )

    TEXT_REPORT.write_text(
        text_report,
        encoding="utf-8",
    )

    JSON_REPORT.write_text(
        json_report,
        encoding="utf-8",
    )

    print(text_report)

    print()

    print(f"Text report saved to : {TEXT_REPORT}")

    print(f"JSON report saved to : {JSON_REPORT}")


if __name__ == "__main__":
    main()