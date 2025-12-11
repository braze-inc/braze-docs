---
page_order: 4.4
nav_title: Create the Feedback Loop
article_title: Create the Feedback Loop
description: "Learn how to create the feedback loop for Decisioning Studio Pro agents to enable self-learning."
---

# Create the Feedback Loop

> Finally, while all customer data is important for the agent, the *most important data assets* are those that tell the agent what happened after customer engagement decisions were sent.

Finally, while all customer data is important for the agent (and for information on how to configure, refer back to [Set Customer Context]({{site.baseurl}}/user_guide/brazeai/decisioning_studio_pro/set_customer_context/)), the *most important data assets* are those that tell the agent what happened after customer engagement decisions were sent.

These assets create the feedback loop that allows the agent to learn.

There are three critical assets for creating the feedback loop: conversions (including any relevant financial data, such as revenue); engagement data; and orchestration data. There are special requirements for each of these data assets.

{% alert note %}
Finally, note that while information on all three categories—conversions, engagement, and activations—is required for an agent to be successful, if the agent is natively integrated with the customer engagement platform, such as Braze, there may not be additional configuration steps necessary, since these may be sent with the customer data.
{% endalert %}

## Conversions Data

The conversion asset describes what happened to the customer after orchestration. For example, supposing an agent is optimizing on Net Present Value (NPV) for customers receiving optimized campaigns, the conversion asset might include a daily update of changes to NPV.

The conversion asset must meet the following requirements:

| Requirements | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to be able track the individual customer journey from recommendation, through activation, to conversion. |
| Each record has an associated timestamp. | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| If using a non-binary (e.g., converted vs. unconverted) target metric, the target metric value associated with each conversion is provided with each conversion event. | Decisioning Studio uses the target metric value to generate training experiences to appropriately reward/penalize the model based on the outcomes of the recommended actions. |
| If conversions can be uniquely attributed to communications (e.g., coupon redemption), fields needed to match conversions to activations are provided. | If a conversion event can be tied to a particular communication, this allows for clean and precise attribution. Direct attribution provides the clearest signal to the model, but if is not possible, as if often the case, proximity-based attribution will be used. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Engagement Data

The engagement asset describes what happened to the customer, including clicks, opens, and other impressions. Engagement data may be included in the conversion data or it may be separate. It plays a similar role as conversions data—telling the agent what happened after customer engagement.

The engagement asset must meet similar requirements to the conversion asset:

| Requirements | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to be able track engagement events for each individual customer. |
| Each record has an associated timestamp. | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| If clicks, opens or other engagement data can be uniquely attributed to communications (e.g., coupon redemption), fields needed to match conversions to activations are provided. | As with conversion data, if engagement can be tied to a particular communication, this allows for clean and precise attribution. Direct attribution provides the clearest signal to the model. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Activations Asset

The activations asset tells the agent which communications were sent. This is often necessary depending on how orchestration is configured. If the agent orchestrates via a direct integration with Braze, SFMC, or Klaviyo, then the agent may be able to pull activation data directly.

The activation asset must meet the following requirements:

| Requirements | Why? |
|-------------|------|
| Each record contains a unique customer identifier that is consistent with all data assets | Decisioning Studio needs to be able track the individual customer journey from recommendation, through activation, to conversion. |
| Each record has an associated timestamp. | Understanding the time between communication and sequence of customer actions is extremely important for model training and metric calculation. |
| Fields needed to match communication content to activation events are provided (e.g., event_id). | Correctly matching communication characteristics to sends is necessary for model attribution and training. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

