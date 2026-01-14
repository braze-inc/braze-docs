# Building AI decisioning agents

> Learn how to build an agent for BrazeAI Decisioning Studio™, so you can automate personalized experimentation and optimize outcomes like conversions, retention, or revenue&#8212;without manual A/B testing.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## About agents

An AI decisioning agent is a custom configuration for the BrazeAI™ decisioning engine that's tailor-made to meet a specific business goal.

For example, you could build a repeat purchase agent to increase follow-up conversions after an initial sale. You define the audience and message in Braze, while your decisioning agents runs daily experiments and automatically tests different combinations of product offers, message timing, and frequency for each customer. Over time, BrazeAI™ learns what works best and orchestrates personalized sends through Braze to maximize repurchase rates.

To build a good agent, you'll:

- Choose a success metric for BrazeAI™ to optimize for, such as revenue, conversions, or ARPU.
- Define which dimensions to test, such as offer, subject line, creative, channel, or send time.
- Select the options for each dimension, such as email versus SMS, or daily versus weekly frequency.

![Example diagram of a decisioning studio agent for referral emails.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Sample agents

Here are some examples of agents that you can build with BrazeAI Decisioning Studio™. Your AI decisioning agents will learn from every customer interaction and apply those insights to the next day's actions.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Building an agent

### Prerequisites

Before you can build an agent, you'll need to [integrate BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration).

### Step 1: Contact AI Expert Services

The AI Expert Services team will work closely with you to scope, design, and build your decisioning agent. If you haven't already, [contact us](https://www.braze.com/get-started/) to get started.

You'll complete the following steps together to build a custom agent that's right for you.

### Step 2: Design your agent

Alongside the AI Expert Services team, you'll define:

- a target audience, 
- the business metric to optimize, 
- the actions for BrazeAI™ decisioning agent, and 
- any first-party customer data the agent should leverage to drive your business outcomes. 

With the design in hand, the team will work with you to identify and complete any additional integration requirements.

### Step 3: Set up your delivery platform

Next, the AI Expert Service team will help you set up your marketing automation platform. While the decisioning studio works best with Braze, a variety of other platforms are supported&#8212;contact your AI Expert Service team for additional resources.

{% tabs local %}
{% tab Braze %}
To set up Braze:

1. Create a [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ will use this delivery method to send 1:1 personalized activation events to the users in your defined audience.
2. Be sure you don't include a Braze [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group), so BrazeAI™ can be the dedicated control group instead.
3. Depending on your dimensions, you can configure Liquid tags in your creative content to dynamically populate your messaging with BrazeAI™ recommendations. BrazeAI™ will pass customer-specific content to the Liquid tags in your templates using the Braze API.
{% endtab %}
{% endtabs %}

### Step 4: Launch and monitor

After launching your agent, your AI Expert Services team will continue to monitor and tune it to your agreed-upon design. They'll also help you make any adjustments, expansions, or modifications to the agent, if needed.
