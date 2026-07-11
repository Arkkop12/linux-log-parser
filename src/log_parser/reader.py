from pathlib import Path


def read_log_file(path: Path) -> list[str]:
    """
    Read a log file and return its contents as a list of lines.

    Args:
        path: Path to the log file.

    Returns:
        A list of log entries without trailing newline characters.

    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the given path is a directory.
        PermissionError: If the file cannot be read.
    """

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise IsADirectoryError(f"Expected a file but got: {path}")

    with path.open("r", encoding="utf-8", errors="replace") as file:
        return file.read().splitlines()