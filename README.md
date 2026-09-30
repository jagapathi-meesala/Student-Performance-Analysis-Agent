# Student Performance Analysis Agent

A framework-independent OpenGAP agent for transparent, deterministic analysis of structured academic assessment records.

## Capabilities

- Calculate aggregate and per-assessment performance metrics.
- Produce a transparent performance summary.
- Identify configured rule-based indicators for review.
- Expose a framework-independent tool contract and adapter boundary.

## Structure

- `agent.yaml` — OpenGAP manifest.
- `SOUL.md`, `RULES.md`, `DUTIES.md`, `AGENTS.md` — agent identity and behavior.
- `core/` — domain logic.
- `contracts/` — portable tool contract types.
- `tools/` — declarative tool schemas.
- `skills/` — reusable capability documentation.
- `adapters/` — framework-neutral interoperability boundaries.
- `verification/` — structural and schema checks.
- `tests/` — automated tests.

## Configuration

Copy `.env.example` to `.env` and provide the runtime thresholds. No secret is required for the deterministic local analysis implementation.

## Validation

Run `pytest -q`. If the OpenGAP CLI is installed, run `opengap validate` from the repository root. The local test suite does not claim OpenGAP CLI verification when the CLI is unavailable.
