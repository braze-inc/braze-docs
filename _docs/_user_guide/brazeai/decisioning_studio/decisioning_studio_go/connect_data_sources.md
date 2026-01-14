---
nav_title: Connect data sources
article_title: Connect data sources
page_order: 1
description: "Learn how BrazeAI Decisioning Studio Go connects to your customer data through your Customer Engagement Platform."
---

# Connect data sources

> BrazeAI Decisioning Studio™ Go connects to your customer data through your Customer Engagement Platform (CEP). This article explains what data is used and how the connection works.

## How Go accesses customer data

Unlike Decisioning Studio Pro, which supports direct data integrations with various sources, Decisioning Studio Go accesses customer data through your CEP. This means:

- **Audience data** is pulled directly from segments or lists defined in your CEP (Braze, Salesforce Marketing Cloud, or Klaviyo)
- **Engagement data** (opens, clicks, sends) is captured through automated queries or native integrations with your CEP
- **No additional data pipeline setup** is required beyond what you configure in your CEP

## Supported integration patterns

Decisioning Studio Go supports the following CEPs for data access:

| CEP | Audience Source | Engagement Data |
|-----|-----------------|-----------------|
| **Braze** | Segments | Braze Currents export |
| **Salesforce Marketing Cloud** | Data Extensions | SQL Query Automation |
| **Klaviyo** | Segments | Native API integration |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Data requirements by CEP

{% tabs %}
{% tab Braze %}

### Braze data requirements

For Braze integrations, Decisioning Studio Go requires:

1. **Braze Currents**: You must have Braze Currents enabled and configured to export engagement data to Decisioning Studio Go. This allows the agent to learn from customer responses.

2. **Segment access**: The API key you create must have permissions to access segments that define your target audience.

3. **User profile data**: Any user profile attributes or custom attributes you want the agent to consider must be accessible through the Braze API.

{% alert important %}
Make sure your Braze Currents export includes data from any campaigns you want to compare against (including BAU campaigns).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC data requirements

For Salesforce Marketing Cloud integrations, Decisioning Studio Go requires:

1. **Data Extensions**: Your audience must be defined in a Data Extension that Decisioning Studio Go can access.

2. **SQL Query Automation**: You'll set up automated SQL queries to export subscriber and engagement data to Data Extensions that Decisioning Studio Go reads daily.

3. **Tracking Events access**: The app package you configure must have permissions to read tracking events (opens, clicks, sends).

The data extensions and SQL queries are configured as part of the [orchestration setup]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% tab Klaviyo %}

### Klaviyo data requirements

For Klaviyo integrations, Decisioning Studio Go requires:

1. **Segment access**: Your audience must be defined as a Klaviyo segment that the API key can access.

2. **Profile data**: The API key must have Full Access to Profiles to read customer attributes.

3. **Metrics access**: The API key must have Full Access to Metrics and Events to capture engagement data.

{% endtab %}
{% endtabs %}

## Best practices

- **Enrich your customer profiles**: The more information available in your CEP about your customers, the better the agent can personalize. Consider adding behavioral data, purchase history, and preference attributes to your customer profiles.
- **Keep data fresh**: Ensure your audience segments and customer data are updated regularly (at minimum, daily) so the agent works with current information.
- **Include relevant attributes**: Think about what customer characteristics might influence which messages resonate—demographics, engagement history, purchase behavior, and lifecycle stage are all valuable signals.

## Next steps

Now that you understand how Go connects to data, proceed to set up your CEP integration:

- [Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

