---
nav_title: FAQ
article_title: Decisioning Studio FAQ
page_order: 10
page_type: FAQ
description: "This page provides answers to frequently asked questions about Decisioning Studio."
---

# Frequently asked questions

> This article provides answers to some frequently asked questions about Decisioning Studio.

### What is a decisioning agent?

A decisioning agent is a custom configuration for BrazeAI Decisioning Studio™ that's tailor-made to meet a specific business goal. This is defined by the success metric, dimensions, and options you choose. The decisioning agent automatically discovers the optimal action for every customer to maximize your chosen business metric.

### What metrics can I optimize for?

You can optimize for any business metric that aligns with your goals, such as revenue, conversions, ARPU (Average Revenue Per User), CLV (Customer Lifetime Value), profit, contract renewals, or any other business KPI.

### What are dimensions in Decisioning Studio?

Dimensions can be thought of as the *types of levers* which the decisioning agent can pull to maximize the success metric. Typical dimensions include offer, subject line, creative, channel, or send time.

### What is an action bank?

The action bank defines the *specific options* which the decisioning agent has access to for each dimension "lever". For instance, for a channel dimension, you would define the specific channels the decisioning agent has access to. For an offer dimension, you would define the specific offers the decisioning agent can test.

### Can the decisioning agent take actions I haven't configured?

No. The decisioning agent can only take actions that *you* configure and add to the action bank. This means that all possible actions are defined by the combinations of what you put in the action bank.

### What are constraints?

Constraints limit the decisioning agent's actions to respect critical business rules. For example, this could be preventing a specific offer from being selected for customers in an ineligible geography, or setting a maximum budget for the decisioning agent to spend.

### What is the difference between Decisioning Studio Go and Decisioning Studio Pro?

Decisioning Studio Pro includes AI Decisioning Services support from Braze's forward deployed data science team, which will help you design and configure your agent to maximize your business outcomes. For more information, see [Decisioning Studio Go vs. Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/#decisioning-studio-go-vs-decisioning-studio-pro).

