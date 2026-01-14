---
nav_title: Preparing your orchestration
article_title: Preparing your orchestration
page_order: 3
page_type: reference
description: "This reference article explains what you need to prepare before setting up orchestration for BrazeAI Decisioning Studio, including choosing your CEP and gathering the required credentials and assets."
---

# Preparing your orchestration

> This reference article explains what you need to prepare before setting up orchestration for BrazeAI Decisioning Studio™, including choosing your Customer Engagement Platform (CEP) and gathering the required credentials and assets.

## What is orchestration?

Orchestration is the connection between Decisioning Studio and your Customer Engagement Platform (CEP). Once your decisioning agent determines the optimal action for each customer, orchestration carries out those decisions by triggering personalized communications through your CEP.

Think of it this way:
- **Decisioning Studio** decides *what* to send and *when* to send it
- **Your CEP** handles *how* to send it

## Choosing your CEP

The first step is to determine which Customer Engagement Platform you'll use with Decisioning Studio. Your choice affects setup complexity and available features.

### Supported CEPs

| CEP | Decisioning Studio Go | Decisioning Studio Pro | Integration Type |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Native API integration (recommended) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | API events + Journey Builder |
| **Klaviyo** | ✓ | ✓ | API events + Flows |
| **Other CEPs** | — | ✓ | Custom (recommendation file) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
If you're already using Braze as your CEP, we recommend using the native Braze integration for the smoothest setup experience.
{% endalert %}

## What you'll need to prepare

Before setting up orchestration, gather the following items based on your chosen CEP.

{% tabs %}
{% tab Braze %}

| Item | Description |
|------|-------------|
| **REST API key** | A new API key with permissions for user data, messages, campaigns, Canvas, segments, and templates. |
| **Braze dashboard URL** | Your Braze instance URL (for example, `https://dashboard-01.braze.com`). |
| **App ID** | The API key associated with the app you want to track (found in **Settings** > **App Settings**). |
| **Email display name and address** | The sender information to use for your campaigns (found in **Settings** > **Email Preferences**). |
| **Base templates** | The message templates your agent will use for orchestration. You'll create API-triggered campaigns for each template. |
| **Test user ID** | A user ID for testing the integration before launch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Item | Description |
|------|-------------|
| **App package credentials** | Client ID, Client Secret, Authentication Base URI, REST Base URI, and SOAP Base URI from an installed package with server-to-server API integration. |
| **API permissions** | Scopes for channels, assets, automations, journeys, contacts, data extensions, and tracking events. |
| **Data extensions** | You'll need data extensions for subscriber data, engagement data, and recommendations. |
| **Email templates** | The templates you want Decisioning Studio to use, with template IDs for each. |
| **Journey Builder access** | Access to create and activate multi-step journeys with API event entry sources. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Item | Description |
|------|-------------|
| **Private API key** | A new API key with full access permissions for events, flows, lists, metrics, profiles, and templates. |
| **Email templates** | The templates you want Decisioning Studio to use. Templates must be associated with a flow (you can create a placeholder flow for this purpose). |
| **Sender information** | The sender name and email address to use for your campaigns. |
| **Flow access** | Access to create and activate flows with metric triggers. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Custom CEP integrations are only available with Decisioning Studio Pro.
{% endalert %}

If you're using a CEP other than Braze, SFMC, or Klaviyo, Decisioning Studio Pro can integrate through a recommendation file approach:

| Item | Description |
|------|-------------|
| **Data ingestion capability** | Your CEP must be able to ingest recommendation files (typically CSV or JSON) containing personalized decisions for each customer. |
| **Dynamic content support** | Your campaigns must support populating fields dynamically based on recommendation data. |
| **Custom engineering resources** | Your team will need to build the integration to read recommendation files and trigger communications. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planning your campaigns

Before setting up orchestration, consider the following:

### Base templates

A base template is any message template that your decisioning agent might use. Consider:

- **How many templates?** Your agent can work with one template or multiple. If multiple, the agent can personalize which template each customer receives.
- **What channels?** Email, push, SMS, or a combination. Each channel may require separate templates and campaigns.
- **What dynamic elements?** Identify which parts of your message the agent will personalize (subject lines, CTAs, offers, timing, etc.). These will become API trigger properties or dynamic placeholders.

### Re-eligibility settings

Your campaigns should allow users to receive messages multiple times:

- For testing, you'll want to send the same campaign to the same user repeatedly
- In production, the agent may determine the same campaign is optimal for a user on consecutive days

{% alert note %}
While setting up re-eligibility for testing, Decisioning Studio agents are designed to respect frequency caps and will not send the same campaign to a user more than once per day in production.
{% endalert %}

### API trigger properties

For Braze integrations, plan which dimensions your agent will optimize. These become API trigger properties that pass dynamic values into your campaigns:

| Example dimension | API trigger property |
|-------------------|---------------------|
| Subject line | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Call to action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Offer | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Discount amount | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Best practices

Keep these best practices in mind as you prepare for orchestration:

1. **Start simple.** Begin with one channel and one or two templates. You can expand later as you learn what works.

2. **Test thoroughly.** Before launching, test your integration with a small set of users to verify that dynamic content populates correctly.

3. **Document your setup.** Keep track of campaign IDs, template IDs, API keys, and other identifiers. You'll need to reference these in the Decisioning Studio portal.

4. **Coordinate with your team.** Orchestration setup may involve marketing, engineering, and data teams. Ensure everyone understands their role in the process.

5. **Plan for feedback data.** Orchestration isn't just about sending messages—it's also about collecting the engagement and conversion data that helps your agent learn. See [Preparing your data sources]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/) for more details.

## Next steps

Once you've gathered your credentials and planned your campaigns, you're ready to set up orchestration:

- [Decisioning Studio Go: Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

