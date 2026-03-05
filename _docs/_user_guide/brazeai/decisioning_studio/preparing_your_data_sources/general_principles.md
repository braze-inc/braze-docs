---
nav_title: General principles
article_title: General data principles for Decisioning Studio
page_order: 1
page_type: reference
description: "This reference article covers the general data principles that apply to all data assets used by BrazeAI Decisioning Studio."
---

# General principles

> Well-structured data is the foundation of an effective Decisioning Studio agent. Before diving into specific asset requirements, it helps to understand the four core principles that apply across all data you send to Decisioning Studio. Violations of any of these principles are among the most common causes of degraded model performance.

## One consistent customer identifier across all assets

Every data asset—customer profiles, activations, engagements, conversions—must reference the same customer identifier. There should be exactly one primary identifier that uniquely and consistently identifies each customer across all assets.

| Requirement | Implication if violated |
|-------------|------------------------|
| A single, unique customer identifier must be present in every asset | If different assets use different ID systems (for example, a warehouse ID for features but a platform ID for activations), the Decisioning Studio engine cannot reliably join them. This breaks the feedback loop and degrades both model training and reporting accuracy. If the mapping between the two ID systems turns out to be many-to-many rather than one-to-many, the resulting data integrity failures can be severe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

See [Using Braze External ID]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/using_braze_external_id/) for guidance on which identifier to use.

## Event data must be passed as an incremental stream, not as a snapshot

Events—such as conversions, engagements, and activations—represent discrete things that happened at a specific point in time. They must be delivered to Decisioning Studio as an incremental (append-only) stream of individual records, not as an aggregated snapshot.

| Requirement | Implication if violated |
|-------------|------------------------|
| Event data must be structured as individual, timestamped records and delivered incrementally | When event data is aggregated into a snapshot (for example, storing a "last send time" attribute rather than individual send records), you lose the precise timing of each event. This makes it impossible to accurately attribute outcomes to specific decisions, breaking the feedback loop that the model needs to learn. Without precise event timestamps, you cannot know exactly when a conversion happened or which recommendation triggered it. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

See [Snapshots versus event streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/snapshots_versus_event_streams/) for a full explanation of the distinction and examples of correct and incorrect patterns.

## Snapshot data must be updated on a regular, time-driven schedule

Snapshot data (such as customer profiles and features) represents the current state of a customer at a given point in time. Updates to snapshot data should be driven by a regular schedule (for example, daily), not by event triggers.

| Requirement | Implication if violated |
|-------------|------------------------|
| Snapshots must be updated for all customers on a regular schedule, regardless of whether a customer had an event on that day | If snapshot updates are only triggered when an event occurs, features that depend on the passage of time (such as "days since last purchase" or "days since enrollment") will become stale for customers who haven't had a recent event. The model will be training on outdated feature values, which reduces its ability to make accurate, timely recommendations. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## All assets must meet minimum data quality and integrity requirements

Beyond structure, the data itself must be internally consistent and complete enough to be useful.

| Requirement | Implication if violated |
|-------------|------------------------|
| Each asset must contain the fields needed to establish a primary key and, where applicable, join keys to other assets. Duplicate records must be removed or deduplicated before ingestion. | Duplicate or unmatchable records add noise to model training and can cause incorrect attribution. Missing keys prevent the engine from linking events across the customer journey from recommendation through to conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

For event stream data specifically, each record must include at minimum:

**Required fields:**
- Customer identifier
- Timestamp of when the event occurred (not when the record was created in your system—these are different; see [Snapshots versus event streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/snapshots_versus_event_streams/) for why this matters)
- Timestamp of when the record was created in your system (used for reliably slicing incremental exports)
- Event type
- Fields sufficient to filter down to the specific events you care about

**Recommended fields:**
- Additional event metadata that allows reliable matching between event types (for example, linking a conversion event back to the specific activation that preceded it)
