---
page_order: 4.3
nav_title: Configure Orchestration
article_title: Configure Orchestration
description: "Learn how to configure orchestration for Decisioning Studio Pro agents to enable personalized communications."
---

# Configure Orchestration

Decisioning agents need some means to orchestrate communications once they have ingested customer data and personalized at a 1:1 level.

While Decisioning Studio integrates most smoothly with Braze's orchestration capabilities, Decisioning Studio also supports native (code-free) integrations Salesforce Marketing Cloud (SFMC) and Klaviyo. Custom integrations can also be configured with any other customer engagement platform (CEP).

{% alert note %}
The Decisioning Studio team is currently building even more seamless integrations between Decisioning Studio and Braze orchestration. This documentation will be updated as these steps are simplified.
{% endalert %}

## If Customer Engagement Platform is Braze (Best case scenario)

Follow these steps to integrate a Braze Decisioning Studio agent with Braze's orchestration capabilities (and Braze's services team will be able to help):

### Step 1: Create an API key

Go to **Settings** > **API Keys**, then create a new key with the following permissions:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Step 2: Set up API-triggered campaigns

Set up an API-triggered campaign for each base template with API trigger properties for all optimized dimensions.

A base template is any template that the Decisioning Agent might use for orchestrating messages. A Decisioning Agent might have 1 base template and multiple, in which case choosing the right base template for each customer will be one of the decisions the agent personalizes.

### Step 3: Configure re-eligibility

Ensure all API Triggered Campaigns allow users to become re-eligible within **15 minutes**.

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
While the Decisioning Studio agent will never send the same campaign more than once a day, you will want to have the ability to send the same campaigns multiple times in a day for testing purposes.
{% endalert %}

### Step 4: Add dynamic placeholders

These will serve as dynamic placeholders for decisions that the Decisioning Studio agent is optimizing.

Here are some examples:

#### Example #1: Email Campaign

Suppose the Decisioning Studio agent is optimizing an email campaign. This might be configured like this: 

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supposing the agent is optimizing for choice of templates and Call to Action (CTA) message, then an API-triggered campaign should be created for each template, and the CTA section of one template might look like:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_2.png %})

#### Example #2: Push campaign

Suppose a Decisioning Studio agent is optimizing the message of a Push campaign. This might be configured like this:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resulting in the following message: 

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Example #3: SMS Campaign

Suppose that the Decisioning Studio agent is optimizing for fields in an SMS campaign. This might be configured like this:

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resulting in the following message: 

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

## If Customer Engagement Platform is SFMC or Klaviyo

Decisioning Studio also supports native integrations with SFMC and Klaviyo.

For SFMC, for example, Decisioning Studio triggers API events into a journey with data required to populate dynamic elements.

For detailed steps to configure an agent that uses either of these customer engagement platforms, contact the services team.

## If another Customer Engagement Platform

Decisioning Studio can integrate with any customer engagement platform. However, this may require some custom engineering work from your team, since Decisioning Studio cannot trigger communications directly.

In this scenario, the agent will deliver a "recommendation file." This file contains rows for each customer, with columns that indicate all of the personalized decisions for that customer.

For example, the following recommendation file might be used by a customer to optimize an email campaign:

| Customer ID | Template | Subject Line | Send Time |
|-------------|----------|--------------|-----------|
| user_123    | Template A | Welcome! | 10:00 AM |
| user_456    | Template B | Get Started | 2:00 PM |

For more information on custom integrations, contact the AI Decisioning Services team.

