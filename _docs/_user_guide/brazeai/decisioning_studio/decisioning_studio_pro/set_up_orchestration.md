---
nav_title: Set up orchestration
article_title: Set up orchestration
page_order: 2
description: "Learn how to configure orchestration for Decisioning Studio Pro agents to enable personalized communications."
toc_headers: h2
---

# Set up orchestration

> Decisioning agents need to connect to a Customer Engagement Platform (CEP) to orchestrate communications once they have ingested customer data and personalized at a 1:1 level. This article explains how to set up the integration for each supported CEP.

## Supported CEPs

Decisioning Studio Pro supports the following Customer Engagement Platforms:

| CEP | Integration type | Setup complexity |
|-----|-----------------|------------------|
| **Braze** | Native API integration | Low (recommended) |
| **Salesforce Marketing Cloud** | Native API events + Journeys | Medium |
| **Klaviyo** | Native API events + Flows | Medium |
| **Other CEPs** | Custom (recommendation file) | High |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Select your CEP below to get started with the integration setup.

{% tabs %}
{% tab Braze %}

## Setting up Braze integration

Follow these steps to integrate a Braze Decisioning Studio agent with Braze's orchestration capabilities (Braze's services team will be available to help):

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

Decisioning Studio Pro supports native integration with Salesforce Marketing Cloud. Decisioning Studio triggers API events into a journey with data required to populate dynamic elements.

The orchestration setup for SFMC is similar for both Decisioning Studio Pro and Decisioning Studio Go. For detailed steps to configure the SFMC integration, follow the [SFMC instructions]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in the Decisioning Studio Go documentation.

{% endtab %}
{% tab Klaviyo %}

## Setting up Klaviyo integration

Decisioning Studio Pro supports native integration with Klaviyo. Decisioning Studio triggers API events into a flow with data required to populate dynamic elements.

The orchestration setup for Klaviyo is similar for both Decisioning Studio Pro and Decisioning Studio Go. For detailed steps to configure the Klaviyo integration, follow the [Klaviyo instructions]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in the Decisioning Studio Go documentation.

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

## Next steps

After setting up orchestration, proceed to design your agent:

- [Design your agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

