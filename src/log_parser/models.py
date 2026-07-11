from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class LogEntry:
    """
    Represents a single parsed log entry.
    """

    timestamp: datetime
    hostname: str
    process: str
    pid: int | None
    message: str