from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(Enum):
    """
    Supported security event types.
    """

    FAILED_LOGIN = "FAILED_LOGIN"
    SUCCESSFUL_LOGIN = "SUCCESSFUL_LOGIN"
    INVALID_USER = "INVALID_USER"
    SUDO_COMMAND = "SUDO_COMMAND"
    SESSION_OPENED = "SESSION_OPENED"
    SESSION_CLOSED = "SESSION_CLOSED"
    UNKNOWN = "UNKNOWN"


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
    event_type: EventType = EventType.UNKNOWN

    @property
    def formatted_timestamp(self) -> str:
        """
        Return the timestamp as a formatted string.
        """
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def pid_display(self) -> str:
        """
        Return the PID as a display string.
        """
        return str(self.pid) if self.pid is not None else "-"

    @property
    def event_name(self) -> str:
        """
        Return the event type as a string.
        """
        return self.event_type.value


@dataclass(slots=True)
class Statistics:
    """
    Stores summary statistics for parsed log entries.
    """

    total_logs: int
    event_counts: dict[EventType, int]
    process_counts: dict[str, int]