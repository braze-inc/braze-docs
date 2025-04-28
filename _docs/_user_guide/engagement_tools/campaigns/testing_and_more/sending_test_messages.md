---
nav_title: Sending Test Messages
article_title: Sending Test Messages
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "This reference article covers how to send test messages across the different Braze channels and how to incorporate custom event properties or user attributes."

---

# Sending test messages

> Before sending a messaging campaign to your users, as a suggested best practice, we recommend testing to make sure it looks right and operates as intended. You can create and send test messages to select devices or team members using the tools in the Braze dashboard.

{% alert important %}
Make sure to save your campaign draft after testing to avoid deleting your campaign. You can send test messages without saving the message as a draft.
{% endalert %}

## Step 1: Identify your test users

Before testing your messaging campaign, it's important to identify your test users. These users can be either existing user IDs or email addresses, or new users that are used exclusively for testing messaging campaigns. 

### Optional: Create a Content Test Group

A convenient way to organize your test users is by creating a [Content Test Group]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), which includes a group of users that will receive test messages from campaigns. You can add this test group into the **Add Content Test Groups** field under **Test Recipients** in your campaign, and launch your tests without creating or adding individual test users.

## Step 2: Send channel-specific test messages

For steps to send test messages, refer to the following section for your respective channel.

{% tabs %}
{% tab Email %}

1. Draft your email message.
2. Click **Preview and Test**.
3. Select the **Test Send** tab and add your email address or user ID in the **Add Individual Users** field. 
4. Click **Send Test** to send your drafted email to your inbox.

![Test Email]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Mobile push

1. Draft your mobile push.
2. Select the **Settings** tab and add your email address or user ID in the **Add Individual Users** field.
3. Click **Send Test** to send your drafted message to your device.

![Test push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Create your web push.
2. Select the **Test** tab. 
3. Check **Send Test to Myself**.
4. Click **Send Test** to send your web push to your web browser.

![Test web push]({% image_buster /assets/img_archive/testwebpush.png %})

If you have already accepted push messages from the Braze dashboard, the push will come through in the corner of your screen. Otherwise, click **Allow** when prompted, and the message will appear.

{% endtab %}
{% tab In-App Message %}

If you have push notifications set up within your app and on your test device, you can send test in-app messages to your app to see what it looks like in real-time. 

1. Draft your in-app message.
2. Select the **Test** tab and add your email address or user ID to the **Add Individual Users** field. 
3. Click **Send Test** to send your push message to your device.

A test push message will appear at the top of your device screen.

![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

Directly clicking and opening the push message will send you to your app, where you can view your in-app message test. Note this in-app message testing feature relies on the user clicking a test push notification to trigger the in-app message. As such, the user must be eligible to receive push notifications in the relevant app for the successful delivery of the test push notification.

#### Troubleshooting

* If your in-app message campaign is not triggered by a push campaign, check the in-app campaign segmentation to confirm the user meets the target audience **before** receiving the push message.
* For test sends on Android and iOS, the in-app messages that use the **Request push permission** on-click behavior may not display on some devices. As a workaround:
  * **Android:** Devices must be on Android 13 and our Android SDK version 21.0.0. Another reason may be that the device on which the in-app message is displayed already has a system-level prompt. You may have selected **Do not ask again**, so you may need to reinstall the app to reset the notification permissions before testing again.
  * **iOS:** We recommend your developer team review the implementation of push notifications for your app and manually remove any code that would request push permissions. For more information, see [Push primer in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
* For an action-based in-app message campaign to deliver, custom events must be logged through the Braze SDK, not REST APIs, so the user can receive eligible in-app messages directly to their device. Users can receive the in-app message if they perform the event during the session.

{% endtab %}
{% tab Content Card %}

After creating your Content Card, you can send a test Content Card to your app to see what it will look like in real-time.

1. Draft your Content Card.
2. Select the **Test** tab and select at least one Content Test Group or individual user to receive this test message. 
3. Click **Send Test** to send your Content Card to your app.

![Test Content Card]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

After creating your SMS or MMS message, you can send a test message to your phone to see what it will look like in real-time. 

1. Draft your SMS or MMS message.
2. Select the **Test** tab and select at least one Content Test Group or individual user to receive this test message. 
3. Click **Send Test** to send your test message.

![Test Content Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

After creating your webhook, you can do a test send to check the webhook response. Select the **Test** tab and select **Send Test** to send a test send to the supplied webhook URL. You can also select an individual user to preview the response as a specific user. 

![Test Content Card]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Sending a test News Feed card requires you to set up a test segment and subsequently send a test campaign out.

##### Step 1: Create a designated test segment

Once you set up a test segment, you can use these messaging channels. The process takes a few short steps and, if configured properly, will only need to be done once.

1. Go to the **Segments** page and [create a new segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 
2. Click the dropdown menu under **Add Filter** and locate the testing filters at the bottom of the list <br><br>![Testing Filters]({% image_buster /assets/img_archive/testmessages1.png %})<br><br>
3. Use the testing filters to select users with specific email addresses or external [user IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift).<br><br>![Testing Filter Options]({% image_buster /assets/img_archive/testmessages2.png %})
<br><br>These filters have the following options:
- **Equals**: Looks for an exact match of the email or user ID you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID.
- **Does not equal**: Excludes a particular email or user ID from test campaigns.
- **Matches**: Finds users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users with an "@yourcompany.com" address, allowing you to send messages to everyone on your team.
<br><br>
These filters can also be used in conjunction to narrow down your list of test users. For example, the test segment could include an email address filter that `matches` "@braze.com" and another filter that `does not equal` "sales@braze.com". You can also select multiple specific emails by using the `matches` option and separating the email addresses with a "\|" character (for example, `matches` "email1@braze.com\|email2@braze.com").
<br><br>
4. Add the testing filters to your test segment.
5. Click **Preview** at the top of the segment editor or export that segment's user data to CSV to verify that you've selected only the users you intended.
6. Click the **User Data** dropdown and select **CSV Export All User Data** to export segment user data. 

![Verify Test Segment]({% image_buster /assets/img_archive/testmessages3.png %})

> Exporting the segment's User Data to CSV will give you the most accurate picture of who falls under that segment. The **Preview** tab is only a sample of users in the segment and therefore may appear to have not selected all intended members. For more information, check out [Viewing and Understanding Segment Data][7].

After you've confirmed that you're only targeting the users you want to receive the test message, you can either select this segment in an existing campaign that you want to test or click the **Start Campaign** button in the segment menu.

##### Step 2: Send a test campaign

To send test News Feed cards, you need to target your previously created test segment. Begin by creating a multichannel campaign and following the usual steps. When you reach the **Target Users** step, select your test segment as shown in the following image.

![Test Segment]({% image_buster /assets/img_archive/test_segment.png %})

Finish confirming your campaign and launch it to test your News Feed cards.

> If you intend to use a single campaign to send a test message to yourself more than once, check the box titled "Allow users to become re-eligible to receive campaign" under the **Schedule** portion of the campaign composer.

{% endtab %}
{% endtabs %}

## Testing personalized campaigns 

If you are testing campaigns that populate user data or use custom event properties, you'll need to take additional or different steps.

### Testing campaigns personalized with user attributes

If you are using [personalization][26] in your message, you'll need to take additional steps to properly preview your campaign and check that user data is properly populating the content.

When sending a test message, make sure to choose either the option to **Select Existing User** or preview as a **Custom User**.

![Testing a personalized message][23]{: style="max-width:70%;" }

#### Selecting an existing user

If selecting an existing user, enter the specific user ID or email in the search field. Then, use the dashboard preview to see how your message would appear to that user, and send a test message to your device that reflects what that user would see.

![Select a user][24]

#### Selecting a custom user

If previewing as a custom user, enter text for various fields available for personalization, such as the user's first name and any custom attributes. Once again, you can enter your own email address to send a test to your device.

![Custom user][25]

### Testing campaigns personalized with custom event properties

Testing campaigns personalized with [custom event properties][19] differs slightly from testing other types of campaigns outlined. The most robust way to test campaigns personalized using custom event properties is to trigger the campaign yourself by doing the following:

1. Write up the copy involving the event property. ![Composing Test Message with Properties][15]
2. Use [action-based delivery][21] to deliver the campaign when the event occurs.

{% alert note %}
If you're testing an iOS push campaign, you must set the delay to 1 minute to allow yourself time to exit the app since iOS doesn't deliver push notifications for the currently open app. Other types of campaigns can be set to deliver immediately.
{% endalert %}

![Test Message Delivery][16]

{: start="3"}
3. Target the users as you would for testing by using a testing filter or targeting your own email address, and finish creating the campaign. 

![Test Message Targeting][17]

{: start="4"}
4. Go into your app and complete the custom event.

The campaign will trigger and show the message customized with the event property.

![Test Message Example][18]

Alternatively, if you are saving custom user IDs, you can also test the campaign by sending a customized test message to yourself.

1. Write the copy for your campaign.
2. Select the **Test** tab and choose **Customized User**. 
3. Add the custom event property on the bottom of the page, and add your user ID or email address to the top box.
4. Click **Send Test** to receive a message personalized with the property.

![Testing Using Customized User][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/
