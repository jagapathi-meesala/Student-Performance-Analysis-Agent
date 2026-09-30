# Architecture

The project separates domain logic in `core/`, tool contracts in `contracts/`, declarative tool descriptions in `tools/`, skills in `skills/`, and framework boundaries in `adapters/`. The core does not import OpenAI, CrewAI, Claude, or Lyzr SDKs.

# Development Rules

Keep domain calculations deterministic and independently testable. Runtime configuration belongs in environment variables; secrets must never be committed.

# Tool Conventions

Each tool validates its input, returns a structured result, and reports failures without exposing internal tracebacks as user-facing data. Tool definitions use stable names and explicit input/output contracts.

# Testing Rules

Run `pytest -q` before committing. Documentation and manifest structure are tested alongside executable behavior.

# Portability

Adapters translate framework-specific invocation shapes into the framework-independent portable contract. An adapter must not claim an installed framework dependency unless that dependency is actually tested in the environment.
