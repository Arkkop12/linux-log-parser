import argparse
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
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs"


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Linux Log Parser",
    )

    parser.add_argument(
        "log_file",
        type=Path,
        help="Path to the Linux log file.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated reports.",
    )

    return parser.parse_args()


def run(
    log_path: Path,
    output_dir: Path,
) -> None:
    """
    Execute the log analysis pipeline.
    """

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    lines = read_log_file(log_path)

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

    (output_dir / "report.txt").write_text(
        text_report,
        encoding="utf-8",
    )

    (output_dir / "report.json").write_text(
        json_report,
        encoding="utf-8",
    )

    print(text_report)
    print()

    print(f"Text report saved to : {output_dir / 'report.txt'}")
    print(f"JSON report saved to : {output_dir / 'report.json'}")


def main() -> None:
    """
    Application entry point.
    """

    args = parse_arguments()

    run(
        args.log_file,
        args.output,
    )


if __name__ == "__main__":
    main()