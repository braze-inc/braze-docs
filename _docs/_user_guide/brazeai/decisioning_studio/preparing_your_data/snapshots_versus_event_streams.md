---
nav_title: Snapshots versus event streams
article_title: Snapshots versus event streams
page_order: 3
page_type: reference
description: "This reference article explains the difference between snapshot data and event stream data, and how each should be structured and delivered to BrazeAI Decisioning Studio."
---

# Snapshots versus event streams

> Data falls into one of two fundamental categories: snapshots (state) and event streams (what happened). Understanding this distinction—and applying it correctly—is one of the most important things you can do to ensure your Decisioning Studio agent learns effectively.

## Snapshot data (state)

A snapshot represents the state of a customer at a specific point in time. It answers the question: "What does this customer look like right now?"

**Nature:** Static and aggregated. A snapshot reflects the cumulative result of all changes up to that moment.

**Best for:** Customer profiles, computed features (for example, "days since last purchase," "loyalty tier," "churn score")

### Required fields

| Field | Purpose |
|-------|---------|
| Customer identifier | Who this record describes |
| Snapshot date | When this snapshot was taken |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### How snapshots should be updated

- **Trigger:** Time-driven, not event-driven. Snapshots should be generated on a fixed schedule (for example, daily), regardless of whether a customer had any activity on that day.
- **Scope:** Every update must include all relevant customers, not just those who had an event.
- **Method:** Append new snapshot records to the dataset rather than overwriting previous values. This preserves historical state for model training.

### Querying snapshot data for daily delivery

Decisioning Studio runs its recommendation pipeline once per day. When delivering snapshot data, export the previous day's snapshot at each pipeline run:

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## Event stream data (flow)

An event stream records discrete actions as they happen. It answers the question: "What did this customer do, and when?"

**Nature:** Raw, immutable, incremental, and chronological. Each record represents one thing that happened at a specific time.

**Best for:** Activation records, engagement logs (opens, clicks), conversion events, coupon redemptions

### Required fields

| Field | Purpose |
|-------|---------|
| Customer identifier | Who this event is about |
| Event type | What happened (for example, activation, conversion, click) |
| Event timestamp | When the event actually occurred |
| Creation timestamp | When this record was created in your system (see note below) |
| Event properties | Additional metadata about the event; the richer this is, the better Decisioning Studio can link events across the customer journey |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
The event timestamp and creation timestamp are different fields and both are required. The event timestamp records when the action actually happened. The creation timestamp records when the data entry was written to your system, which may be later due to processing delays. Do not conflate the two.
{% endalert %}

### How event streams should be updated

- **Trigger:** Event-driven. New records are added when new events occur.
- **Scope:** Only customers who had an event get new records.
- **Method:** Existing records are immutable. Updates are always inserts of new records.

### Querying event data for daily delivery

**Use `create_timestamp`, not `event_timestamp`, to slice daily exports.** Events are sometimes written to your system after they occur (late arrivals). If you slice on `event_timestamp`, those late-arriving records will be permanently missed.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

For example: if an event occurred on January 1st but wasn't written to your system until January 2nd, slicing by `event_timestamp` on January 2nd would miss it entirely. Slicing by `create_timestamp` captures it correctly.

## For native Braze integrations

Braze provides two built-in mechanisms that map directly to these two data types.

### Custom Attributes — snapshot data

Custom Attributes store user-level state at a point in time. They are the correct vehicle for customer profiles and computed features (for example, `churn_score`, `total_purchases_last_30d`). They are **not** suitable for raw event data, because they overwrite rather than accumulate.

### Braze Currents — event stream data

Braze Currents provides raw, immutable event flow data. The `USER_BEHAVIOR_CUSTOM_EVENTS` table captures every instance of a custom event as it occurs, making it the correct source for activation, engagement, and conversion events.

{% alert tip %}
Treat Custom Attributes as the source of customer state and Braze Currents as the source of customer behavior events. Do not use Custom Attributes to pass raw event data to Decisioning Studio.
{% endalert %}

## Common pitfalls

### Pitfall 1: Passing event data as a snapshot

Aggregating event data into snapshot fields before sending it to Decisioning Studio causes several problems:

- **Loss of granularity:** Once data is aggregated to a daily customer-level summary, the individual event records are gone. Decisioning Studio cannot reconstruct them.
- **Imprecise timestamps:** A field like "last_email_sent" tells you the most recent occurrence but loses the full history of events and makes precise attribution impossible.
- **Phantom updates:** Even on days when no events occurred, the snapshot record is updated, creating duplicate entries that are difficult to deduplicate.

If you're using Braze, use Currents exports (not Custom Attributes) to deliver raw event data to Decisioning Studio.

### Pitfall 2: Updating snapshot data on an event trigger

Some implementations update snapshot data only when an event occurs—for example, recalculating a feature only when a customer makes a purchase. This causes features that depend on the passage of time to become stale for customers who haven't had a recent event.

For example, a feature like `days_since_last_purchase` has a different correct value every single day. If it's only recalculated when a purchase occurs, it will be frozen at an incorrect value for all customers who haven't purchased recently. Always update snapshot data on a time-driven schedule that covers all customers, every day.
