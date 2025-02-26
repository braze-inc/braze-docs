---
nav_title: VWO
article_title: VWO
description: "Learn how to integrate VWO with Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
layout: dev_guide
---

# VWO

VWO is a powerful experimentation platform that helps brands enhance key business metrics by enabling teams to run conversion optimization programs backed by customer behavior data. With VWO, you can unify customer data, gain behavioral insights, build hypotheses, run A/B tests across multiple platforms (server, web, and mobile), roll out features, personalize experiences, and optimize the entire customer journey.

By integrating VWO with Braze, you can leverage VWO experiment data to create targeted segments and deliver personalized campaigns.

## Prerequisites

| Requirement      | Description |
|-----------------|-------------|
| VWO account     | A VWO account with access to experimentation data |
| Braze account   | An active Braze account with the Braze Web SDK integrated on your webpage |

## Integration

### Step 1: Enable the integration

1. Log in to your VWO account.
2. Navigate to **Configurations > Integrations** from the left panel of your VWO dashboard. This section allows you to enable integrations at the workspace level, applying them to all future test campaigns by default.

   ![VWO Integration Configuration](images/image2.png)

3. Click on the Braze integration and enable it.
4. If you wish to enable Braze integration for existing campaigns, select the specific campaign, go to **Configuration > Integrations**, and enable Braze.

   ![Enable Braze Integration](images/image1.png)

5. Once enabled, VWO will start sending experiment data to Braze at the campaign level.

### Step 2: Create a segment in Braze using VWO event properties

1. Log in to your Braze dashboard.
2. Click on **Segments** in the top panel and then select **+ Create Segment**.
3. In the **Create Segment** popup, enter a name for the segment and click **Create Segment**.
4. Under the newly created segment, navigate to the **Filters** section.
5. Click **Add Filter** and choose **Custom Event** as the filter type.
6. In the dropdown, search for **VWO**.
7. Select the relevant VWO property and specify the required value.
8. Configure the number of visits and time frame as needed, then click **Save**.

   ![Braze Segment Creation](images/image3.png)

9. Click **Calculate Exact Statistics** to view the number of users that match your segment criteria.

   ![Braze Segment Statistics](images/image4.png)

## Data flow

VWO sends the campaign experiment data to Braze as a custom event using the following format:

- **Event Name:** VWO
- **Event Properties:** `vwo_campaign_name`, `vwo_variation_name`

The custom event properties can be used for segmentation and targeting.

## Important Notes

1. If you'd like to use event property segmentation in Braze, it must be enabled by the Braze team. Please contact your Braze CSM or Support team to have it enabled. Below is a sample message you can use to request event property segmentation:

   **Subject:** Request to Enable Event Property Segmentation for VWO Integration

   **Message:**  
   "Hello Braze Team,  
   We would like to enable event property segmentation for events sent from our VWO<>Braze integration. Here are the details:

   - **Event Name:** VWO  
   - **Event Properties:** `vwo_campaign_name`, `vwo_variation_name`  

   Please confirm once the properties have been enabled in our account.

   Thank you."

2. The custom event being sent to Braze from VWO, along with any event properties enabled for segmentation, consumes data points in Braze.

## Limitations

The integration currently doesn't support real-time sync of test data. There may be a delay of up to 15 minutes for test data to appear in Braze.


## Troubleshooting

If you're not seeing VWO data in Braze:
1. Right-click on the page, where your test campaign is running and select **Inspect Element**.
2. Under the **Network** tab, search for **Braze** to filter the network calls for Braze.
3. The network calls get populated as the page loads. You may reload the page to view the network calls.
4. Select a network call to view further details.
5. Go to the **Request Payload** section in the **Payload** tab, where you can find events: that has name: **ce**, indicating Custom Event.
6. Expand 0: and data: to see n: “VWO” (name of the Custom Event) and p: {vwo_campaign_name: “<your vwo campaign name>”, vwo_variation_name: “<variation name>”}. These indicate that the values are being pushed by VWO to Braze.

For additional support, contact your VWO customer success manager.
