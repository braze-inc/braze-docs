---
nav_title: Looker
alias: /partners/looker/
---

# About Looker

Looker, a business intelligence and big-data analytics platform, enables you to explore, analyze, and share real-time business analytics seamlessly.

Looker and Braze empower you to transform customer experiences with live customer-lifecycle data visualizations.

## Integration

Braze partners with Looker through first-party Looker Blocks. To use Looker with Braze, we recommend sending your Braze data to a [data warehouse using Braze Currents][6], then use Braze's Looker Blocks to quickly model and visualize your Braze data in Looker.

Braze's Looker Blocks can reduce the burden of modeling data and enable marketers to quickly access and visualize data.

[See how Braze uses Currents.][1]

# Available Looker Blocks

Our Looker Blocks help Braze customers quickly access a view of granular data we offer via [Currents][5]. Our blocks provide pre-made visualizations and modeling for Currents data so Braze customers can easily implement analytic patterns like retention, evaluate message deliverability, take a more detailed look at user behavior, and more.

Braze currently has two Blocks available: the Message Engagement Analytics and the User Behavior Analytics Blocks.

| Block | Description | More Information | Code |
|---|---|---|---|
| __Message Engagement Analytics Block__ | This block includes data around push, email, in-app messages, webhook, newsfeed, conversion, Canvas entry, and campaign control group enrollment events. | [Learn more about this Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze) from Looker. | See the code on [Github](https://github.com/llooker/braze_message_engagement_block). |
| __User Behavior Analytics Block__ | This block includes data around custom events, purchases, sessions, location events, and uninstalls. | [Learn more about this Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze) from Looker. | See the code on [Github](https://github.com/llooker/braze_retention_block). |

# Implementing the Looker Blocks

To implement the Looker Blocks, follow the instructions in the README files of the Github code.

- [Message Engagement Analytics Block README][2]
- [User Behavior Analytics Block README][3]

{% alert important %}
  Braze has built our Looker Blocks using [Snowflake](https://www.snowflake.com/) as our data warehouse. While we aim for our Blocks to work with as many data warehouses as possible, there may be some SQL functions that differ in availability, syntax, or behavior across dialects.
{% endalert %}

Both integrations assume that your [initial Braze integration][4], as well as your Braze integration with a Looker-compatible [data warehouse][7] is appropriately configured to capture and send necessary data.

{% alert warning %}
Be aware of different naming conventions! Custom names can cause incongruences in data unless you take care to change all corresponding names. If you've customized any View/table or model names, rename each in the LookML to the name you've selected.
{% endalert %}

[1]: {{ site.baseurl }}/partners/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{ site.baseurl }}//user_guide/onboarding_with_braze/integration/
[5]: {{ site.baseurl }}/partners/braze_currents/about/
[6]: {{ site.baseurl }}/partners/braze_currents/integration/available_partners/
[7]: https://looker.com/solutions/other-databases
