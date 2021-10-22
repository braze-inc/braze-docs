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

> This reference article goes over how to send test messages across the different Braze channels and how to incorporate custom event properties and user attributes. 
> <br>
> <br>
> By testing out your campaigns, you can make sure everything about it is just right!

Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. You can create and send test messages to select devices or team members using the tools in the dashboard.

{% alert important %}
Make sure to save your campaign draft after testing to avoid deleting your campaign. You can send test messages without saving the message as a draft.
{% endalert %}

## Channel-specific test sending

For steps to send test messages, refer to the section for your channel below.

{% tabs %}
{% tab Email %}

#### Email

After drafting your email message, click **Preview and Test**. From this page, select the **test send** tab and add your email address or user ID in the **add individual users** field. When you're ready, click **send test** to send your drafted email to your inbox.

![Test Email]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Mobile push

After drafting your mobile push, select the **Settings** tab and add your email address or user ID in the **Add Individual Users** field. When you're ready, click **Send Test** to send your drafted message to your device.

![Test Push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

After creating your web push, select the **Settings** tab. Check **Send Test to Myself** and click **Send Test**.

![Test Web Push]({% image_buster /assets/img_archive/testwebpush.png %})

If you have already accepted push messages from the Braze dashboard, you will see the push come through in the corner of your screen. Otherwise, click **Allow** when prompted, and the message will appear.

{% endtab %}
{% tab In-App Message %}

#### In-app message

If you have push notifications set up within your app and on your test device, you can send test in-app messages to your app to see what it looks like in real-time. After drafting your in-app message, select the **Test** tab and add your email address or user ID to the **Add Individual Users** field. When you're ready, click **Send Test**. A test push message will appear at the top of your device screen. 

![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

Directly clicking and opening the push message will send you to your app, where you'll be able to view your in-app message test.

{% endtab %}
{% tab Content Card %}

#### Content card

After creating your Content Card, you can send a test Content Card to your app to see what it will look like in real-time. After drafting your Content Card, select the __Test__ tab and select at least one Content Test Group or individual user to receive this test message. 

![Test Content Card]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

#### SMS/MMS

After creating your SMS/MMS message, you can send a test message to your phone to see what it will look like in real-time. After drafting your message, select the __Test__ tab and select at least one Content Test Group or individual user to receive this test message. 

![Test Content Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

#### Webhook

After creating your webhook, you can do a test send to check the webhook response. Select the __test__ tab and select __send test__ to send a test send to the supplied webhook URL. You may also select an individual user to preview the response as a specific user. 

![Test Content Card]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

#### News Feed card

Sending a test News Feed card requires you to set up a test segment and subsequently send a test campaign out.

##### Step 1: Create a designated test segment

Once you set up a test segment, you can utilize these messaging channels. The process takes a few short steps and, if configured properly, will only need to be done once.

Go to the **Segments** page and create a new segment. In the dropdown menu under **Add Filter**, locate the testing filters at the bottom of the list.

![Testing Filters]({% image_buster /assets/img_archive/testmessages1.png %})

Use these testing filters to select users with specific email addresses or external [user IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/).

![Testing Filter Options]({% image_buster /assets/img_archive/testmessages2.png %})

These filters have the following options:

1. **Equals** - Looks for an exact match of the email or user ID you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID.
2. **Does not equal** - Use this if you want to exclude a particular email or user ID from test campaigns.
3. **Matches** - Finds users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users with an "@yourcompany.com" address, allowing you to send messages to everyone on your team.

These filters can also be used in conjunction to narrow down your list of test users. For example, the test segment could include an email address filter that `matches` "@braze.com" and another filter that `does not equal` "sales@braze.com". You can also select multiple specific emails by using the `matches` option and separating the email addresses with a "\|" character (e.g. `matches` "email1@braze.com\|email2@braze.com").

After adding the testing filters to your test segment, verify that you've selected only the users you intended by clicking **Preview** at the top of the segment editor or by exporting that segment's user data to CSV. To export segment user data, click the **User Data** dropdown and select **CSV Export All User Data**.

![Verify Test Segment]({% image_buster /assets/img_archive/testmessages3.png %})

> Exporting the segment's User Data to CSV will give you the most accurate picture of who falls under that segment. The **Preview** tab is only a sample of users in the segment and therefore may appear to have not selected all intended members. For more information, check out [Viewing and Understanding Segment Data][7].

Once you've confirmed that you're only targeting the users you want to receive the test message, you can either select this segment in an existing campaign that you want to test or click the **Start Campaign** button in the segment menu.

##### Step 2: Send a test campaign

To send test News Feed cards, you need to target your previously created test segment. Begin by creating a multichannel campaign and following the usual steps. When you reach the **Target Users** step, select your test segment as shown below.

![Test Segment]({% image_buster /assets/img_archive/test_segment.png %})

Finish confirming your campaign and launch it to test your News Feed cards.

>  Be sure to check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard if you intend to use a single campaign to send a test message to yourself more than once.

{% endtab %}
{% endtabs %}

## Campaign personalized with user attributes

If you are using [personalization][26] in your message, you'll need to take additional steps to properly preview your campaign and check that user data is properly populating the content.

When sending a test message, make sure to choose either the option to **Select Existing User** or preview as a **Custom User**.

![Testing a personalized message][23]{: style="max-width:70%;" }

If selecting an existing user, enter a specific app user's user ID or email in the search field. Then use the dashboard preview to see how your message would appear to that user, and send a test message to your device that reflects what that user would see.

![Select a user][24]

If previewing as a customized user, enter text for various fields available for personalization, such as the user's first name and any custom attributes. Once again, you can enter your own email address to send a test to your device.

![Custom user][25]

## Campaign personalized with custom event properties

Testing campaigns [personalized][20] with [custom event properties][19] differs slightly from testing other types of campaigns outlined above. The most robust way to test campaigns personalized using custom event properties is to trigger the campaign yourself. Begin by writing up the copy involving the event property:

![Composing Test Message with Properties][15]

Then use [action-based delivery][21] to deliver the campaign when the event occurs. 

{% alert note %}
If you're testing an iOS Push campaign, you must set the delay to 1 minute to allow yourself time to exit the app since iOS doesn't deliver push notifications for the currently open app. Other types of campaigns can be set to deliver immediately.
{% endalert %}

![Test Message Delivery][16]

As described above, target the users as you would for testing using either a testing filter or by targeting your own email address and finish creating the campaign.

![Test Message Targeting][17]

Go into your app and complete the custom event, and the campaign will trigger, and you should see the message customized with the event property:

![Test Message Example][18]

Alternatively, if you are saving custom user IDs, you can also test the campaign by sending a customized test message to yourself. After writing the copy for your campaign, select the **Test** tab and choose **Customized User**. Add the custom event property on the bottom of the page, add your user ID or email address to the top box, and click **Send Test**. 

You should receive a message personalized with the property.

![Testing Using Customized User][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/