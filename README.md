# codexopt-demo

Demo repository for showcasing CodexOpt on intentionally messy instruction assets.

## Contents

- `AGENTS.md` with duplicate and conflicting guidance
- `SKILL.md` examples:
  - missing frontmatter
  - verbose/redundant text
  - duplicated lines
- `tasks.md` with 5 evaluation tasks
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

## GEPA Run Guide

For step-by-step local and cloud GEPA setup (including low-budget runs), see:

- `docs/gepa-local-and-cloud.md`

