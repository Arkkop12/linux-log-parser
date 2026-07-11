from collections import Counter

from .models import EventType, LogEntry, Statistics


def generate_statistics(entries: list[LogEntry]) -> Statistics:
    """
    Generate summary statistics from parsed log entries.
    """

    event_counter = Counter(entry.event_type for entry in entries)
    process_counter = Counter(entry.process for entry in entries)

    event_counts = {
        event_type: event_counter.get(event_type, 0)
        for event_type in EventType
    }

    process_counts = dict(process_counter)

    return Statistics(
        total_logs=len(entries),
        event_counts=event_counts,
        process_counts=process_counts,
    )