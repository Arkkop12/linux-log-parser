import re
from datetime import datetime

from .exceptions import InvalidLogFormatError
from .models import LogEntry


LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<hostname>\S+)\s+"
    r"(?P<process>[^\[\]:]+)"
    r"(?:\[(?P<pid>\d+)\])?:\s+"
    r"(?P<message>.+)$"
)


def parse_line(line: str) -> LogEntry:
    """
    Parse a single log line into a LogEntry object.
    """

    match = LOG_PATTERN.match(line)

    if match is None:
        raise InvalidLogFormatError(f"Invalid log format: {line}")

    data = match.groupdict()

    current_year = datetime.now().year

    timestamp = datetime.strptime(
        f"{current_year} {data['timestamp']}",
        "%Y %b %d %H:%M:%S",
    )

    pid = int(data["pid"]) if data["pid"] else None

    return LogEntry(
        timestamp=timestamp,
        hostname=data["hostname"],
        process=data["process"],
        pid=pid,
        message=data["message"],
    )


def parse_log(lines: list[str]) -> list[LogEntry]:
    """
    Parse multiple log lines into a list of LogEntry objects.
    """

    entries: list[LogEntry] = []

    for line in lines:
        entries.append(parse_line(line))

    return entries