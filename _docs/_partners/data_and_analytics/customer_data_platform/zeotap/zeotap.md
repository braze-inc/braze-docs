---
nav_title: Zeotap
description: "This reference article outlines the partnership between Braze and Zeotap, a next-generation customer data platform that provides identity resolution, insights, and enrichment."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) is a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment.

With the Zeotap and Braze integration, you can extend the scale and reach of your campaigns by syncing Zeotap customer segments to map user data to Braze user accounts. You can then act on this data, delivering personalized target experiences to your users.

## Prerequisites

| Requirement | Description |
| --- | --- |
|Zeotap account | A [Zeotap account](https://zeotap.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Create a Zeotap destination

1. From the Zeotap Unity platform, navigate to the **DESTINATIONS** application.
2. Under **All Channels**, select **Braze**.
3. In the prompt that appears, name your destination, and provide your client name and Braze REST API key associated with your Braze account.
4. Lastly, select your Braze REST endpoint instance from the dropdown and save the destination. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Step 2: Create and link a Zeotap segment to your destination 
 
1. From the Zeotap Unity platform, navigate to the **CONNECT** application.
2. Create a segment and select the Braze destination created in step 1.
3. Select a supported output identifier: MAIDs, email address hashed to SHA256, or any 1P customer identifier recognized by Braze (if you want to use a custom identifier for your Braze account, get in touch with Zeotap so that it can be enabled for your account). Only one output identifier can be used for the Braze integration. These identifiers must be the same as the external ID set when collecting Braze SDK data.
4. Save the segment.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
The identifiers that appear are both available in the segment and supported by Braze.
{% endalert %}

### Step 3: Create Braze segment

After successfully creating, pushing, and processing a segment in Zeotap, the Zeotap users will appear in the Braze dashboard. You can look up users by user ID in the Braze dashboard. 

![A Braze user profile showing the segment one through four listed as "true" under "Custom attributes".]({% image_buster /assets/img/zeotap/zeotap4.png %})

If a user is part of the Zeotap segment, the segment name appears as a custom attribute on their user profile with the boolean value `true`. Take note of the custom attribute name as you will need it when creating a Braze segment. 

Next, you must create and define this segment within Braze:
1. From the Braze dashboard, select **Segments** and then **Create Segment**.
2. Next, name your segment and select the custom attribute segment made in Zeotap.
3. Save your changes. 

![In the Braze segment builder, you can find the imported segments set as custom attributes.]({% image_buster /assets/img/zeotap/zeotap3.png %})

You can now add this newly created segment to future Braze campaigns and Canvases to target these end-users. 

