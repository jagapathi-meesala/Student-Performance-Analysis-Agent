---
name: risk-assessment
description: Identify rule-based student performance risk indicators from supplied assessment results and configured thresholds.
---

# Risk Assessment

## Purpose

This skill identifies a performance risk indicator from validated student assessment results using deterministic threshold rules.

## Inputs

The skill receives validated assessment records and the configured student performance risk threshold. The threshold is supplied through runtime configuration.

## Behavior

The skill calculates the overall performance percentage using the same validated calculation logic as the performance analysis path. It compares that percentage against the configured threshold and reports the rule used.

## Outputs

The skill returns a structured risk indicator, the calculated performance percentage, the threshold used, and an explanation of the deterministic comparison.

## Invalid Inputs

Invalid assessment records are rejected before risk evaluation. Missing required runtime configuration is reported as a configuration error rather than silently replaced with an invented production value.

## Limitations

A risk indicator is not a diagnosis or prediction. The skill only evaluates the supplied numerical assessment data against the configured deterministic threshold.
