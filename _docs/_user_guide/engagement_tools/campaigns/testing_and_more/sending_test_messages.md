---
nav_title: Sending test messages
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

A convenient way to organize your test users is by creating a [Content Test Group]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), which includes a group of users that will receive test messages from campaigns. You can add this test group to the **Add Content Test Groups** field under **Test Recipients** in your campaign, and launch your tests without creating or adding individual test users.

## Step 2: Send channel-specific test messages

For steps to send test messages, refer to the following section for your respective channel.

{% tabs %}
{% tab Email %}

1. Draft your email message.
2. Select **Preview and Test**.
3. Select the **Test Send** tab and add your email address or user ID in the **Add individual users** field. 
4. Select **Send Test** to send your drafted email to your inbox.

![Test Email]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Mobile push

1. Draft your mobile push.
2. Select the **Settings** tab and add your email address or user ID in the **Add Individual Users** field.
3. Select **Send Test** to send your drafted message to your device.

![Test push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Create your web push.
2. Select the **Test** tab. 
3. Select **Send Test to Myself**.
4. Select **Send Test** to send your web push to your web browser.

![Test web push]({% image_buster /assets/img_archive/testwebpush.png %})

If you have already accepted push messages from the Braze dashboard, the push will come through in the corner of your screen. Otherwise, click **Allow** when prompted, and the message will appear.

{% endtab %}
{% tab In-App Message %}

If you have push notifications set up within your app and on your test device, you can send test in-app messages to your app to see what it looks like in real-time. 

1. Draft your in-app message.
2. Select the **Test** tab and add your email address or user ID to the **Add Individual Users** field. 
3. Select **Send Test** to send your push message to your device.

A test push message will appear at the top of your device screen.

![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

Directly clicking and opening the push message will send you to your app, where you can view your in-app message test. Note this in-app message testing feature relies on the user clicking a test push notification to trigger the in-app message. As such, the user must be eligible to receive push notifications in the relevant app for the successful delivery of the test push notification.

{% endtab %}
{% tab Content Card %}

After creating your Content Card, you can send a test Content Card to your app to see what it will look like in real-time.

1. Draft your Content Card.
2. Select the **Test** tab and select at least one Content Test Group or individual user to receive this test message. 
3. Select **Send Test** to send your Content Card to your app.

![Test Content Card]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

After creating your SMS or MMS message, you can send a test message to your phone to see what it will look like in real-time. 

1. Draft your SMS or MMS message.
2. Select the **Test** tab and select at least one Content Test Group or individual user to receive this test message. 
3. Select **Send Test** to send your test message.

![Test Content Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

After creating your webhook, you can do a test send to check the webhook response. Select the **Test** tab and select **Send Test** to send a test send to the supplied webhook URL. You can also select an individual user to preview the response as a specific user. 

![Test Content Card]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% endtabs %}

## Testing personalized campaigns 

If you are testing campaigns that populate user data or use custom event properties, you'll need to take additional or different steps.

### Testing campaigns personalized with user attributes

If you are using [personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) in your message, you'll need to take additional steps to properly preview your campaign and check that user data is properly populating the content.

When sending a test message, make sure to choose either the option to **Select Existing User** or preview as a **Custom User**.

![Testing a personalized message]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Selecting an existing user

If selecting an existing user, enter the specific user ID or email in the search field. Then, use the dashboard preview to see how your message would appear to that user, and send a test message to your device that reflects what that user would see.

![Select a user]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Selecting a custom user

If previewing as a custom user, enter text for various fields available for personalization, such as the user's first name and any custom attributes. Once again, you can enter your own email address to send a test to your device.

![Custom user]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Testing campaigns personalized with custom event properties

Testing campaigns personalized with [custom event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) differs slightly from testing other types of campaigns outlined. 

#### Method 1: Triggering campaign manually

You can trigger the campaign yourself as a robust way to test campaigns personalized using custom event properties:

1. Write up the copy involving the event property. 

![Composing Test Message with Properties]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Use [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) to deliver the campaign when the event occurs.

{% alert note %}
If you're testing an iOS push campaign, you must set the delay to one minute to allow yourself time to exit the app because iOS doesn't deliver push notifications for the currently open app. Other types of campaigns can be set to deliver immediately.
{% endalert %}

![Test Message Delivery]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Target the users as you would for testing by using a testing filter or targeting your own email address, and finish creating the campaign. 

![Test Message Targeting]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Go into your app and complete the custom event.

The campaign will trigger and show the message customized with the event property.

![Test Message Example]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

#### Method 2: Sending yourself a test message

Alternatively, if you are saving custom user IDs, you can also test the campaign by sending a customized test message to yourself.

1. Write the copy for your campaign.
2. Select the **Test** tab and choose **Customized User**. 
3. Add the custom event property at the bottom of the page, and add your user ID or email address to the top box.
4. Select **Send Test** to receive a message personalized with the property.

![Testing Using Customized User]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

#### Method 3: Using Liquid

You can test custom event properties by manually inputting values with Liquid. 

1. In the message editor, input values for your custom event properties.
2. Select the **Preview as a User** tab to check that the correct message displays.

## Troubleshooting

### In-app messages

If your in-app message campaign is not triggered by a push campaign, check the in-app campaign segmentation to confirm the user meets the target audience **before** receiving the push message.

For test sends on Android and iOS, the in-app messages that use the **Request push permission** on-click behavior may not display on some devices. As a workaround:
- **Android:** Devices must be on Android 13 and our Android SDK version 21.0.0. Another reason may be that the device on which the in-app message is displayed already has a system-level prompt. You may have selected **Do not ask again**, so you may need to reinstall the app to reset the notification permissions before testing again.
- **iOS:** We recommend your developer team review the implementation of push notifications for your app and manually remove any code that would request push permissions. For more information, see [Push primer in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

For an action-based in-app message campaign to deliver, custom events must be logged through the Braze SDK, not REST APIs, so the user can receive eligible in-app messages directly to their device. Users can receive the in-app message if they perform the event during the session.
