---
nav_title: Choosing good features
article_title: Choosing good features for Decisioning Studio
page_order: 5
page_type: reference
description: "This reference article covers how to construct effective customer features for BrazeAI Decisioning Studio, including feature types, general guidelines, behavioral feature construction, and the relationship between features and the action space."
---

# Choosing good features

> Customer features are the inputs the Decisioning Studio model uses to make individualized recommendations. High-quality features that are well-matched to your decision space are one of the most impactful levers for improving model performance. This article covers the types of features you can provide, how to construct them well, and how to think about aligning features with the actions your agent will be choosing between.

If you have internal data science or data engineering teams, they are best positioned to construct and curate features, since they have the most context about which signals in your data are meaningful.

{% alert note %}
For Braze customers, customer features are typically passed to Decisioning Studio through Custom Attributes on user profiles. For details on Custom Attributes versus Custom Events and their respective update strategies, see [Snapshots versus event streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/snapshots_versus_event_streams/).
{% endalert %}

## Types of customer features

There are four common categories of customer features:

| Feature type | What it captures | Examples |
|-------------|-----------------|---------|
| **User profiling** | Objective facts about the customer's status | `age`, `loyalty_tier`, `days_enrolled`, `city`, `acquisition_channel` |
| **User propensity** | Model-derived scores for the customer's likelihood to do something | `churn_risk_score`, `purchase_intent_score`, `upsell_affinity` |
| **User behavioral** | Summaries of customer activity over a time window | `clicks_past_30d`, `purchases_past_7d`, `app_logins_past_14d` |
| **Environmental** | Contextual signals external to the customer | `is_promotional_period`, `is_holiday`, `regional_economic_index` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Together, these feature types give the model the information it needs to identify segments, distinguish between customers, and adapt recommendations accordingly.

## General guidelines

Keep the following in mind when selecting and constructing features:

- **Coverage:** Features should cover all customers in your target audience. A feature that is missing or null for a large portion of your audience gives the model less to work with for those customers.
- **Granularity:** All features should be aggregated to the customer level. See [Using Braze External ID]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/using_braze_external_id/) for guidance on what "customer level" means in practice.
- **Freshness:** Features should be updated on a time-driven schedule, not an event-driven one. See [Snapshots versus event streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/snapshots_versus_event_streams/) for why this matters.
- **Validity:** Feature values should fall within ranges that make sense given the definition. A feature for "purchases in the last 30 days" should never be negative.
- **Sparsity:** Avoid features that are zero or null for the vast majority of customers, unless there is a clear business reason. Sparse features add noise without adding signal.
- **Correlation:** Avoid including features that are highly correlated with each other. Redundant features can introduce bias and slow down training without improving predictions.

## Constructing behavioral features

Behavioral features summarize a customer's history of actions over a defined time window (for example, "number of purchases in the last 28 days"). These are among the most valuable features for a recommendation system because they capture how a customer actually behaves, not just who they are.

### Choosing time windows

The right time window depends on how frequently customers take the action you're measuring:

- **Short windows (7–28 days):** Use for high-frequency activities such as app logins, email opens, or website visits.
- **Long windows (90–365 days):** Use for infrequent activities such as product purchases, subscription renewals, or customer service contacts.

A useful diagnostic: if a large percentage of your feature values are zero, the time window is probably too short. Widen it until you see meaningful variance across customers.

### Choosing aggregations

- **For events without a value** (something either happened or it didn't): use **count** aggregations. For example, `email_opens_past_30d`.
- **For events with an associated value** (revenue, duration, quantity): use both **sum** and **average** aggregations. For example, `purchase_value_sum_past_90d` and `purchase_value_avg_past_90d`. These provide complementary information about total volume and per-event magnitude.

## Aligning features with the action space

Decisioning Studio is not a propensity model—it is a ranking system. Its goal is to identify, for each customer, which action from a defined set of options is most likely to produce the best outcome. This creates a specific requirement: **features should, where possible, give the model information that helps it distinguish between the available options for a given customer.**

### Why this matters

Consider a simple example. Suppose your agent's action space is recommending one of three menu items: coffee, black tea, or bubble tea.

If your features describe customers at a high level—"orders drinks frequently" or "high email engagement"—the model can segment customers into broad groups. But when it comes to ranking coffee versus bubble tea for a specific customer, broad features don't help much. Two customers can look identical on high-level features but have completely opposite preferences.

When the model encounters contradictory signals—recommending coffee to two seemingly similar customers but only one converts—it cannot learn effectively. The noise reduces its ability to make accurate rankings.

### Building features that match the action space

Features that map to the same granularity as your action space give the model much stronger ranking signals. In the café example, a feature like `coffee_orders_past_14d` directly tells the model whether a customer prefers coffee. A feature like `black_tea_orders_past_14d` does the same for black tea. The model can now make a well-informed ranking decision.

With action-aligned features, the model can also detect saturation and fatigue. If a customer has a high `coffee_orders_past_14d` value but didn't convert on a recent coffee recommendation, the model learns that recommending coffee again may not be the best choice—and starts testing alternatives.

### When exact alignment isn't available

Exact feature-to-action alignment is the ideal, but it is often constrained by data availability. Two approaches can help when you can't build perfectly aligned features:

**Data summarization:** If you can't distinguish between black tea and bubble tea purchases, use an aggregated `tea_orders_past_14d` feature. This loses some precision but still helps the model distinguish tea-preferring customers from coffee-preferring ones.

**Indirect signals:** Features that aren't directly in the action space can still be valuable if they have a logical relationship to it. For example, `dessert_purchased_past_30d` is a reasonable proxy for preference for sweet items, which is likely correlated with bubble tea preference. The model can learn from these indirect signals even without a direct feature match.

The underlying principle is that more relevant and granular information always helps, but the model can still learn from imperfect features. Start with what you have, and refine over time as more data becomes available.
