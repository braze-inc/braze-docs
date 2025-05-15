# Eppo

Eppo is a next-generation experimentation platform that enables teams to run A/B tests, manage features at scale, and leverage AI-driven insights for data-driven decision-making.

This integration is maintained by Eppo.

## About the integration

By integrating Eppo with Braze, you can set up A/B tests in Braze and analyze results in Eppo to uncover insights and tie message performance to long-term business metrics like revenue or retention.

## Prerequisites

| Requirement                        | Description                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| Eppo account                       | An Eppo account is required to take advantage of this partnership                   |
| Currents or Snowflake Data Sharing | Currents or Snowflake Data Sharing is required for Eppo to analyze experiment data. |

## Integration

### Step 1: Configure Braze Currents or Snowflake Datat Sharing in Braze

Eppo analyzes experiments directly in your data warehouse, so the only requirement for the integration is that the Braze message engagement data is available in the warehouse connected to Eppo. You can export campaign data from Braze using Currents, or access Braze data in your Snowflake instance via Braze Data Sharing.

### Step 2: Set up your experiment in a Braze Campaign or Canvas

You can use Braze’s native A/B testing features in your campaigns and canvases.. Read more about setting up multivariate and a/b testing in braze here:
[https://www.braze.com/docs/user\_guide/engagement\_tools/testing/multivariant\_testing/#what-are-multivariate-and-ab-testing](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing)

### Step 3: Set up Eppo to measure Braze experiments

To run experiments using Braze data in Eppo, you need to create Assignments tables in your warehouse based on user-level message event data exported from Braze. Separate tables are recommended for Canvas and Campaign experiments since they rely on different metadata.

* **For Canvas experiments**, assignments can be created either:

  * At the **Canvas entry** level (`users.canvas.Entry`)
  * Or within a **Canvas experiment step** (`users.canvas.experimentstep.SplitEntry`)
    In these cases, fields like `canvas_name`, `experiment_step_id`, `canvas_variation_name`, and `experiment_split_id` are used to define the experiment name and variation.

* **For Campaign experiments**, use **Send events** (e.g. push, email, SMS) to determine when a user entered the experiment. `campaign_name`, `message_variation_name`, and `time` are used to populate the Assignment table.

To track **message-specific metrics** (like clicks, opens), you should include a **Secondary Entity** by creating a `combined_id` that joins the user ID with the campaign or canvas name. This `combined_id` is also used in your Fact tables so that the metrics align with the correct experiment and variation.

Eppo then uses these Assignments and Fact tables to analyze results, and it’s recommended to set up a **Protocol** in Eppo to standardize future experiment setup. For more information, please refer to Eppo’s documentation.

[https://docs.geteppo.com/guides/marketing/integrating-with-braze/](https://docs.geteppo.com/guides/marketing/integrating-with-braze/)

## Support

For questions about setting up Braze Currents Snowflake Data Sharing or configuring multivariate campaigns, please reach out to your Braze Customer Success Manager.

For assistance with configuring Eppo to measure Braze experiments, contact the Eppo support team.
