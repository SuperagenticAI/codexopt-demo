# Running CodexOpt with GEPA (Local + Cloud)

This guide shows how to run CodexOpt with GEPA in a small-budget setup using either:

- Local models (for example, Ollama)
- Cloud models (for example, Google Gemini via LiteLLM provider naming)

It is written to be copy-paste friendly for any machine.

## Prerequisites

- Python 3.10+
- `uv`
- `codexopt-demo` repository
- `codexopt` available in your environment
- `gepa` installed in the same environment

## 1) Environment Setup

From the demo repository root:

```bash
uv sync --extra dev
uv pip install -e ../codexopt
uv pip install gepa
uv run python -c "from gepa.optimize_anything import optimize_anything; print('GEPA OK')"
```

If your `codexopt` package is not next to this repo, replace `../codexopt` with your actual local path.

## 2) Baseline (No model cost)

```bash
uv run codexopt init
uv run codexopt scan
uv run codexopt benchmark
```

This gives baseline metrics before GEPA optimization.

## 3) Local Models (Ollama)

### 3.1 Start model runtime and pull a small model

```bash
ollama serve
ollama pull qwen3:8b
```

### 3.2 Create local GEPA config

Create `codexopt.local.yaml`:

```yaml
version: 1
targets:
  agents_files:
    - AGENTS.md
  skills_globs:
    - ".codex/skills/**/SKILL.md"
  exclude_globs:
    - ".git/**"
    - ".venv/**"
    - ".uv-cache/**"
    - ".codexopt/**"
output:
  root_dir: ".codexopt"
optimization:
  engine: "gepa"
  min_apply_delta: 0.01
  max_metric_calls: 20
  reflection_model: "ollama/qwen3:8b"
```

### 3.3 Run low-budget local optimization

```bash
uv run codexopt --config codexopt.local.yaml optimize skills
uv run codexopt --config codexopt.local.yaml optimize agents
uv run codexopt --config codexopt.local.yaml report --output report-local.md
```

## 4) Cloud Models (Google Gemini)

### 4.1 Set API key(s)

```bash
export GEMINI_API_KEY="YOUR_KEY"
export GOOGLE_API_KEY="$GEMINI_API_KEY"
```

### 4.2 Create cloud GEPA config

Create `codexopt.gemini.yaml`:

```yaml
version: 1
targets:
  agents_files:
    - AGENTS.md
  skills_globs:
    - ".codex/skills/**/SKILL.md"
  exclude_globs:
    - ".git/**"
    - ".venv/**"
    - ".uv-cache/**"
    - ".codexopt/**"
output:
  root_dir: ".codexopt"
optimization:
  engine: "gepa"
  min_apply_delta: 0.01
  max_metric_calls: 20
  reflection_model: "gemini/gemini-2.0-flash-exp"
```

If that alias is not supported in your setup, switch to the Gemini model identifier supported by your LiteLLM/provider configuration.

### 4.3 Run low-budget cloud optimization

```bash
uv run codexopt --config codexopt.gemini.yaml optimize skills
uv run codexopt --config codexopt.gemini.yaml optimize agents
uv run codexopt --config codexopt.gemini.yaml report --output report-gemini.md
```

## 5) Budget Control Tips

- Start with `max_metric_calls: 20`.
- Optimize one target at a time (`skills`, then `agents`).
- Review with dry-run first:

```bash
uv run codexopt apply --kind skills --dry-run
```

- Increase budget gradually (`20 -> 40 -> 80`) only if deltas are promising.

## 6) About "iterations"

Current CodexOpt GEPA integration exposes tuning primarily via:

- `reflection_model`
- `max_metric_calls`

A direct `iterations` field is not exposed yet.

## 7) Suggested comparison flow for a tiny experiment

1. Baseline: `scan` + `benchmark`
2. Local run: GEPA with Ollama (`max_metric_calls: 20`)
3. Cloud run: GEPA with Gemini (`max_metric_calls: 20`)
4. Compare:
   - files improved
   - average delta
   - quality vs cost tradeoff

Use `.codexopt/runs/*` artifacts and generated reports to document your results.
