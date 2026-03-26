---
nav_title: Launch your agent
article_title: Launch your agent
page_order: 5
page_type: reference
description: "Learn how to launch your Decisioning Studio agent and close the AI decisioning loop for self-learning optimization."
---

# Launch your agent

> After you've connected data sources, set up orchestration, and designed your agent, you're ready to launch. This article covers activating your agent and closing the AI decisioning loop so the agent can continuously learn and improve.

## Launch steps

After completing all configuration steps with your AI Decisioning Services team:

1. Review your agent configuration to ensure all settings are correct.
2. Verify that your data connections and orchestration integrations are active.
3. Work with your AI Decisioning Services team to activate the agent.

Once launched, your agent will:
- Begin receiving audience and customer data
- Start making personalized recommendations for each customer
- Orchestrate actions through your configured CEP
- Collect feedback data to learn and improve over time

## Close the AI decisioning loop

Once launched, your agent needs feedback data to learn and improve. This includes conversions data, engagement data, and activations data that tell the agent what happened after customer engagement decisions were sent.

For detailed requirements on preparing these critical feedback data assets, see [Preparing your data sources]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/).

{% alert note %}
If the agent is natively integrated with the customer engagement platform (such as Braze or Salesforce Marketing Cloud), there may not be additional configuration steps necessary for feedback data, since these may be sent automatically with the customer data.
{% endalert %}

## Monitor your agent

After launching, work with your AI Decisioning Services team to monitor performance:

- **Performance metrics:** Track your success metric across experiment groups
- **Learning progress:** Observe how the agent's recommendations evolve over time
- **Insights:** Understand which dimensions and options are driving results for different customer segments

## Ongoing optimization

Your AI Decisioning Services team will continue to work with you to:

- Analyze agent performance and identify optimization opportunities
- Expand dimensions or options as needed
- Adjust constraints based on business rule changes
- Scale successful agents to additional use cases

{% alert tip %}
The agent continuously learns and improves over time. Allow sufficient time for the agent to gather data and optimize before making significant changes to the configuration.
{% endalert %}

