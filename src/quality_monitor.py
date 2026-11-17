"""Small, dependency-free data quality checks for order events."""

REQUIRED_FIELDS = ("order_id", "event_time", "amount_cents", "currency")


def assess_records(records: list[dict]) -> dict:
    """Return a concise quality report while retaining only first valid order IDs."""
    valid_records = []
    seen_order_ids = set()
    invalid_records = 0
    duplicate_records = 0

    for record in records:
        if any(not record.get(field) for field in REQUIRED_FIELDS) or not isinstance(record.get("amount_cents"), int) or record["amount_cents"] <= 0:
            invalid_records += 1
            continue
        if record["order_id"] in seen_order_ids:
            duplicate_records += 1
            continue
        seen_order_ids.add(record["order_id"])
        valid_records.append(record)

    return {
        "total_records": len(records),
        "valid_records": len(valid_records),
        "invalid_records": invalid_records,
        "duplicate_records": duplicate_records,
        "total_amount_cents": sum(record["amount_cents"] for record in valid_records),
        "quality_status": "passed" if not invalid_records and not duplicate_records else "needs_attention",
    }
