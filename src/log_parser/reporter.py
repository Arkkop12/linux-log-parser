import json
from datetime import datetime

from .models import LogEntry, Statistics


def add_section(lines: list[str], title: str) -> None:
    """
    Append a formatted section heading to the report.
    """

    lines.append("=" * 50)
    lines.append(title)
    lines.append("=" * 50)


def generate_text_report(
    entries: list[LogEntry],
    statistics: Statistics,
) -> str:
    """
    Generate a human-readable text report.
    """

    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = []

    add_section(lines, "Linux Log Analysis Report")
    lines.append("")
    lines.append(f"Generated : {generated_time}")
    lines.append(f"Total Logs: {statistics.total_logs}")
    lines.append("")

    add_section(lines, "Event Summary")

    for event_type, count in statistics.event_counts.items():
        lines.append(f"{event_type.value:<20}: {count}")

    lines.append("")

    add_section(lines, "Process Summary")

    for process, count in statistics.process_counts.items():
        lines.append(f"{process:<20}: {count}")

    lines.append("")

    add_section(lines, "Detailed Events")
    lines.append("")

    for entry in entries:
        lines.append(f"[{entry.event_type.value}]")
        lines.append(
            f"Time     : {entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        lines.append(f"Host     : {entry.hostname}")
        lines.append(f"Process  : {entry.process}")
        lines.append(
            f"PID      : {entry.pid if entry.pid is not None else '-'}"
        )
        lines.append(f"Message  : {entry.message}")
        lines.append("")
        lines.append("-" * 50)
        lines.append("")

    return "\n".join(lines)


def generate_json_report(
    entries: list[LogEntry],
    statistics: Statistics,
) -> str:
    """
    Generate a JSON report.
    """

    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = {
        "generated_at": generated_time,
        "total_logs": statistics.total_logs,
        "event_summary": {
            event.value: count
            for event, count in statistics.event_counts.items()
        },
        "process_summary": statistics.process_counts,
        "detailed_events": [
            {
                "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "hostname": entry.hostname,
                "process": entry.process,
                "pid": entry.pid,
                "event_type": entry.event_type.value,
                "message": entry.message,
            }
            for entry in entries
        ],
    }

    return json.dumps(
        report,
        indent=4,
        ensure_ascii=False,
    )