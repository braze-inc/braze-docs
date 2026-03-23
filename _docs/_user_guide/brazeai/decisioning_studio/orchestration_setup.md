---
nav_title: Set up orchestration
article_title: Set up orchestration
page_order: 4
page_type: reference
description: "This article explains how to set up orchestration for BrazeAI Decisioning Studio, including choosing your CEP, gathering required credentials, and configuring your integration."
toc_headers: h2
---

# Set up orchestration

> Decisioning agents need to connect to a customer engagement platform (CEP) to orchestrate communications once they have ingested customer data and personalized at a 1:1 level. This article covers what you need to prepare and how to configure the integration for each supported CEP.

## What is orchestration?

Orchestration is the connection between Decisioning Studio and your customer engagement platform (CEP). Once your decisioning agent determines the optimal action for each customer, orchestration carries out those decisions by triggering personalized communications through your CEP.

Think of it this way:

- **Decisioning Studio** decides *what* to send and *when* to send it
- **Your CEP** handles *how* to send it

## Choose your CEP

The first step is to choose which CEP to use with Decisioning Studio. Your choice affects setup complexity and available features.

### Supported CEPs

| CEP | Integration type | Setup complexity |
|-----|-----------------|------------------|
| **Braze** | Native API integration (recommended) | Low |
| **Salesforce Marketing Cloud** | API events + Journey Builder | Medium |
| **Klaviyo** | API events + Flows | Medium |
| **Other CEPs** | Custom (recommendation file) | High |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
If you're already using Braze as your CEP, we recommend using the native Braze integration for the smoothest setup experience.
{% endalert %}

## Prerequisites

Before setting up orchestration, gather the following items based on your chosen CEP.

{% tabs %}
{% tab Braze %}

| Requirement | Description |
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

| Requirement | Description |
|------|-------------|
| **App package credentials** | Client ID, Client Secret, Authentication Base URI, REST Base URI, and SOAP Base URI from an installed package with server-to-server API integration. |
| **API permissions** | Scopes for channels, assets, automations, journeys, contacts, data extensions, and tracking events. |
| **Data extensions** | You'll need data extensions for subscriber data, engagement data, and recommendations. |
| **Email templates** | The templates you want Decisioning Studio to use, with template IDs for each. |
| **Journey Builder access** | Access to create and activate multi-step journeys with API event entry sources. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Requirement | Description |
|------|-------------|
| **Private API key** | A new API key with full access permissions for events, flows, lists, metrics, profiles, and templates. |
| **Email templates** | The templates you want Decisioning Studio to use. Templates must be associated with a flow (you can create a placeholder flow for this purpose). |
| **Sender information** | The sender name and email address to use for your campaigns. |
| **Flow access** | Access to create and activate flows with metric triggers. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

If you're using a CEP other than Braze, SFMC, or Klaviyo, Decisioning Studio can integrate through a recommendation file approach:

| Item | Description |
|------|-------------|
| **Data ingestion capability** | Your CEP must be able to ingest recommendation files (typically CSV or JSON) containing personalized decisions for each customer. |
| **Dynamic content support** | Your campaigns must support populating fields dynamically based on recommendation data. |
| **Custom engineering resources** | Your team will need to build the integration to read recommendation files and trigger communications. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planning your campaigns

Before setting up orchestration, consider the following details:

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

## Integration setup

Select your CEP below to get started with the integration setup.

{% tabs %}
{% tab Braze %}

## Setting up Braze integration

Follow these steps to integrate a Decisioning Studio agent with Braze's orchestration capabilities (Braze's services team will be available to help):

### Step 1: Create an API key

Go to **Settings** > **API Keys**, then create a new key with the following permissions:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Step 2: Set up API-triggered campaigns

Set up an API-triggered campaign for each base template with API trigger properties for all optimized dimensions.

A base template is any template that the Decisioning Agent might use for orchestrating messages. A Decisioning Agent might have 1 base template or multiple, in which case choosing the right base template for each customer will be one of the decisions the agent personalizes.

### Step 3: Configure re-eligibility

Ensure all API-triggered campaigns allow users to become re-eligible within 15 minutes.

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
While the Decisioning Studio agent will never send the same campaign more than once a day, you will want to have the ability to send the same campaigns multiple times in a day for testing purposes.
{% endalert %}

### Step 4: Add dynamic placeholders

These serve as dynamic placeholders for decisions that the Decisioning Studio agent is optimizing.

#### Example 1: Email Campaign

Suppose the Decisioning Studio agent is optimizing an email campaign. This might be configured like this:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supposing the agent is optimizing for choice of templates and Call to Action (CTA) message, then an API-triggered campaign should be created for each template, and the CTA section of one template might look like:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Example 2: Push campaign

Suppose a Decisioning Studio agent is optimizing the message of a Push campaign. This might be configured like this:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resulting in the following message:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Example 3: SMS Campaign

Suppose that the Decisioning Studio agent is optimizing for fields in an SMS campaign. This might be configured like this:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resulting in the following message:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Setting up SFMC integration

Decisioning Studio supports native integration with Salesforce Marketing Cloud. Decisioning Studio triggers API events into a journey with data required to populate dynamic elements.

For detailed steps to configure the SFMC integration, follow the [SFMC instructions]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in the Decisioning Studio Go documentation.

{% endtab %}
{% tab Klaviyo %}

## Setting up Klaviyo integration

Decisioning Studio supports native integration with Klaviyo. Decisioning Studio triggers API events into a flow with data required to populate dynamic elements.

For detailed steps to configure the Klaviyo integration, follow the [Klaviyo instructions]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in the Decisioning Studio Go documentation.

{% endtab %}
{% tab Other CEPs %}

## Setting up other CEP integrations

Decisioning Studio can integrate with any customer engagement platform. However, this may require some custom engineering work from your team, since Decisioning Studio cannot trigger communications directly.

In this scenario, the agent will deliver a "recommendation file." This file contains rows for each customer, with columns that indicate all of the personalized decisions for that customer.

For example, the following recommendation file:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Might be used to optimize an email campaign that looks like the following:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Best practices

Keep these best practices in mind as you prepare for orchestration:

1. **Start simple.** Begin with one channel and one or two templates. You can expand later as you learn what works.
2. **Test thoroughly.** Before launching, test your integration with a small set of users to verify that dynamic content populates correctly.
3. **Document your setup.** Keep track of campaign IDs, template IDs, API keys, and other identifiers. You'll need to reference these in the Decisioning Studio portal.
4. **Coordinate with your team.** Orchestration setup may involve marketing, engineering, and data teams. Ensure everyone understands their role in the process.
5. **Plan for feedback data.** Orchestration isn't just about sending messages—it's also about collecting the engagement and conversion data that helps your agent learn. See [Preparing your data]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data/) for more details.

## Next steps

After setting up orchestration, proceed to design your agent:

- [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)