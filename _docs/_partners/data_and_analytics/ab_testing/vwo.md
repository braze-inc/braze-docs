---
nav_title: Vwo
article_title: Integrating VWO with Braze
description: "Learn how to integrate VWO with Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) is a powerful experimentation platform that helps brands enhance key business metrics by enabling teams to run conversion optimization programs backed by customer behavior data. With VWO, you can unify customer data, gain behavioral insights, build hypotheses, run A/B tests across multiple platforms (server, web, and mobile), roll out features, personalize experiences, and optimize the entire customer journey.

By integrating VWO with Braze, you can leverage VWO experiment data to create targeted segments and deliver personalized campaigns.

## Prerequisites

| Requirement     | Description |
|-----------------|-------------|
| VWO account     | A VWO account with access to experimentation data. |
| Braze account   | An active Braze account with the [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrated on your webpage. You'll also need event property segmentation enabled. To request it, see [Considerations](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integrating VWO with Braze

### Step 1: Enable the Braze integration in VWO

1. Log in to your VWO account.
2. In the VWO dashboard, go to **Configurations > Integrations**. Here, you can enable integrations at the workspace level, which applies the integration to all future test campaigns by default.

   ![VWO Integration Configuration]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Select the Braze integration to enable it.
5. Optionally, you can enable the Braze integration for any existing campaigns. To do so, select a campaign, then go to **Configuration > Integrations**, and enable Braze.

   ![Enable Braze Integration]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. After you've enabled the integration, VWO will start sending experiment data to Braze at the campaign level.

### Step 2: Create a segment in Braze with VWO event properties

1. In the Braze dashboard, select **Segments** > **+ Create Segment**.
3. In the **Create Segment** window, enter a name for the segment, then **Create Segment**.
4. In your newly-created segment, select **Filters** > **Add Filter**, then choose **Custom Event** as the filter type.
6. In the filter dropdown, search for **VWO**.
7. Select the relevant VWO property and specify the required value.
8. If needed, configure the number of visits and time frame. When you're finished, select **Save**.

   ![Braze Segment Creation]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. To view the number of users that match your segment criteria, select **Calculate Exact Statistics**.

   ![Braze Segment Statistics]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Data flow

VWO sends the campaign experiment data to Braze as a custom event using the following format:

- **Event Name:** VWO
- **Event Properties:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
These custom event properties can also be used for segmentation and targeting.
{% endalert %}

## Considerations

### Request event property segmentation

Before you can use event property segmentation, you'll need it enabled in Braze. Use the following template to contact your Braze CSM or the support team for access.

   <table>
   <thead>
      <tr>
         <th>Field</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Subject</strong></td>
         <td>Request to Enable Event Property Segmentation for VWO Integration</td>
      </tr>
      <tr>
         <td><strong>Body</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our VWO&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> VWO<br>
         - <strong>Event Properties:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze data points

The custom event sent from VWO to Braze&#8212;including any event properties enabled for segmentation&#8212;will consume data points in your Braze instance.

### Limitations

Currently, this integration doesn't support real-time sync of test data. There may be a delay of up to 15 minutes for test data to appear in Braze.

## Troubleshooting

If you're not seeing VWO data in Braze:

1. Right-click on the page, where your test campaign is running and select **Inspect Element**.
2. Under the **Network** tab, search for **Braze** to filter the network calls for Braze.
3. The network calls get populated as the page loads. You may reload the page to view the network calls.
4. Select a network call to view further details.
5. Go to the **Request Payload** section in the **Payload** tab, where you can find events: that has name: **ce**, indicating Custom Event.
6. Expand 0: and data: to see n: “VWO” (name of the Custom Event) and p: {vwo_campaign_name: “<your vwo campaign name>”, vwo_variation_name: “<variation name>”}. These indicate that the values are being pushed by VWO to Braze.

 ![Braze Troubleshooting]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

For additional support, contact your VWO customer success manager.
