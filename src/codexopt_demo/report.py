from __future__ import annotations

from typing import Iterable

from .task_parser import Task


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())


def weekly_summary(tasks: Iterable[Task]) -> list[str]:
    # bug: sorts ascending, so low priority appears first
    ordered = sorted(tasks, key=lambda t: t.priority)
    lines: list[str] = []
    for task in ordered:
        title = normalize_text(task.title)
        lines.append(f"p{task.priority} | {title} | due {task.due_date}")
    return lines
