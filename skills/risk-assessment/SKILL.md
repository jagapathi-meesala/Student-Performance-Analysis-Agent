# Risk Assessment Skill

## Purpose
Identify a transparent, rule-based indicator when overall performance is below a configured threshold.

## Inputs
The skill consumes validated assessment records and runtime thresholds supplied through environment variables.

## Behavior
It first calculates the overall percentage, then compares it with `STUDENT_PERFORMANCE_RISK_THRESHOLD`. No causal or predictive conclusion is produced.

## Outputs
The output contains a boolean flag, the applied rule name, the configured threshold, and an explanation tied to that comparison.

## Invalid Inputs
Invalid assessment records or missing/invalid runtime configuration produce structured errors rather than substituted values.
