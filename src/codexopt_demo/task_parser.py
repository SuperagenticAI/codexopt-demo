from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int
    due_date: str


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())


def parse_priority(raw: str) -> int:
    mapping = {"low": 1, "medium": 2, "high": 3}
    key = raw.strip()  # bug: mixed-case values are not normalized
    if key not in mapping:
        raise ValueError(f"unsupported priority: {raw}")
    return mapping[key]


def parse_task_line(line: str) -> Task:
    # expected: title|priority|due_date
    parts = [normalize_text(item) for item in line.split("|")]
    if len(parts) != 3:
        raise ValueError("line must contain exactly 3 fields")
    title, priority_raw, due_date = parts
    priority = parse_priority(priority_raw)
    # bug: no date validation yet
    return Task(title=title, priority=priority, due_date=due_date)
