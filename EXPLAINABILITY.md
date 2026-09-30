# Explainability

## Inputs and Data Sources
The agent receives structured assessment records containing scores, maximum marks, and optional assessment names. The data source is the caller-provided academic record; the agent does not fetch grades from an external database or invent missing values.

### Input Requirements
Each assessment must contain a numeric `score` and a positive numeric `max_score`. Scores must be between zero and the supplied maximum, and the assessment list must contain at least one record.

### Input Validation
Validation occurs before any calculation. Missing fields, invalid numeric values, impossible score ranges, and empty assessment lists are rejected with a structured error.

## Decision and Reasoning
The agent calculates overall performance as `100 * sum(scores) / sum(max_scores)`, so assessments are weighted by their supplied maximum marks. Performance bands and risk flags are selected by deterministic comparisons against runtime-configured thresholds, making the same valid input produce the same result under the same configuration.

### Decision Mechanics
The performance-analysis path calculates total score, total maximum score, overall percentage, and each assessment percentage. The risk path compares the resulting overall percentage with `STUDENT_PERFORMANCE_RISK_THRESHOLD` and reports the exact rule used.

### Tool Behavior
`calculate-performance` returns raw calculated metrics. `analyze-performance` adds a configured performance band, while `identify-risk` adds a rule-based indicator and its threshold; each tool uses the same validated calculation logic.

### Failure Handling
A malformed request is rejected rather than repaired silently. Missing runtime configuration is reported as a configuration error, and unknown tools are rejected by the portable registry boundary.

## Limits and Constraints
The agent only analyzes the supplied numerical assessment records and configured thresholds. It cannot establish why a student achieved a score, predict future academic outcomes, or substitute for educator judgment or institutional policy.

### Constraints
The agent does not infer sensitive personal characteristics, fabricate missing assessments, compare a student with an unnamed population, or turn a threshold flag into a diagnosis. Framework adapters are compatibility boundaries and do not imply that a framework SDK is installed or tested.

### Expected Outputs
Successful outputs contain structured metrics and, where requested, a transparent band or risk indicator. Failed inputs contain an error category and message without exposing internal tracebacks.

### Worked Example
For assessments of 18/20 and 32/40, the overall percentage is `100 * (18 + 32) / (20 + 40) = 83.33%`. The result is then compared with the runtime thresholds; no additional causal conclusion is inferred from the percentage.

### Provenance
Calculated values originate from the caller-provided assessment records and the runtime environment variables used as thresholds. No external academic dataset is silently consulted by the deterministic implementation.
