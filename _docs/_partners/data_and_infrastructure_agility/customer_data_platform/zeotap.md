---
nav_title: Zeotap
description: "This article outlines the partnership between Braze and Zeotap, a next-generation customer data platform providing identity resolution, insights, and enrichment."
alias: /partners/zeotap/
page_type: partner
search_tag: Partner

---

# Zeotap

> [Zeotap](https://zeotap.com/) is a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment.

With the Zeotap and Braze integration, you can extend the scale and reach of your campaigns by syncing Zeotap customer segments to map Zeotap user data to Braze user accounts. You can then act on this data, delivering personalized target experiences to your users.

## Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | The Braze API Key will be used in the API calls to the Braze REST Endpoint URLs to authenticate the service. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
|---|---|---|---|
| Zeotap Account and Account Information | Zeotap | [Zeotap](https://zeotap.com/) | You must have an active Zeotap account to utilize their services with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Braze and Zeotap integration

### Step 1: Create a Zeotap destination for Braze

1. From the Zeotap Unity platform, navigate to the __DESTINATIONS__ application.
2. Under __All Channels__, search for Braze.
3. Select Braze and in the prompt that appears, enter the destination name, client name, and API key associated with your Braze account.
4. Select the Braze REST endpoint instance and save the destination. <br><br>![Zeotap Braze destination][1]

### Step 2: Create and link a Zeotap segment to your destination 
 
1. From the Zeotap Unity platform, navigate to the __CONNECT__ application.
2. Create a segment and push it to Braze.
3. Select the associated output identifier.<br><br>The supported output identifiers for this integration include MAID, sha56 email, and sha56 phone.<br><br>Only one of these identifiers can be used for the Braze integration. These identifiers must be the same as the external ID set when collecting data using the Braze SDK.
4. Click __Yes__ to activate the segment. 

![Zeotap segment][2]

{% alert note %}
The identifiers that appear in the window are the ones that are both available in the segment and supported by Braze.
{% endalert %}

### Step 3: Create Braze segment

After successfully creating, pushing, and processing a segment in Zeotap, the Zeotap users will appear in the Braze dashboard. You can look up users by user ID in the Braze dashboard. 

![Zeotap user profile][4]

If a user is part of the Zeotap Segment, the segment name appears as a custom attribute on their user profile with the boolean value `true`. Take note of the customer attribute name as you will need it when creating a Braze segment. 

Next, you must create and define this segment within Braze by performing the following steps:
1. From the Braze dashboard, select __Segments__ and then __Create Segment__.
2. Next, name your segment and select the custom attribute segment that was made in Zeotap.
3. Save your changes. 

![Braze segment][3]

You can add this newly created segment to future Braze campaigns and Canvases to target these end-users. 

[1]: {% image_buster /assets/img/zeotap/zeotap1.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap2.png %}
[3]: {% image_buster /assets/img/zeotap/zeotap3.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap4.png %}