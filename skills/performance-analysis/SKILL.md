---
name: performance-analysis
description: Analyze supplied student assessment records using deterministic performance calculations and report transparent results.
---

# Performance Analysis

## Purpose

This skill analyzes structured student assessment records and calculates performance metrics without inventing missing data.

## Inputs

Each assessment must contain a numeric `score` and a positive numeric `max_score`. Scores must be between zero and the supplied maximum.

## Behavior

The skill validates the assessment records before calculation. Overall performance is calculated from the supplied scores and maximum scores, and assessment-level percentages are reported.

## Outputs

The skill returns structured performance metrics including total score, total maximum score, overall percentage, and assessment-level percentages.

## Invalid Inputs

Malformed assessments, missing required fields, invalid numeric values, impossible score ranges, and empty assessment lists are rejected with structured errors.

## Limitations

The skill only analyzes caller-provided numerical assessment data. It does not infer causes of performance or predict future academic outcomes.
