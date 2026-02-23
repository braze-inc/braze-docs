---
nav_title: Launch your agent
article_title: Launch your agent
page_order: 4
description: "Learn how to launch your BrazeAI Decisioning Studio Go agent and set up Business as Usual (BAU) reporting for performance comparison."
---

# Launch your agent

> Once you've connected your data sources, set up orchestration, and designed your agent, you're ready to launch. This article covers activating your agent and setting up optional BAU reporting.

## Launching your agent

After completing all configuration steps in the Decisioning Studio Go portal:

1. Review your agent configuration to ensure all settings are correct.
2. Verify that your CEP integration is active and the orchestration is ready.
3. Select **Launch** (or equivalent action) in the Decisioning Studio Go portal to activate your agent.

Once launched, your agent will:
- Begin receiving audience data from your CEP
- Start making personalized recommendations for each customer
- Orchestrate sends through your configured CEP
- Collect engagement data to learn and improve over time

## Setting up BAU reporting

By default, the Decisioning Studio Go portal reporting compares the Decisioning Studio Go group against the Random Control group. If you have an existing Business as Usual (BAU) campaign that you'd like to compare against, you can set up BAU reporting to view all three groups in one place.

### Benefits of BAU reporting

The primary benefit of setting up BAU reporting is the application of Decisioning Studio Go's invalid click filtering. When applied to all three experiment groups, this allows for the most accurate and fair ("apples to apples") click performance comparison by removing noise from:
- Suspected machine clicks
- Clicks to the unsubscribe link

### Requirements for BAU reporting

Before setting up BAU reporting, ensure an apples-to-apples comparison between the BAU treatment group, the Decisioning Studio Go group, and the Random Control group:

- **No overlap**: No recipient can belong to more than one group for the entire duration of the experiment
- **Random assignment**: Recipients are randomly assigned to groups with no bias
- **Equal options**: Any options available to the BAU group (creative, frequency, time, incentive, or offer) are available to the Decisioning Studio Go and Random Control groups

{% alert warning %}
Without an "apples to apples" experiment design, BAU reporting can be confusing or misleading.
{% endalert %}

### Required information

After validating your experiment design, gather the following details to set up BAU reporting:

**Campaign IDs from your CEP:**

| CEP | Accepted Types |
|-----|---------------|
| **Braze** | Campaigns and Canvases |
| **Salesforce Marketing Cloud** | Journeys only |
| **Klaviyo** | Flows only |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**Audience ID from your CEP:**

| CEP | Accepted Types |
|-----|---------------|
| **Braze** | Segments only |
| **Salesforce Marketing Cloud** | Data Extensions only |
| **Klaviyo** | Segments only |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

If you don't have an existing audience that tracks your BAU audience, you must create one.

### Considerations

- **Click KPIs only**: Similar to Decisioning Studio Go more generally, BAU reporting only covers click KPIs, not conversion KPIs.
- **Canvas limitations**: We do not currently support filtering to specific Canvas step IDs. Events from all Canvas steps will be included in BAU data. This may invalidate comparisons against BAU if only certain Canvas steps should be included.

### Setting up BAU reporting

Follow the instructions in your Decisioning Studio Go portal. You must have:
- One or more campaign IDs where all communications are BAU communications
- One audience ID that tracks recipients in the BAU audience each day

## Monitoring your agent

After launching, monitor your agent's performance in the Decisioning Studio Go portal:

- **Engagement metrics**: Track click rates across experiment groups
- **Learning progress**: Observe how the agent's recommendations evolve over time
- **Group comparisons**: Compare Decisioning Studio Go performance against Random Control and BAU (if configured)

{% alert tip %}
Allow at least 2-4 weeks of data collection before drawing conclusions about performance. The agent needs sufficient interactions to learn and optimize effectively.
{% endalert %}

## Troubleshooting

If your agent isn't performing as expected:

1. **Verify orchestration**: Confirm that your CEP integration is active, campaigns and journeys are running, and that no global caps or similar rules are interfering with orchestration.
2. **Check data flow**: Confirm that audience data and engagement data are being captured correctly.
3. **Review experiment groups**: Ensure proper random assignment and no overlap between groups.
4. **Contact support**: Reach out to Braze Support for further assistance.
