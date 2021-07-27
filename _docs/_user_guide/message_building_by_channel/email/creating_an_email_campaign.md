---
nav_title: Creating an Email Campaign
platform: Message_Building_and_Personalization
subplatform: Email
page_order: 1
description: "This reference article covers how to create an email campaign using the Braze platform. Included are best practices on how to compose your messages, preview your content, and schedule your campaign."

tool:
  - Dashboard
  - Campaigns

channel:
  - email
---

# Creating an Email Campaign

> This article covers how to create an email campaign in Braze. Here, we'll cover steps and best practices on how to compose your message, preview your content, and schedule your campaign.

Email messages are great for delivering content to your users on their terms. They are also excellent tools to re-engage users who may have even uninstalled your app. Sending customized and tailored email messages will enhance your users' experience, and help your users get the most value out of your app.

To see examples of email campaigns, check out our [Case Studies][9].

## Step 1: Create a New Campaign
On the **Campaigns** page, click **Create Campaign** and select **Email** as your messaging channel.

![newcampaign][19]

Give your new campaign a name and optional description. You can also assign [tags][20] to keep track of engagement tactics.  

## Step 2: Compose Your Email or Use a Template {#step-2-choose-your-template-and-compose-your-email}

Braze offers basic email templates for a variety of use cases to get you started with creating email campaigns. Click on the appropriate tile to choose an existing email template, [create your own][10], or [upload one from a file][18], and then draft your message.

![email1][3]

Once you choose a template for your email, you'll see an overview of your email, where you can quickly jump to the fullscreen editor, change your sending info, and view warnings about deliverability or law compliance.

![newemailoverview][14]

### Step 2a: Add Email Headers

Email headers contain information about the email being sent. These key-value pairs typically have information about the sender, recipient, authentication protocols, and contain email routing information. Braze automatically adds the necessary header information required by the RFC for emails to be delivered to your inbox provider properly.

However, Braze does allow you the flexibility to add additional email headers as needed for advanced use cases. There are a few reserved fields that the Braze platform will overwrite during sending. Avoid using the following keys:

| Reserved Fields |  |  |
| --- | --- | --- |
| BCC | dkim-signature | Reply-To |
| CC | From | Subject |
| Content-Transfer-Encoding | MIME-Version | To |
| Content-Type | Received | x-sg-eid |
| DKIM-Signature | received | x-sg-id |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Step 2b: Preview and Test Your Message

After you finish composing your perfect email, you need to test it before sending it out.

From the bottom of the overview screen, click **Preview and Test**. Here you can preview how your email will appear in a customer's inbox. With **Preview as User** selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message will appear in different contexts.

When you're ready for a final check, select **Test Send** and send a test message to yourself or a group of content testers to ensure that your email displays properly on a variety of devices and email clients.

![newemailtest][15]

If you see any issues with your email, or want to make any changes, click **Edit Email** to return to the editor.

### Step 2c: Check for Email Errors

The editor will call out any problems it catches with your message before you send it. Here's a list of errors that are accounted for in our editor:

- **From Display Name** and **Header** not specified together.
- Invalid **From** and **Reply-To** addresses.
- Duplicate **Header** keys.
- Liquid syntax problems.
- [Email bodies larger than 400kb; bodies are highly recommended to be smaller than 102kb.][16]
- Emails with a blank **Body** or **Subject**.
- Emails with no unsubscribe link.
- The email you are sending from is not whitelisted, thus sends will be highly limited to ensure deliverability.


## Step 3: Schedule Your Messaging Campaign

You can schedule your campaigns against three types of delivery:
- Scheduled (sending your campaign at a designated time),
- Action-Based (sending when your users perform specified actions), and
- API-Triggered (sending according to an API request).



{% tabs %}
  {% tab Scheduled Delivery %}
Scheduled Delivery allows you to specify the time at which you want the message to send, either immediately or at a future time (you can also consider local time in your scheduling). You can also use [Intelligent Timing][21] to send the message when the user is most likely to engage. Braze makes this calculation based on a statistical analysis of the user's interactions with your app.

Messages can also be configured to recur daily, weekly (optionally on specific days), or monthly.

Unless you check **Allow users to become re-eligible to receive campaign**, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.


![Schedule]({% image_buster /assets/img_archive/schedule_new.png %}){: height="80%"" width="80%"}

  {% endtab %}
  {% tab Action-Based Delivery %}

  Action-Based Delivery allows you to specify the time a message will send after a user takes a particular action (selected from the __New Trigger Action__ dropdown.)

![Action]({% image_buster /assets/img_archive/action_delivery_new.png %}){: height="80%"" width="80%"}

  {% alert note %}
  When the trigger action is set to "Interact With Campaign", selecting a "Receive" option as the interaction will cause your new campaign to trigger as soon as Braze marks the selected campaign as sent, even if that message bounces or fails to be delivered.
  {% endalert %}

  {% endtab %}
  {% tab API-Triggered Delivery %}
Check out our [API-Triggered section of the Developer Guide]({{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery) for more on API-Triggered Delivery.

![API]({% image_buster /assets/img_archive/api_delivered_new.png %}){: height="80%"" width="80%"}
  {% endtab %}
{% endtabs %}


## Step 4: Choose Conversion Events

Braze allows you to track how often users perform specific actions after receiving a campaign, known as a [conversion event][22]. You can specify any of the following actions as a conversion event:

- Opens app
- Makes purchase (This can be a generic purchase or a specific item)
- Performs specific custom event
- Opens email
- Clicks email

You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action. While Braze automatically tracks opens and clicks for your campaign, you may wish to set the conversion event to be when a user opens or clicks on an email address to take advantage of Braze's [Intelligent Selection][13] feature.

## Step 5: Choose Your Target Segment

Next, you need to choose the target segment from the dropdown menu. You'll automatically be given a snapshot of what that segment population looks like right now, including how many users within that segment are reachable via email. Keep in mind that exact segment membership is always calculated just before the message is sent.

![Target Segment][5]

Optionally, you can also choose to limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

## Step 6: Review and Deploy

The final page will give you a summary of the campaign you've just designed. Confirm all the relevant details and click **Launch Campaign** to enable it for sending.

Now just wait for all the data to roll in!

![email2][6]

## Email Reporting

Braze provides you with a detailed report of each of your email campaigns. Navigate to the **Campaigns** tab on your dashboard and select your desired campaign to open the **Details** page. This page is broken up into three tabs:

- Campaign Analytics
- Retention Report
- Funnel Report

### Campaign Analytics

On the **Campaign Analytics** page, you can comprehensively view and analyze the success of your campaign in an organized format.

Additionally, you can see how successful different links in a single email campaign are using heat maps. Under **Email Performance**, expand the **Total Clicks** dropdown and click **View Heat Map** to bring up a visual view of your email that shows the overall frequency and location of clicks within the lifespan of the campaign. 

{% alert note %}
Date ranges are not taken into consideration for email heat maps.
{% endalert %}

![email_analytics][17]

When looking at clicks for your variant, the clicks will reflect unique clicks. When you expand each variation, the clicks for each link within the variation will reflect total clicks (not unique).

For detailed definitions of the metrics on this page, check out our [Email Analytics Glossary]({{site.baseurl}}/user_guide/message_building_by_channel/email/analytics_glossary/).

{% alert note %}
Braze will de-duplicate sends by email address. However, opens are not de-duplicated to prevent the illusion that an email opened by a user with multiple [User Profiles]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) under a single email address would only be counted towards a single User Profile.
{% endalert %}

### Retention Report

On the **Retention Report** page, you can run various reports to measure user retention for users who have performed a selected retention event in a specific campaign. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/).

### Funnel Report

On the **Funnel Report** page, you can analyze the journeys your customers take after receiving your campaign. If your campaign uses a control group or multiple variants, you will be able to understand how the different variants have impacted the conversion funnel at a more granular level, and optimize based on this data. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/).

[1]: {% image_buster /assets/img_archive/newcampaign_new.png %}
[3]: {% image_buster /assets/img_archive/choose_email_creation.png %}
[5]: {% image_buster /assets/img_archive/targetsegment_email_new.png %}
[6]: {% image_buster /assets/img_archive/confirm_email.png %}
[9]: https://www.braze.com/customers
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#intelligent-selection
[14]: {% image_buster /assets/img/email.jpg %}
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[16]: {{site.baseurl}}/help/best_practices/email/email_styling_tips/#email-size
[17]: {% image_buster /assets/img_archive/email_click_results_heatmap.gif %}
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[19]: {% image_buster /assets/img_archive/new_campaign_email.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/