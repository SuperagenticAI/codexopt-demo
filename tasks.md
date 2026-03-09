# Evaluation Tasks (Demo)

Use these five tasks to compare baseline vs optimized instruction assets.

1. Fix `parse_priority` so it accepts uppercase values like `"HIGH"` and `"Medium"`.
2. Add validation to reject malformed due dates and raise a clear `ValueError`.
3. Remove duplicated `normalize_text` logic across modules without changing behavior.
4. Add tests that cover empty input, mixed-case priorities, and malformed dates.
5. Improve weekly report ordering to show highest priority tasks first.
