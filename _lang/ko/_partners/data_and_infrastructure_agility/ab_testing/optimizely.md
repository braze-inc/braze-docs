---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "This reference article outlines the partnership between Braze and Optimizely that allows you to sync your Braze customer segments, events, and Currents events to Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) is a leading digital experience platform that offers experimentation and content management tools for digital products and marketing campaigns.

The Braze and Optimizely integration is a two-way integration that allows you to:

- Sync your Braze customer segments and events to Optimizely Data Platform (ODP) nightly to enrich Optimizely customer profiles, reports, and segmentation.
- Send Braze Currents events from Braze to Optimizely’s reporting tool.
- Sync ODP customer data and events to Braze to enrich your Braze customer data and trigger Braze messaging based on customer events in ODP.

## Prerequisites

| 요구 사항                     | 설명 |
|----------------------------------|-------------|
| Optimizely Data Platform account | An Optimizely Data Platform (ODP) account is required to take advantage of this partnership. |
| Braze REST API 키               | A Braze REST API key with the following permissions: `users.track`,`users.export.segments`,`segments.list`,`campaigns.trigger.send`, and `canvas.trigger.send`. |
| 커런츠                         | To export data back into Optimizely, you need to have Braze Currents set up for your account. |
| Optimizely URL and Token         | This can be obtained by navigating to your Optimizely dashboard and copying the ingestion URL and token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 통합 구성

1. In the **App Directory** of Optimizely Data Platform (ODP), select the **Braze** app and then select **Install App**.
2. Go to the **Settings** tab. In the **Authorization** section, do the following:
    1. Enter Braze **REST API Key**.
    2. Select your Braze **Instance URL**.
    2. Select **Verify API Key**.
3. In Braze, go to **[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**.
4. Select **Create New Current** > **Custom Currents Export**.
5. Configure the Current using the endpoint and token provided in ODP. This is required to sync Braze events to ODP. 

![Optimizely authorization.][1]

{:start="6"}
6\. In ODP, expand the **Segments** section and select specific segments from the **Segments to Sync** list, or select **Import All Customers** to sync all segments.
7\. Add any [additional field mappings](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) you want between Braze and ODP.
8\. Select **Save**.

![Optimizely Braze segment sync.][2]

{% alert tip %}
You must select segments to import Braze customer profiles. If you don't select any segments, the integration won't import any customer profiles.
{% endalert %}

### 2단계: Map data fields

The integration has default data field mappings between Braze and ODP. For example, the **Email** field in Braze is mapped to the **Last Seen Email** field in ODP.

![Optimizely and Braze segment map fields.][3]

#### Map additional fields (optional)

If there are additional data fields in Braze that you want to map to ODP, do the following in ODP:

1. In the **Segments** section of the app, select the Braze field from the **Braze User Data Fields** drop-down list.
2. Select the ODP field from the **ODP Customer Fields** drop-down list.
3. Select **Save Field Map**.

![Optimizely Braze Segment Save Field Maps][4]

#### Delete non-required field mappings (optional)

You can also delete any data field mappings that aren't required. Do the following in ODP:

1. In the **Segments** section of the app, select the field mapping you want to delete from the **Field Map** drop-down list.
2. Select **Delete Field Map**.

![Optimizely Braze Segment Delete Field Maps][5]

### 3단계: Sync data from Optimizely Data Platform (ODP) to Braze

After you configure the integration, you can set up an activation in ODP to sync your ODP customer data to Braze.

1. Go to **Activation** > **Engage** and select **Create New Campaign**.
2. Select **Behavioral** to set up an automated, recurring sync.
3. Select **Create From Scratch**, then enter a name for your activation that represents the data you are syncing to Braze (such as **Braze Data Sync**).
4. In the **Enrollment** section, you can sync data for customers that match a segment or sync data for customers that trigger an event (like when ODP registers that a customer opens an email):
   - **Customers that match a segment:** Select your desired segment, then select **Next**.<br><br>![Optimizely Select Segment][6]
   - **Customers that trigger an event:** Expand the **Filter** drop-down list and select the ODP event to use as the trigger for this data sync to Braze. Then, expand **Automation Rules** and adjust as desired. <br><br>![Optimizely Trigger Event][7]
5. Expand **Touchpoints**, select to edit **Touchpoint 1**, then select **Braze**.
6. Expand the **Targeting** section, then select the **Target Identifier**.
7. Select one of the following options for **Add Users To** in the **Configure** section:
    - **캠페인:** Add customers to a specific campaign in Braze. After choosing this option, you must select the Braze campaign.
    - **캔버스:** Add customers to a specific canvas in Braze. After choosing this option, you must select the Braze canvas.
    - **Profile Update Only:** Update only the Braze customer profile.
8. (Optional) Select the **Number of Additional Fields** you want to sync to Braze (up to 20).  
    Then, select the following for each additional field's drop-down list and input field that:
    - In each **Field #** drop-down list, select the Braze field you want to populate. 
    - In each corresponding **Field # Value**, enter the ODP field you want to send to the selected Braze field. For example, if you selected **Company Name** from the **Field #** drop-down list, enter `{{customer.company_name}}` for the corresponding **Field # Value**.
9. Select **Save**, then select your activation name in the breadcrumb trail.
10. Select **Select start time and schedule** in the **Touchpoints** section if you selected **Customers that match a segment** for the enrollment.
11. Complete the following settings:
    - **Recurring or Continuous:** Select **Recurring**.
    - **Start Date:** Enter the date you want to send the data to Braze.
    - **End:** Defaults to **Never**. If you want to end the Braze data sync on a specific date, set that here.
    - **Repeats:** Set to **Daily**.
    - **Repeat Every** – Set to **1 day**.
    - **Timing:** Enter the time you want to send the data to Braze.
    - **Time Zone:** Select the time zone in which you want to send this data.
12. Select **Apply**, **Save**, then **Go Live**. Your sync starts at your designated start date and time (or when the trigger event occurs).

## 문제 해결

### Inspect events

To verify that data is properly syncing from ODP to Braze, you can inspect events in ODP.

1. In ODP, go to **Account Settings** > **Event Inspector**.
2. Select **Start Inspector**.
3. When data is available in the inspector, a number displays next to **Refresh**. Select to view the data.
4. The raw data that ODP and Braze sends back and forth displays. Select **View Details** to see the formatted version of that raw data.
5. Data fields sent from Braze back to ODP start with `_braze`.

### Check activity logs

Each data sync is also logged in the [ODP activity log](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Go to **Account Settings** > **Activity Log**.
2. Filter the categories by **braze**.
3. Select **View Details** for a formatted view of the log details, including the number of matches.

[1]: {% image_buster /assets/img/optimizely/image1_authorization.png %}
[2]: {% image_buster /assets/img/optimizely/image2_syncsegment.png %}
[3]: {% image_buster /assets/img/optimizely/image3_emailmapfield.png %}
[4]: {% image_buster /assets/img/optimizely/image4_mapfields.png %}
[5]: {% image_buster /assets/img/optimizely/image5_deletephonefield.png %}
[6]: {% image_buster /assets/img/optimizely/image6_segment.png %}
[7]: {% image_buster /assets/img/optimizely/image7_trigger.png %} 