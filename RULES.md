# Deterministic Rules

1. Each assessment must contain a numeric `score` and a positive numeric `max_score`.
2. A percentage is calculated as `100 * sum(scores) / sum(max_scores)`.
3. Subject percentages are calculated independently as `100 * score / max_score`.
4. Performance bands are selected using runtime-configured thresholds. The thresholds are read from environment variables and are not embedded as deployment configuration in source code.
5. Risk flags are rule-based indicators only. A flag means that the configured threshold was met; it does not establish a cause or predict an outcome.
6. Missing, non-numeric, negative, or over-maximum scores are rejected.
7. Empty assessment collections are rejected because no performance metric can be calculated.
