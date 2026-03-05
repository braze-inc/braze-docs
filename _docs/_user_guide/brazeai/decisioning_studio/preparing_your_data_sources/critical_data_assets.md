---
nav_title: Critical data assets
article_title: Critical data assets for Decisioning Studio
page_order: 2
page_type: reference
description: "This reference article covers the required and optional data assets for BrazeAI Decisioning Studio, including the feedback data needed to close the AI decisioning loop."
---

# Critical data assets

> Decisioning Studio requires certain data assets to function, and benefits from additional optional data. This article describes what each asset is, why it matters, and what fields are required.

## Closing the AI decisioning loop

The three required event assets—activations, engagements, and conversions—together form the feedback loop that allows Decisioning Studio to learn and improve over time.

- **Activations** tell the model what it decided to do
- **Engagements** tell the model how customers responded to the message
- **Conversions** tell the model whether the ultimate business outcome was achieved

Each of these must be structured as an incremental event stream (not a snapshot). See [Snapshots versus event streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/snapshots_versus_event_streams/) for details.

{% alert note %}
If Decisioning Studio is natively integrated with your customer engagement platform (Braze, Salesforce Marketing Cloud, or Klaviyo), activation and engagement data may be collected automatically without additional configuration. Consult your setup documentation to confirm.
{% endalert %}

## Required assets

### Customer profile

Customer profile data describes who your customers are. Decisioning Studio uses this data to understand the current state of each customer and generate relevant recommendations.

Common profile attributes include:

- Years as a customer
- Geography (where permitted by your industry and privacy requirements)
- Acquisition channel (for example, web, phone, in-store)
- Satisfaction or sentiment score
- Model-derived scores (for example, churn propensity, lifetime value estimate)
- Loyalty tier or program membership

### Activation and engagement data

Activation data records what Decisioning Studio actually sent—which recommendation was delivered to which customer through which channel. Engagement data records what the customer did in response: whether they opened, clicked, or otherwise interacted with the message.

For native Braze integrations, activation and engagement data may be available automatically through Braze Currents. For other configurations, this data must be provided explicitly.

This data is critical because it closes the loop between a recommendation and its outcome. Without it, the model cannot learn which decisions are working.

### Conversions data

Conversion data describes what happened to the customer after a recommendation was made and a message was sent. This is the primary signal the model uses to evaluate whether a recommendation was successful.

| Requirement | Reason |
|-------------|--------|
| Each record contains the customer identifier, consistent with all other assets | Decisioning Studio must be able to join conversions to the recommendations that preceded them. |
| Each record has a timestamp for when the conversion event occurred | Accurate timing is essential for attribution—the model needs to know which recommendation a conversion can be attributed to. |
| If using a non-binary success metric (for example, revenue rather than converted/not converted), the metric value must be included with each conversion record | Decisioning Studio uses the metric value to generate training experiences. Without the value, the model can only learn that a conversion happened, not how valuable it was. |
| If conversions can be directly attributed to a specific communication (for example, coupon redemption), include the fields needed to match the conversion to the activation record | Direct attribution gives the model the clearest learning signal. If direct attribution is not possible, Decisioning Studio uses proximity-based attribution as a fallback. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Optional assets

More data generally leads to better model performance, but should be balanced against the implementation effort required. The following optional assets are commonly useful:

### Customer behavior

- Account login history
- Device type and operating system
- Customer service interactions (for example, number of support calls, topics discussed)
- Product usage (for example, hours used per day, features accessed, content categories viewed)

### Other transactions

- Products purchased by date, including product attributes
- Transaction amounts
- Transaction channels (for example, in-store versus online)
- Payment methods

### Other marketing engagement

- Outbound communications sent outside of Decisioning Studio recommendations (for example, emails, SMS)
- Email engagement not triggered by Decisioning Studio (for example, opens, clicks)
- Survey responses (for example, NPS scores, engagement surveys)
- Web and mobile app activity (for example, pages browsed, products viewed)
