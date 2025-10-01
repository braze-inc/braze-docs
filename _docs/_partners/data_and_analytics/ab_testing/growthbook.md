---
nav_title: GrowthBook
article_title: GrowthBook
description: "Learn how to integrate GrowthBook with Braze."
alias: /partners/growthbook/
page_type: partner
search_tag: Partner
---

# GrowthBook

> [GrowthBook](https://www.growthbook.io/) is an open-source feature flagging and experimentation platform that helps teams deploy code safely, run A/B tests, and make data-driven decisions with your existing data stack.

*This integration is maintained by GrowthBook.*

The GrowthBook and Braze integration enables you to leverage GrowthBook's powerful statistical engine to analyze your Braze messaging experiments. Connect campaign performance to product metrics, revenue, and long-term user behavior—all within your existing data infrastructure.

## Prerequisites

| Requirement                        | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| GrowthBook account                 | Sign up for a free GrowthBook account at [growthbook.io](https://www.growthbook.io) (cloud or self-hosted). |
| Data export method                 | Either Braze Currents or Snowflake Data Sharing to export message engagement data to your warehouse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Export Braze data to your warehouse

GrowthBook performs analysis directly on data in your warehouse, so you'll need to export Braze engagement data using one of these methods:

- **Braze Currents**: Stream event data to your warehouse via cloud storage or direct integration
- **Snowflake Data Sharing**: For Snowflake users, access Braze data directly through [data sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

Once configured, Braze will continuously send message engagement events (sends, opens, clicks, conversions) to your warehouse.

### Step 2: Run messaging experiments in Braze

Configure your A/B tests using Braze's native experimentation capabilities in campaigns or Canvases. For guidance, see [Multivariate and A/B testing](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

Make note of your campaign names and variation identifiers, as you'll reference these when setting up analysis in GrowthBook.

### Step 3: Configure GrowthBook to analyze Braze experiments

To analyze your Braze experiments, you'll connect GrowthBook to your warehouse and set up the necessary queries and metrics.

#### Connect your data warehouse

If your Braze data is already available in GrowthBook, skip to the next step.

1. In GrowthBook, go to **Metrics and Data → Data Sources**
2. Add your warehouse as a new data source

#### Create an Experiment Assignment Query

In your data source settings, add an Experiment Assignment Query to identify which users received which variation:

{% tabs local %}
{% tab canvas experiments %}

For Canvas experiments:
```sql
SELECT
  external_user_id as user_id,
  canvas_name as experiment_id,
  canvas_variation_name as variation_id,
  time as timestamp
FROM braze_currents.users_canvas_entry
WHERE 
  time >= '{{ start_date }}'
  AND time <= '{{ end_date }}'
```

{% endtab %}
{% tab campaign experiments %}

For campaign experiments:
```sql
SELECT
  external_user_id as user_id,
  campaign_name as experiment_id,
  message_variation_name as variation_id,
  time as timestamp
FROM braze_currents.users_messages_email_send
WHERE 
  time >= '{{ start_date }}'
  AND time <= '{{ end_date }}'
```

{% endtab %}
{% endtabs %}

#### Create Metrics

Navigate to **Metrics and Data → Fact Tables** to define your event data. With fact tables in place, you can create metrics without writing additional SQL.

### Step 4: View experiment results

For past campaigns:
1. Select **Experiments → Add Experiment → Import Existing Experiment**
2. Choose the data source with Braze experiments. GrowthBook will automatically find all existing experiments.
3. Import experiments for analysis
4. View and analyze results using GrowthBook's statistical tools

For ongoing campaigns, create the experiment before launch to monitor results in real-time.

## Why GrowthBook for Braze experiments?

- **Warehouse-native**: Analysis runs directly on your data without duplication
- **Statistical rigor**: Bayesian and Frequentist engines, CUPED variance reduction, sequential testing
- **Unified platform**: Analyze both marketing and product experiments in one place
- **Open source**: Full transparency into calculations and methodologies
- **Cost optimization**: Enterprise customers benefit from query optimization that reduces warehouse costs

## Support

For Braze Currents setup or campaign configuration, contact your Braze customer success manager.

For GrowthBook configuration and analysis setup, visit our [documentation](https://docs.growthbook.io) or join our [Slack community](https://join.slack.com/t/growthbookusers/shared_invite/zt-2xw8fu279-Y~hwnfCEf7WrEI9qScHURQ).
