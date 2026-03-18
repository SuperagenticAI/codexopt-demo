# codexopt-demo

Demo repository for showcasing CodexOpt on intentionally messy instruction assets.

## Main Project

This demo is the companion repository for the main CodexOpt project:

- CodexOpt: https://github.com/SuperagenticAI/CodexOpt

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
codexopt --config codexopt.yaml benchmark
codexopt --config codexopt.yaml optimize agents
codexopt --config codexopt.yaml optimize skills
codexopt apply --kind agents --dry-run
codexopt --config codexopt.yaml report --output codexopt-report.md
```

Command reference used in the demo:

```bash
cd /path/to/codexopt-demo
export GEMINI_API_KEY="YOUR_REAL_KEY"
export GOOGLE_API_KEY="$GEMINI_API_KEY"
rm -rf .codexopt codexopt-report.md
ls
codexopt --config codexopt.gepa.example.yaml benchmark
codexopt --config codexopt.gepa.example.yaml optimize agents --engine heuristic --file AGENTS.md
codexopt --config codexopt.gepa.example.yaml optimize skills --engine heuristic --glob ".codex/skills/**/SKILL.md"
codexopt apply --kind agents --dry-run
codexopt apply --kind skills --dry-run
codexopt --config codexopt.gepa.example.yaml report --output codexopt-report.md
sed -n '1,120p' codexopt-report.md
codexopt --config codexopt.gepa.example.yaml optimize agents \
  --engine gepa \
  --reflection-model gemini/gemini-2.5-pro \
  --max-metric-calls 2 \
  --file AGENTS.md
```

- `benchmark`: baseline score plus evidence-aware feedback
- `optimize agents`: optimize `AGENTS.md`
- `optimize skills`: optimize demo skill files
- `apply --dry-run`: preview changes without writing files
- `report`: generate a markdown summary from the latest runs
- `optimize ... --engine gepa`: optional low-budget GEPA example with Gemini 2.5 Pro

To benchmark against repo tasks and issue themes, copy the demo config first:

```bash
cp codexopt.gepa.example.yaml codexopt.yaml
codexopt --config codexopt.yaml benchmark
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

GEPA in CodexOpt is model-agnostic. You can use OpenAI, Gemini, local models,
or other GEPA/LiteLLM-compatible providers for reflection and candidate feedback.

OpenAI example:

```bash
export OPENAI_API_KEY="YOUR_KEY"
```

```yaml
optimization:
  engine: "gepa"
  reflection_model: "openai/gpt-5-mini"
```

Gemini example:

```bash
export GEMINI_API_KEY="YOUR_KEY"
export GOOGLE_API_KEY="$GEMINI_API_KEY"
```

```yaml
optimization:
  engine: "gepa"
  reflection_model: "gemini/gemini-2.5-pro"
```

### 3) Run optimization with GEPA

```bash
codexopt --config codexopt.yaml optimize agents
codexopt --config codexopt.yaml optimize skills
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

## Try It Yourself

```bash
cd /path/to/codexopt-demo
export GEMINI_API_KEY="YOUR_REAL_KEY"
export GOOGLE_API_KEY="$GEMINI_API_KEY"
rm -rf .codexopt codexopt-report.md
ls
codexopt --config codexopt.gepa.example.yaml benchmark
codexopt --config codexopt.gepa.example.yaml optimize agents --engine heuristic --file AGENTS.md
codexopt --config codexopt.gepa.example.yaml optimize skills --engine heuristic --glob ".codex/skills/**/SKILL.md"
codexopt apply --kind agents --dry-run
codexopt apply --kind skills --dry-run
codexopt --config codexopt.gepa.example.yaml report --output codexopt-report.md
sed -n '1,120p' codexopt-report.md
codexopt --config codexopt.gepa.example.yaml optimize agents \
  --engine gepa \
  --reflection-model gemini/gemini-2.5-pro \
  --max-metric-calls 2 \
  --file AGENTS.md
```
