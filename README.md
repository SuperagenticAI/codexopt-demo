# codexopt-demo

Demo repository for showcasing CodexOpt on intentionally messy instruction assets.

## Contents

- `AGENTS.md` with duplicate and conflicting guidance
- `SKILL.md` examples:
  - missing frontmatter
  - verbose/redundant text
  - duplicated lines
- `tasks.md` with 5 evaluation tasks
- `issues.md` with recurring feedback themes
- Tiny Python package under `src/codexopt_demo`
- GEPA local/cloud setup guide: `docs/gepa-local-and-cloud.md`

## Quick Start (uv)

```bash
uv lock
uv sync --extra dev
uv run --no-sync pytest -q
uv run --no-sync ruff check src tests
```

## Run CodexOpt against this demo

From this repo root:

```bash
codexopt init
codexopt scan
codexopt benchmark
codexopt optimize agents --file AGENTS.md
codexopt optimize skills --glob ".codex/skills/**/SKILL.md"
codexopt apply --kind skills --dry-run
codexopt report --output codexopt-report.md
```

## How To Run This Demo

This demo is meant to mirror how a team would use CodexOpt in a real repository.

Inputs in this demo:

- [`AGENTS.md`](/Users/shashi/oss/codexopt-demo/AGENTS.md)
- demo skills under [`.codex/skills/`](/Users/shashi/oss/codexopt-demo/.codex/skills)
- repo task evidence in [`tasks.md`](/Users/shashi/oss/codexopt-demo/tasks.md)
- recurring feedback themes in [`issues.md`](/Users/shashi/oss/codexopt-demo/issues.md)

Suggested flow:

1. Run `benchmark` to get a baseline score plus feedback.
2. Run `optimize agents` and `optimize skills`.
3. Review `.codexopt/runs/*/optimize.json` and generated reports.
4. Use `apply --dry-run` before writing any changes.

Example:

```bash
cp codexopt.gepa.example.yaml codexopt.yaml
codexopt benchmark --config codexopt.yaml
codexopt optimize agents --config codexopt.yaml
codexopt optimize skills --config codexopt.yaml
codexopt apply --kind agents --dry-run
codexopt report --output codexopt-report.md
```

To benchmark against repo tasks and issue themes, copy the demo config first:

```bash
cp codexopt.gepa.example.yaml codexopt.yaml
codexopt benchmark --config codexopt.yaml
```

That config enables:

- `tasks.md` as task evidence
- `issues.md` as recurring feedback evidence

The benchmark and report artifacts will then include:

- criterion sub-scores
- natural-language feedback
- task/issue evidence counts

The current demo shows evidence-aware instruction optimization. It does not yet run full agent task simulations from `tasks.md`; those tasks currently shape scoring and feedback.

## GEPA Configuration in this Demo

Use this example file:

- `codexopt.gepa.example.yaml`

### 1) Copy it to active config

```bash
cp codexopt.gepa.example.yaml codexopt.yaml
```

### 2) Set your reflection model

Edit `codexopt.yaml`:

```yaml
evidence:
  task_files:
    - tasks.md
  issue_files:
    - issues.md
optimization:
  engine: "gepa"
  max_metric_calls: 120
  reflection_model: "your-provider/your-reflection-model"
```

### 3) Run optimization with GEPA

```bash
codexopt optimize agents --config codexopt.yaml
codexopt optimize skills --config codexopt.yaml
```

### 4) Override from CLI (optional)

```bash
codexopt optimize skills \
  --engine gepa \
  --reflection-model your-provider/your-reflection-model \
  --max-metric-calls 200
```

### About "iterations"

Current CodexOpt exposes GEPA tuning via `max_metric_calls` and `reflection_model`.
A direct `iterations` field is not exposed yet; use `max_metric_calls` as the primary search-budget control.

If GEPA is unavailable or the requested model path fails, CodexOpt records that fallback in the optimization artifact and report.

## GEPA Run Guide

For step-by-step local and cloud GEPA setup (including low-budget runs), see:

- `docs/gepa-local-and-cloud.md`
