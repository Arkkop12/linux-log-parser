from pathlib import Path

from log_parser.reader import read_log_file


def main() -> None:
    log_path = Path("assets/sample_logs/auth.log")

    lines = read_log_file(log_path)

    print(f"Total lines: {len(lines)}")
    print()

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()  