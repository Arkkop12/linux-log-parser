# Linux Log Parser
### A Python-based log analysis tool for Blue Team learning.

A Python-based log analysis tool designed to help understand how Linux authentication logs can be transformed into structured security information. The project parses Linux authentication logs, identifies common security events, generates statistical summaries, and exports analysis reports in both text and JSON formats.

The primary objective of this project is to understand how Linux authentication logs can be transformed into structured security information through log parsing, event detection, and reporting while applying clean software engineering principles.

## Architecture Diagram

## Project Overview

Linux Log Parser is the second project in a long-term Blue Team Cyber Security portfolio roadmap. It focuses on one core competency: Linux log analysis.

The application reads Linux authentication log files, parses each log entry into structured data, detects common security-related events, calculates useful statistics, and generates analysis reports that can be used for further investigation.

Rather than attempting to build a full Security Information and Event Management (SIEM) platform, this project intentionally focuses on a single responsibility: transforming raw Linux authentication logs into meaningful security information. This keeps the project focused, maintainable, and aligned with the principle of one repository for one primary competency.

## Project Highlights

* Parses Linux authentication log files into structured Python objects.
* Detects common security-related events such as failed logins, successful logins, and sudo command executions.
* Generates statistical summaries for detected events and running processes.
* Produces analysis reports in both human-readable text and JSON formats.
* Provides a simple Command Line Interface (CLI) using the Python Standard Library.
* Includes automated unit tests covering the application's core modules.
* Uses a modular architecture with clear separation of responsibilities.
* Relies exclusively on the Python Standard Library without external runtime dependencies.

## Features

* Read Linux authentication log files.
* Parse raw log entries into structured objects.
* Detect predefined security events.
* Generate event and process statistics.
* Export reports as TXT and JSON.
* Support configurable output directories through the CLI.
* Handle common file-related exceptions gracefully.
* Validate core functionality using automated unit tests.

## Technology Stack

| Category                | Technology               |
| ----------------------- | ------------------------ |
| Programming Language    | Python 3                 |
| Operating System        | Linux Mint 22.3 Cinnamon |
| Version Control         | Git                      |
| Repository Hosting      | GitHub                   |
| Development Environment | Visual Studio Code       |
| Testing Framework       | unittest                 |
| Build Configuration     | pyproject.toml           |
| Dependencies            | Python Standard Library  |

## Software Architecture

The application is designed using a modular architecture where each module has a single responsibility. Every stage of the log analysis pipeline is separated into its own component, making the project easier to understand, maintain, test, and extend.

| Module          | Responsibility                                                                              |
| --------------- | ------------------------------------------------------------------------------------------- |
| `reader.py`     | Read raw log files from the filesystem.                                                     |
| `parser.py`     | Parse raw log lines into structured `LogEntry` objects.                                     |
| `detector.py`   | Identify predefined security-related events from parsed logs.                               |
| `statistics.py` | Generate event and process statistics.                                                      |
| `reporter.py`   | Generate analysis reports in TXT and JSON formats.                                          |
| `main.py`       | Coordinate the complete log analysis workflow and provide the Command Line Interface (CLI). |

The project follows the principle of **Separation of Concerns**, where each module focuses on one specific task. This design simplifies future maintenance while improving readability and testability.

## Workflow

The application processes Linux log files through several sequential stages.

1. Read the input log file.
2. Parse each log line into a structured object.
3. Detect predefined security events.
4. Generate statistical summaries.
5. Produce TXT and JSON reports.
6. Save generated reports to the selected output directory.

The overall workflow can be summarized as follows:

```text
Log File
    │
    ▼
Reader
    │
    ▼
Parser
    │
    ▼
Event Detector
    │
    ▼
Statistics
    │
    ▼
Reporter
    │
    ▼
TXT Report
JSON Report
```

## Repository Structure

```text
linux-log-parser/
├── assets/
│   ├── diagram/
│   ├── images/
│   └── sample_logs/
├── configs/
├── notes/
├── outputs/
├── src/
│   ├── log_parser/
│   └── main.py
├── tests/
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

### Directory Description

| Directory  | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| `assets/`  | Project assets including diagrams, images, and sample log files. |
| `configs/` | Configuration files for future project expansion.                |
| `notes/`   | Development notes and supporting documentation.                  |
| `outputs/` | Generated TXT and JSON reports.                                  |
| `src/`     | Application source code.                                         |
| `tests/`   | Automated unit tests.                                            |

## Installation

Clone the repository.

```bash
git clone https://github.com/Arkkop12/linux-log-parser.git
```

Move into the project directory.

```bash
cd linux-log-parser
```

(Optional) Create and activate a virtual environment.

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install the project in editable mode.

```bash
pip install -e .
```

## Usage

Analyze a Linux authentication log file.

```bash
python src/main.py assets/sample_logs/auth.log
```

Specify a custom output directory.

```bash
python src/main.py assets/sample_logs/auth.log --output reports
```

Display the command-line help message.

```bash
python src/main.py --help
```

The application generates two reports:

* `report.txt`
* `report.json`

Both reports are stored in the selected output directory.

## Example Output

```text
==================================================
Linux Log Analysis Report
==================================================

Generated : 2026-07-11 16:30:41
Total Logs: 5

==================================================
Event Summary
==================================================

FAILED_LOGIN      : 2
SUCCESSFUL_LOGIN  : 1
SUDO_COMMAND      : 1
SESSION_OPENED    : 1

==================================================
Process Summary
==================================================

sshd              : 3
sudo              : 1
systemd-logind    : 1
```

*A complete report also includes a detailed event section and a JSON-formatted report.*

## Testing

Run all unit tests from the project root.

```bash
python -m unittest discover tests
```

Expected output:

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.0xxs

OK
```

The project includes automated unit tests covering the core modules, including log reading, parsing, event detection, statistics generation, and report generation.

## Future Improvements

The following improvements are intentionally left for future iterations while keeping the current project focused on its primary objective.

* Support additional Linux log formats.
* Add configurable event detection rules.
* Export analysis reports in CSV format.
* Improve event filtering capabilities.
* Support recursive log analysis for multiple log files.

## Author

**Arka Dwi Indrastata**

Informatics Student

Informatics Student with a learning focus on Blue Team Cyber Security, including Linux security, log analysis, DFIR, and Security Operations.

GitHub: https://github.com/Arkkop12

## License

This project is distributed under the MIT License.

See the `LICENSE` file for additional information.
