---
nav_title: Lemnisk
article_title: Lemnisk
description: "This reference article details the partnership between Braze and Lemnisk, a AI-enabled customer data platform-led Marketing Automation platform, allowing you to stream user data collected at Lemnisk from various sources, into Braze to activate them across various channel and destinations using Braze's tools."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/), is an AI-powered Customer Data Platform (CDP) and Marketing Automation solution that enables real-time capture, unification, and activation of customer data from diverse, siloed sources. It seamlessly delivers this unified data across various martech and business platforms, while offering robust, real-time analytics to track every stage of the customer data lifecycle. 

_This integration is maintained by Lemnisk._

## About the integration

Lemnisk and Braze integration will allow brands and enterprises unlock the full potential of Braze by acting as a CDP-led intelligence layer that unifies user data across platforms in real time, and sending the user's information and behaviours collected to Braze in real-time. Lemnisk delivers enriched customer profiles—blending behavioral signals and personal attributes—directly into Braze, enabling brands to personalize messaging from Braze with deeper context.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Lemnisk and Braze Accounts | An existing user of [Lemnisk](https://www.lemnisk.co/) and [Braze](https://www.braze.com/) can take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permission. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your account](https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints). |
| External API in Lemnisk | You will have to get **External API** enabled for your Lemnisk account, with help from your CSM. |

## Integration

### Step 1: Creating a Braze External API

1. In Lemnisk, navigate to the External API channel. Click on 'Add New External API'. We'll now set up the [Track Users](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) endpoint as an External API. <br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20Open%20External%20API.png" alt="img1" width="80%">
2. Give Basic Details to the configuration as shown in the image below.<br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20Ext.%20API%20Basic%20Details.png" alt="img1" width="80%"><br><br>Enter the API details of the Track User endpoint as shown below. Define as many fields as you like at Engagement-level using {{}} so that you can provide different values to them for different campaigns<br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20Ext.%20API%20-%20Ext.%20API%20Details.png" alt="img1" width="80%">

3. Click on Save to set up your Track Users configuration.


### Step 2: Test and verify the Configuration

1. Once the configuration is saved successfully, you'll be taken to the 'Test API' Section.
2. Give test values of the API parameters in the JSON tree view, and click on 'Test Configuration'.
3. You'll see a success response from Braze if the credentials and API definitions are correct.<br><br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20Test%20Ext%20API.png" alt="img1" width="80%"><br><br>
4. To verify if the events are getting registered with Braze correctly, let's verify this test user on Braze Audience. Go to your Braze Dashboard > Audience (on the left navigation bar) > Search Users. Search for the email (or any other Identifier that you saved in the External API configuration). You should see the profile of the user that you sent to Braze from the Test API trigger.<br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20Braze%20COV.png" alt="img1" width="80%">

### Step 3: Creating Engagements to trigger User Events to Braze

Having verified the configuration to with Braze, we're almost done. All we have to do is start sending users to braze based on your use case. 
1. Create a Segment on Lemnisk. Say for example, as soon as users submit a lead form, send that information to Braze.
2. On that Segment, navigate to External API > 'Add Engagement'.
3. In the Engagement Creation screen, provide the basic details, and select our recently set up configuration (Braze Track Users) as the API.
4. In the 'Configure Parameters' section, you'll find the inputs for the Braze' parameters you chose to expose at engagement level - in this example below, we have _Name of the User_, _Product ID_ and _Event Time_. <br><br><img src="https://raw.githubusercontent.com/karansingh-lemnisk/braze_lemnisk-docs/develop/assets/img/lemnisk/lemnisk-braze%20create%20an%20Engagement.png" alt="img1" width="80%">
5. Provide appropriate personalisation variables to those inputs (variables to populate the lead form values) and click on 'Save'.
6. Activate the Engagement.

<div style="border: 1px solid #4CAF50; background-color: #e8f5e9; padding: 10px; border-radius: 6px; color: #2e7d32;">
  🎉 <strong>Congratulations!</strong><br>
  You've successfully set up events streaming to Braze via Lemnisk.
</div>
