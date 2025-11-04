---
nav_title: Eppo
article_title: Eppo
description: "Learn how to integrate Eppo with Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) is a next-generation experimentation platform that enables teams to run A/B tests, manage features at scale, and leverage AI-driven insights for data-driven decision-making.

*This integration is maintained by Eppo.*

The Braze and Eppo integration allows you to set up A/B tests in Braze and analyze results in Eppo to uncover insights and tie message performance to long-term business metrics like revenue or retention.

## Prerequisites

| Requirement                        | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Eppo account                       | An Eppo account is required to take advantage of this partnership.                   |
| Currents or Snowflake Data Sharing | Currents or Snowflake Data Sharing is required for Eppo to analyze experiment data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Configure Currents or Snowflake Data Sharing in Braze

Eppo analyzes experiments directly in your data warehouse. To enable the integration, Braze message engagement data must be available in the warehouse connected to Eppo. You can export campaign data from Braze using Currents, or access Braze data in your Snowflake instance using [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Step 2: Set up your experiment in a Braze campaign or Canvas

You can use native A/B testing features in your campaigns and Canvases. To learn more, see [Multivariate and A/B testing](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Step 3: Set up Eppo to measure Braze experiments

To run experiments using Braze data in Eppo, create [assignments tables](https://docs.geteppo.com/data-management/definitions/assignment-sql/) in your warehouse based on user-level message event data exported from Braze. Separate tables are recommended for Canvas and campaign experiments because they rely on different metadata.

{% tabs local %}
{% tab canvas experiments %}
For Canvas experiments, assignments can be created either:

- At the Canvas entry level (`users.canvas.Entry`)
- Or in a Canvas Experiment step (`users.canvas.experimentstep.SplitEntry`)

In these cases, fields like `canvas_name`, `experiment_step_id`, `canvas_variation_name`, and `experiment_split_id` are used to define the experiment name and variation.

{% endtab %}

{% tab campaign experiments %}
For campaign experiments, use send events (such as push, email, SMS) to determine when a user entered the experiment. `campaign_name`, `message_variation_name`, and `time` are used to populate the assignment table.

{% endtab %}
{% endtabs %}

To track message-specific metrics (like clicks or opens), include a **Secondary Entity** by creating a `combined_id` that joins the user ID with the campaign or Canvas name. This `combined_id` is also used in your fact tables to align metrics with the correct experiment and variation.

Eppo uses these assignments and fact tables to analyze results, and it's recommended to set up a **Protocol** in Eppo to standardize future experiment setup. For more information, refer to [Eppo’s documentation](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Support

For questions about setting up Braze Currents, Snowflake Data Sharing, or configuring multivariate campaigns, reach out to your Braze customer success manager.

For assistance with configuring Eppo to measure Braze experiments, contact the Eppo support team.
