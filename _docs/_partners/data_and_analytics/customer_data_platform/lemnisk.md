---
nav_title: Lemnisk
article_title: Integrating Lemnisk with Braze
description: "This reference article details the partnership between Braze and Lemnisk, an AI-enabled customer data platform-led Marketing Automation platform, allowing you to stream user data collected at Lemnisk from various sources, into Braze to activate them across various channels and destinations using Braze's tools."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/), is an AI-powered Customer Data Platform (CDP) and marketing automation solution that enables real-time capture, unification, and activation of customer data from diverse, siloed sources. It seamlessly delivers this unified data across various MarTech and business platforms, while offering robust, real-time analytics to track every stage of the customer data lifecycle. 

_This integration is maintained by Lemnisk._

## About the integration

The Lemnisk and Braze integration allows brands and enterprises to unlock the full potential of Braze by acting as a CDP-led intelligence layer that unifies user data across platforms in real time, and sending the user's information and behaviors collected to Braze in real-time. Lemnisk delivers enriched customer profiles directly into Braze by blending behavioral signals and personal attributes that let you personalize your messaging with deeper context.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Lemnisk accounts | A [Lemnisk](https://www.lemnisk.co/) account is required to take advantage of this partnership. |
| External API in Lemnisk | Contact your Lemnisk CSM to get **External API** enabled for your account. |
| Braze REST API key | A Braze REST API key with `users.track` permission. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your account]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integrating Lemnisk

### Step 1: Create a Braze External API {#create-a-braze-external-api}

In Lemnisk, go to the External API channel. Select **Add New External API**. We'll now set up the [Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint as an External API.

![Starting the External API creation process in Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Under **Basic Details**, enter a name, description, channel, and channel identifier.

![Entering basic configuration details for a new External API in Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Under **External API details**, enter the relevant details for your `users.track` endpoint. You can define multiple engagement-level fields using {% raw %}`{{}}`{% endraw %}, which lets you set different values for different campaigns.

![Filling out the External API endpoint and payload details]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

To finish setting up your Track Users configuration, select **Save**. You'll automatically be redirected to the **Test API** page.

### Step 2: Test the configuration

On the **Test API** page, enter some test values for the API parameters in your JSON tree view, then select **Test Configuration**.

If your credentials and API definitions are correct, Braze will return a success response.

![Testing an External API configuration with a sample payload and success response]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Next, you'll verify that your events are being sent to Braze successfully. In the Braze dashboard, go to **Audience** > **Search Users**, then enter one of the identifiers from your External API configuration (such as a user email address). If everything is working correctly, the profile that received your test API trigger will be listed.

![Viewing a user's profile and activity overview in Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Step 3: Trigger user events in Braze

1. On Lemnisk, create a new segment. For example, you could create a segment that sends information to Braze as soon as users submit a lead form.
2. In your new segment, go to **External API** > **Add Engagement**.
3. Under **Engagement Creation**, enter the basic details and select the configuration [you created previously](#create-a-braze-external-api).
4. Under **Configure Parameters**, you'll find the inputs for the Braze parameters you chose to expose at engagement level. In the following example, it shows _Name of the User_, _Product ID_, and _Event Time_.
    ![Creating an engagement to send user data to Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Enter the relevant personalization variables for our chosen parameters, then select **Save**.
6. When you're finished, activate the Engagement.
