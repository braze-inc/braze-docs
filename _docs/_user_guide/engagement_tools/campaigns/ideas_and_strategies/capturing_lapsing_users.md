---
nav_title: Capturing Lapsing Users
platform: Campaigns
subplatform: Ideas and Strategies
page_order: 1

tools: campaigns
page_type: tutorial
description: "This how-to article addresses the issue of lapsing users and how to effectively use Braze Campaigns to re-engage those users."
---
# Capturing Lapsing Users

> This how-to article addresses the issue of lapsing users and how to effectively use Braze Campaigns to re-engage those users.

If your audience is dwindling, it’s crucial to try wooing them back. Recognizing this necessity, Braze makes it easy to set up automated recurring re-engagement campaigns to capture lapsing users. You can choose the re-engagement timeframe and recurrence that best suits your app, but to demonstrate, we'll get started with a 14 day (2 week) weekly re-engagement plan.

For more on targeting users, check out our [Campaign Set Up LAB course](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!


## Step 1: Segmentation

First, we’ll create a segment to target users who have not used the app in the past two weeks, using the following filters:

- Last Used App more than 2 weeks ago
- Last Used App less than 3 weeks ago

![SCREENSHOT][1]

Don’t forget to name the segment something simple and memorable, like “Lapsed Users – 2 Weeks.” Since we’ll be setting up the campaign to recur on a weekly basis, we’ll want to make sure there’s at least 1 week of users captured in the segment. That’s why we’ve selected users who last used the app between 2 and 3 weeks ago.

## Step 2: Campaign Creation

Next, we’ll click 'Create Campaign' and choose what type of campaign we will be sending to this segment.

![SCREENSHOT][5]

We’ll automatically name the campaign “Message to Lapsed Users - 2 Weeks” and select the segment. Here, we will create the content of our message. In the example, we’ll only target iOS users, but you can use Braze for Android and iOS push notifications. The closer to the last time a user was in the app, the more important it is to be topical and relevant. Messaging a user after two weeks of not using the app, it's important to surface relevant content and highlight the benefits of using the app.

![SCREENSHOT][2]

Step 2 is where we’ll create a recurring schedule. We’ll use [local time zone delivery][4] at 5 PM. It’s recommended that you look at your sessions graph to target users just prior to high-usage periods. This ensures that you attempt to re-engage people when they’re most likely to use the app. In addition to local time zone delivery, also check recurring and select weekly. Again, choose the day of the week that you think will resonate most with lapsed users. You can change this later and test your initial hypothesis.

![SCREENSHOT][3]

Now, you’re ready to send the campaign. Confirm the settings on the last page of the wizard and click 'Launch Campaign'!

[1]: {% image_buster /assets/img_archive/2weeklapse1.png %}
[2]: {% image_buster /assets/img_archive/2weeklapse3.jpg %}
[3]: {% image_buster /assets/img_archive/2weeklapse4.png %}
[4]: {{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer
[5]: {% image_buster /assets/img_archive/2weeklapse2.png %}
