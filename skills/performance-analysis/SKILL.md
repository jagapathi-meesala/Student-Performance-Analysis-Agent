# Performance Analysis Skill

## Purpose
Calculate transparent aggregate and per-assessment performance metrics from structured scores.

## Inputs
A non-empty `assessments` list is required. Each assessment contains a numeric `score` and positive numeric `max_score`, with an optional name.

## Behavior
The skill validates every record and calculates `100 * sum(score) / sum(max_score)`. It also calculates a percentage for each assessment independently.

## Outputs
The result contains total score, total maximum score, overall percentage, and per-assessment percentages.

## Invalid Inputs
Missing fields, non-numeric values, negative scores, scores above the maximum, non-positive maximums, and empty lists are rejected.
