# Data Quality Monitoring Demo

A small, dependency-free Python project that validates order events before they move downstream. It checks required fields, rejects invalid monetary values, detects duplicate order IDs, and produces a concise quality report.

## Why it matters

Data platforms need observable quality gates, not just successful pipeline runs. This demo shows a simple pattern for validating incoming records and reporting whether the batch is safe to use.

## Run

```bash
python3 run_monitor.py
python3 -m unittest discover -s tests -v
```

## Sample output

The included sample intentionally contains duplicate and invalid records, so the report returns `needs_attention` along with counts for each issue type.

## Scope

This is a portfolio demo using synthetic data only. It does not connect to employer systems or contain proprietary data.
