---
nav_title: Designing decisioning agents
article_title: Designing decisioning agents
page_order: 3
page_type: reference
description: "This reference article covers key concepts and best practices for designing and configuring your decisioning agent."
---

# Designing decisioning agents

> This reference article covers key concepts and best practices for designing and configuring your decisioning agent.

## About decisioning agents

Designing your decisioning agent is the first step in setting up Decisioning Studio. For the decisioning agent to be able to make decisions, you need to define what outcome you want to maximize, and what actions the agent can take to do so.

### Key concepts

The following terms are referenced throughout the Decisioning Studio guide.

| Term | Definition |
| --- | --- |
| **Decisioning agent** | A decisioning agent is a custom configuration for BrazeAI Decisioning Studio™ that's tailor-made to meet a specific business goal. This is defined by the success metric, dimensions, and options you choose. |
| **Success metric** | The specific business metric you want to optimize for, such as revenue, conversions, or average revenue per user (ARPU). This is the metric which the decisioning agent will aim to maximize through its actions. |
| **Dimensions** | Dimensions can be thought of as the *types of levers* which the decisioning agent can pull to maximize the success metric. Typical dimensions include offer, subject line, creative, channel, or send time. |
| **Action Bank** | The action bank defines the *specific options* which the decisioning agent has access to for each dimension "lever". For instance, for a channel dimension, you would define the specific channels the decisioning agent has access to. For an offer dimension, you would define the specific offers the decisioning agent can test. 
| **Constraints** | In general, the decisioning agent could take any combination of actions that you put in the action bank. However, you can also define constraints to limit the decisioning agent's actions to respect critical business rules. For example, this could be preventing a specific offer from being selected for customers in an ineligible geography, or setting a maximum budget for the decisioning agent to spend. 
{: .reset-td-br-1 .reset-td-br-2}

![A high level overview of a decisioning agent]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
The decisioning agent can only take actions that *you* configure and add to the action bank. This means that all possible actions are defined by the combinations of what you put in the action bank. 
{% endalert %}

## How to design your decisioning agent

When setting up a decisioning agent, you'll need to think through four main design elements:

### The "goal": Define your success metric

> What outcome do you want the agent to maximize?

Your success metric is the business outcome the agent will optimize for. This should align directly with your business objectives—not proxy metrics like clicks or opens, but real business results like revenue, conversions, ARPU, or customer lifetime value.

### The "who": Select your audience

> Who will the decisioning agent engage?

Define the audience that your agent will serve. This could be all customers, a specific segment (like loyalty program members), or customers at a particular stage of their lifecycle (like recent purchasers or at-risk subscribers).

### The "what": Configure your action bank

> What options can the agent choose from to drive the outcome?

The action bank defines all the levers the agent can pull—the dimensions (like channel, offer, timing, and frequency) and the specific options within each dimension. The agent experiments with different combinations of these options to find what works best for each customer.

### The "how": Configure your constraints

> What rules should the agent follow?

Constraints are the rules that the agent must follow. This could be preventing a specific offer from being selected for customers in an ineligible geography, or setting a maximum budget for the decisioning agent to spend.

## Best practices and examples

To maximize the impact of your decisioning agent, you should:

- Choose a success metric that closely aligns with your business goals and objectives, such as revenue, conversions, or ARPU.
- Focus on the dimensions, or "levers" to test, such as offer, subject line, creative, channel, or send time, that are most likely to have a significant impact on the success metric.
- Select the options for each dimension, such as email versus SMS, or daily versus weekly frequency, that are most likely to have a significant impact on the success metric.

Some examples of decisioning agents you could build are:

{% tabs %}
{% tab Repeat purchase agent %}
You could build a repeat purchase agent to increase follow-up conversions after an initial sale:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different combinations of product offers, message timing, and frequency for each customer
- Over time, BrazeAI™ learns what works best for each customer
- Orchestrates personalized sends through Braze to maximize repurchase rates
{% endtab %}
{% tab Cross-sell or upsell agent %}
You could build a cross-sell or upsell agent to maximize average revenue per user (ARPU) from internet subscriptions:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different combinations of messages, sending times, discounts, and plan offers for each customer
- BrazeAI™ learns which customers are susceptible to leapfrog offers and which require discounts or other incentives to upgrade
- Orchestrates personalized sends through Braze to maximize ARPU
{% endtab %}
{% tab Renewal and retention agent %}
You could build a renewal and retention agent to secure contract renewals, maximizing both contract length and net present value (NPV):

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different renewal offers for each customer
- BrazeAI™ identifies customers who are less price sensitive and need less significant discounts to renew
- Orchestrates personalized sends through Braze to maximize contract renewals and NPV
{% endtab %}
{% tab Winback agent %}
You could build a winback agent to increase reactivation by encouraging past subscribers to resubscribe:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing thousands of variables at once, including creative, message, channel, and cadence
- BrazeAI™ discovers the best combination for each individual customer
- Orchestrates personalized sends through Braze to maximize reactivation rates
{% endtab %}
{% tab Referral agent %}
You could build a referral agent to maximize new accounts opened through business credit card referrals from existing customers:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different emails, creatives, sending times, and credit card offers for each customer
- BrazeAI™ determines the ideal combination for specific customers
- Orchestrates personalized sends through Braze to maximize referral conversions
{% endtab %}
{% tab Lead nurturing and conversion agent %}
You could build a lead nurturing and conversion agent to drive incremental revenue and pay the right amount for each customer:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different customer segments, bidding methodology, bid levels, and creative
- BrazeAI™ leverages robust first-party data to optimize paid ad performance as privacy policies change
- Orchestrates personalized sends through Braze to maximize revenue while optimizing cost per customer
{% endtab %}
{% tab Loyalty and engagement agent %}
You could build a loyalty and engagement agent to maximize purchases by new enrollees in a customer loyalty program:

- Define the audience and message in Braze
- Decisioning Studio automatically runs daily experiments, testing different email offers, sending times, and frequencies for each customer
- BrazeAI™ learns what works best for each new enrollee in the loyalty program
- Orchestrates personalized sends through Braze to maximize purchase and repurchase rates
{% endtab %}
{% endtabs %}

## Next steps

Ready to build your own decisioning agent? Follow the next steps for your Decisioning Studio tier:

- **Decisioning Studio Go**: [Set up Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Set up Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

These guides walk you through connecting data sources, setting up orchestration, designing your agent, and launching to production.
