import re

from .models import EventType, LogEntry


EVENT_PATTERNS: dict[EventType, re.Pattern[str]] = {
    EventType.FAILED_LOGIN: re.compile(r"Failed password", re.IGNORECASE),
    EventType.SUCCESSFUL_LOGIN: re.compile(r"Accepted password", re.IGNORECASE),
    EventType.INVALID_USER: re.compile(r"Invalid user", re.IGNORECASE),
    EventType.SUDO_COMMAND: re.compile(r"COMMAND=", re.IGNORECASE),
    EventType.SESSION_OPENED: re.compile(r"Session opened", re.IGNORECASE),
    EventType.SESSION_CLOSED: re.compile(r"Session closed", re.IGNORECASE),
}


def detect_event(entry: LogEntry) -> LogEntry:
    """
    Detect the security event type for a single parsed log entry.
    """

    for event_type, pattern in EVENT_PATTERNS.items():
        if pattern.search(entry.message):
            entry.event_type = event_type
            return entry

    return entry


def detect_events(entries: list[LogEntry]) -> list[LogEntry]:
    """
    Detect security event types for multiple parsed log entries.
    """

    return [detect_event(entry) for entry in entries]