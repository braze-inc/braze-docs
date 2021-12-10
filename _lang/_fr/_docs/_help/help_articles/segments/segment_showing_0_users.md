---
nav_title: Missing Users in Segment
article_title: Missing Users in Segment
page_order: 1
page_type: solution
description: "This help article walks you through troubleshooting steps if zero users are showing in your segment, but you anticipate more."
tool: Segments
---

# Missing users in segment

There are two possible solutions when you are seeing `0` users, but you anticipated more:
* [Calculate Exact Statistics](#calculate-exact-statistics)
* [Verify Data Transfer](#verify-data-transfer)

## Calculate exact statistics

The Segment statistics could be providing an estimate. The estimation is calculated based on a random sample with a 95% confidence interval that the result is within `+/- 1%`. The smaller your user base is, the more likely it is that the size of your segment is a rough estimate. Click **Calculate Exact Statistics** on the **Segment Details** panel. This will calculate the exact number of users in your segment.

!\[Calculate Exact Statistics\]\[28\]


## Verify data transfer

It is possible that the data you are filtering on is not being sent to Braze. To check which custom events are being sent to Braze, click **Custom Events** on the left hand menu in the **Data** section. Select the custom event along with the specific dates and app to see what data is actually being transferred to Braze. If you notice that `0` data is being sent to Braze, the next step is to evaluate how you are sending the events to Braze.

!\[Data Transfer Verification\]\[29\]

{% alert important %}
The data that you see in the Braze dashboard may not have the same syntax as what you are sending to Braze. Ensure that these two match exactly.
{% endalert %}

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on January 5, 2021_
[28]: {% image_buster /assets/img_archive/trouble8.png %} [29]: {% image_buster /assets/img_archive/trouble9.png %}
