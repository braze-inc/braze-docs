---
nav_title: Capturing Lapsing Users
article_title: Capturing Lapsing Users
page_order: 1
page_type: tutorial
description: "This how-to article addresses the issue of lapsing users and how to effectively use Braze campaigns to re-engage those users."
tool:
  - Segments
  - Campaigns

---

# Capturing lapsing users

> This how-to article addresses the issue of lapsing users and how to effectively use Braze campaigns to re-engage those users.

If your audience is dwindling, it’s crucial to try wooing them back. Recognizing this necessity, Braze makes it easy to set up automated recurring re-engagement campaigns to capture lapsing users. You can choose the re-engagement timeframe and recurrence that best suits your app, but to demonstrate, we'll get started with a 14 day re-engagement plan.

For more on targeting users, check out our [LAB course](http://lab.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup!

## Step 1: Segmentation

First, we’ll create a segment to target users who have not used the app in the past two weeks, using the following filters:

- Last Used App more than 2 weeks ago
- Last Used App less than 3 weeks ago

![][1]

Don’t forget to name the segment something simple and memorable, like “Lapsed Users – 2 Weeks.” Since we’ll be setting up the campaign to recur on a weekly basis, we’ll want to make sure there’s at least one week of users captured in the segment. That’s why we’ve selected users who last used the app between two to three weeks ago.

## Step 2: Campaign creation

Next, click **Create Campaign** and choose the type of campaign we will be sending to this segment. in this example, we'll create a new [push campaign][6].

![][5]

We’ll name the campaign **Message to Lapsed Users - 2 Weeks** and select the segment. Here, we will create the content of our message. In this example, we’ll only target iOS users, but you can use Braze for Android and iOS push notifications. The closer to the last time a user was in the app, the more important it is to be topical and relevant. Messaging a user after two weeks of not using the app, it's important to surface relevant content and highlight the benefits of using the app.

![][2]

Next, we'll create a recurring schedule to send our weekly message on Thursdays at 5:45pm using [local time zone delivery][4] in **Time-Based Scheduling Options**. We recommended that you look at your sessions graph to target users just prior to high-usage periods. This ensures that you attempt to re-engage people when they’re most likely to use the app. You can change this later and test your initial hypothesis.

![][3]

Now, you’re ready to send the campaign. Confirm the settings on the last page of the wizard and click **Launch Campaign**!

[1]: {% image_buster /assets/img_archive/2weeklapse1.png %}
[2]: {% image_buster /assets/img_archive/2weeklapse3.png %}
[3]: {% image_buster /assets/img_archive/2weeklapse4.png %}
[4]: {{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer
[5]: {% image_buster /assets/img_archive/2weeklapse2.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message