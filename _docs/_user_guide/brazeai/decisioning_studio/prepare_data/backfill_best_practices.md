---
nav_title: Backfilling best practices
article_title: "Backfill best practices"
page_order: 7
page_type: reference
description: "Learn how to correctly backfill historical data for BrazeAI Decisioning Studio, including requirements, common pitfalls, and how to avoid data quality issues that affect AI model performance."
---

# Backfill best practices

> For various reasons, data may need to be backfilled, whether because of data errors, new information (such as new features), or reconciling data between two systems. When backfilling occurs, follow the principles in this article to maintain data quality and model performance.

## When backfilling is needed

Backfilling is the process of retroactively populating a dataset with historical data. Common scenarios include:

| Scenario | Description | Example |
|----------|-------------|---------|
| **New features** | You've identified a new metric that is important for your model, and you have the raw historical logs to compute it. | You add "click-through rate" as a feature and need three months of history so the model has enough data to learn from. |
| **Data recovery** | Your data pipeline failed on specific days, creating gaps in the data delivered to Decisioning Studio. | A pipeline outage on Tuesday left a gap. After the fix is deployed, you backfill those missing records from the source system. |
| **Logic changes** | You've updated the formula for a feature calculation or changed an event definition. | You redefined "active user" and need to re-export historical data so the model trains on the updated definition. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Requirements

For Decisioning Studio to function correctly, all incoming data must support backfilling for historical periods. The specific lookback window required (measured in months) depends on the AI model's training requirements. Consult your AI Decisioning Services team to confirm the correct value for your use case.

When performing a historical backfill, the following standards are mandatory:

- **Process consistency:** Historical feature snapshots must be generated using a process that is fully consistent with the creation of live snapshots. If your live pipeline applies any transformations, aggregations, or filters, those same steps must be applied to backfilled data.
- **Schema consistency:** The schema for backfilled data must precisely match the normal daily pipeline, including the same fields, data types, and column naming conventions.

## Common pitfalls

### Data leakage (look-ahead bias)

Data leakage is the most critical backfilling mistake. It occurs when the backfill process inadvertently incorporates information that would not have been available at the time the historical record was generated.

#### Why it matters 

If the model trains on data that "knows the future," it will appear to perform well during training but will produce poor results in production, because real-time decisions don't have access to future data.

For example, consider calculating a historical "lifetime value" feature using a customer's total spend to date (that is, up to today), then using that value to predict behavior that occurred months ago. At the time of that historical event, the full lifetime value wasn't yet known.

This can be avoided by always reconstruct historical features using only the information that would have been available at the historical timestamp, not information that accumulated afterwards.

### Schema and logic drift

Data structures and business definitions evolve over time. Inconsistencies between historical and live data can silently degrade model quality.

- **Schema drift:** If a field (for example, `zip_code`) was added to your database recently, backfilled records from before that change will contain nulls for that field. Ensure your pipeline handles missing fields gracefully and that the model is not overly dependent on fields with sparse historical coverage.
- **Logic drift:** If the definition of a metric changed at a specific point in time (for example, "active user" was redefined in 2024), applying the new definition uniformly to older data (for example, 2022 records) can create artificial spikes or drops that didn't actually occur. Where possible, apply the definition that was in effect at the time of each historical record, or clearly document the break point so the model can account for it.

### Duplicate records from failed backfill jobs

Backfill jobs that fail mid-run and are restarted can produce duplicate records if the process is not designed to prevent it. Duplicate records artificially inflate metrics and introduce noise into model training.

**The solution:** Design all backfill scripts to be idempotent: running the same job twice should produce the same result as running it once. Use one of the following patterns:

- **Upsert (update or insert):** Keyed on a unique transaction ID or timestamp, so re-inserting an existing record updates it rather than creating a duplicate.
- **Delete then insert:** Delete existing records for the target time range before inserting, so the dataset is always replaced cleanly.