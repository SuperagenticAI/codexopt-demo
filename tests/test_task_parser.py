from codexopt_demo.task_parser import parse_priority


def test_parse_priority_lowercase() -> None:
    assert parse_priority("high") == 3
