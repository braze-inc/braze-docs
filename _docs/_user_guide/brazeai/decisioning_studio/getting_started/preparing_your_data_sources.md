---
nav_title: Preparing your data sources
article_title: Preparing your data sources
page_order: 2
page_type: reference
description: "This reference article covers the critical feedback data assets needed to close the AI decisioning loop and enable your agent to continuously learn and improve."
---

# Preparing your data sources

> This reference article covers the critical feedback data assets needed to close the AI decisioning loop and enable your agent to continuously learn and improve.

## Closing the AI decisioning loop

While all customer data is important for the agent (see [Connect data sources]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), the *most important data assets* are those that tell the agent what happened after customer engagement decisions were sent.

These assets create the feedback loop that allows the agent to learn.

{% alert note %}
If the agent is natively integrated with the customer engagement platform (such as Braze, SFMC, or Klaviyo), there may not be additional configuration steps necessary for feedback data, since these may be sent automatically with the customer data.
{% endalert %}

## Critical feedback data assets

There are three critical assets for creating the feedback loop:

### 1. Conversions data

The conversion asset describes what happened to the customer after orchestration. For example, supposing an agent is optimizing on Net Present Value (NPV) for customers receiving optimized campaigns, the conversion asset might include a daily update of changes to NPV.

| Requirement | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to track the individual customer journey from recommendation, through activation, to conversion. |
| Each record has an associated timestamp | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| If using a non-binary (e.g., converted vs. unconverted) target metric, the target metric value is provided with each conversion event | Decisioning Studio uses the target metric value to generate training experiences to appropriately reward/penalize the model based on the outcomes of the recommended actions. |
| If conversions can be uniquely attributed to communications (e.g., coupon redemption), fields needed to match conversions to activations are provided | If a conversion event can be tied to a particular communication, this allows for clean and precise attribution. Direct attribution provides the clearest signal to the model, but if not possible (as is often the case), proximity-based attribution will be used. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 2. Engagement data

The engagement asset describes customer interactions, including clicks, opens, and other impressions. Engagement data may be included in the conversion data or may be separate. It plays a similar role as conversions data—telling the agent what happened after customer engagement.

| Requirement | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to track engagement events for each individual customer. |
| Each record has an associated timestamp | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| If clicks, opens, or other engagement data can be uniquely attributed to communications, fields needed to match engagement to activations are provided | As with conversion data, if engagement can be tied to a particular communication, this allows for clean and precise attribution. Direct attribution provides the clearest signal to the model. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3. Activations data

The activations asset tells the agent which communications were sent. This is often necessary depending on how orchestration is configured. If the agent orchestrates via a direct integration with Braze, SFMC, or Klaviyo, then the agent may be able to pull activation data directly.

{% alert note %}
Engagement data and activations data are very commonly found in the same data asset.
{% endalert %}

| Requirement | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to track the individual customer journey from recommendation, through activation, to conversion. |
| Each record has an associated timestamp | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| Fields needed to match communication content to activation events are provided (e.g., event_id) | Correctly matching communication characteristics to sends is necessary for model attribution and training. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

