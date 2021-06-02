---
nav_title: Sending Test Messages
platform: Campaigns
subplatform: Testing and More
page_order: 3

tool: 
- Campaigns
- Segments
page_type: reference
description: "This reference article covers how to send test messages across the different Braze channels and how to incorporate custom event properties or user attributes."
---
# Sending Test Messages

> This reference article goes over how to send test messages across the different Braze channels, as well as how to incorporate custom event properties and user attributes. 
> <br>
> <br>
> By testing out your campaigns you can make sure everything about it is just right!

Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. Creating and sending test messages to select devices or members of your team is very simple using the tools in the dashboard.

## Sending a Test Mobile Push Notification or Email Message

After drafting your Push or Email, you have the ability to send the message to your own device to see what it looks like in real-time. In the settings bar, click the "eye" icon, input your email address or userID, and click "Send Test." This will send the message that you drafted to your device.

This is what the testing process will look like for a push message.

![Test Push][10]

And here is what the process will look like for an email message.

![Test Email][9]

Keep in mind that you will either need your users' email address or Braze UserID to send test messages to your device.

## Sending a Test Web Push Notification

After drafting your web push, you have the ability to send the message to your computer to see what it looks like in real-time. In the settings bar, click the "eye" icon, and click "Send Test to Myself."

![Test Web Push][11]

If you have already accepted push messages from the Braze Dashboard, you will see the push come through in the corner of your screen. Otherwise, please click "Allow" when prompted, and the message will then appear.

## Sending a Test In-App Message

If you have push notifications set up within your app and on your test device, you have the ability to send test in-app messages to your app to see what it looks like in real-time. In the settings bar, click the "eye" icon, input your email address or userID, and click "Send Test:"

![Test In App][14]

This will send a push message to your device like the following:

![Test Push for In App][13]

Directly clicking and opening the push message will send you to your app where you'll be able to view your in-app message test.

## Sending a Test News Feed Card

Sending a test News Feed card requires you to set up a test segment and subsequently send a test campaign out.

### Creating a Designated Test Segment

Once you set up a test segment, you can utilize these messaging channels. The process is very simple and if configured properly will only need to be done once.

Navigate to the "Segments" page in the dashboard and create a new segment. In the dropdown menu under "Add Filter", you'll find our testing filters at the bottom of the list.

![Testing Filters][1]

Our testing filters allow you to select users with specific email addresses or external [user IDs][2].

![Testing Filter Options][3]

These filters have three options:

1. __"Equals"__ - This will look for an exact match of the email or user ID that you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID.
2. __"Does Not Equal"__ - Use this if you want to exclude a particular email or user ID from test campaigns.
3. __"Matches"__ - This will find users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users that have an "@yourcompany.com" address, allowing you to send messages to everyone on your team.

These filters can also be used in conjunction with each other to narrow down your list of test users. For example, the test segment could include an email address filter that `matches` "@braze.com" and another filter that `does not equal` "sales@braze.com". You can also select multiple specific emails by using the   `matches` option and separating the email addresses with a "\|" character (e.g. `matches` "email1@braze.com\|email2@braze.com").

After adding the testing filters to your test segment, you can verify that you've selected only the users you intended by clicking "Preview" at the top of the segment editor or by exporting that segment's user data to CSV by clicking on the gear icon in the right-hand corner of the editor and selecting "CSV Export All User Data" from the dropdown menu.

![Verify Test Segment][4]

> Exporting the segment's User Data to CSV will give you the most accurate picture of who falls under that segment. The "Preview" tab is only a sample of the users in the segment - [see more details about this in our FAQ][7] - and therefore may appear to have not selected all intended members.

Once you've confirmed that you're only targeting the users that you want to receive the test message, you can either select this segment in an existing campaign that you want to test or click the "Start Campaign" button in the segment menu.

## Sending the Test Campaign

In order to send test News Feed cards, you need to target your previously created test segment. Begin by creating a Multi-Channel campaign and following the usual steps. When you reach the 'Target Users' section, select your test segment as shown below.

![Test Segment][8]

Finish confirming your campaign and launch it to test your News Feed cards.

>  Be sure to check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard if you intend to use a single campaign to send a test message to yourself more than once.

## Sending a Test Campaign Personalized with User Attributes

If you are using [personalization][26] in your message, you'll need to take some additional steps to properly preview your campaign and check that user data is properly populating the content.

When sending a test message, make sure to choose either the option to "Select Existing User" or preview as a "Custom User."

![Testing a personalized message][23]

If selecting a user, you'll be able to enter the user ID or email of a specific app user into a search field. Then you'll be able to use the dashboard preview to see how that user's message would appear and send a test message to your device that reflects that that user would see.

![Select a user][24]

If previewing as a customized user, you'll be able to enter in text for various fields available for personalization, such as first name and any custom attributes. Once again, you can enter your own email address to send a test to your device.

![Custom user][25]

## Sending a Test Campaign Personalized with Custom Event Properties
Testing campaigns [personalized][20] with [Custom Event Properties][19] differ slightly from testing other types of campaigns outlined above. The most robust way to test campaigns personalized using Custom Event Properties is to trigger the campaign yourself. Begin by writing up the copy involving the event property:

![Composing Test Message with Properties][15]

Then use [Action Based Delivery][21] to deliver the campaign when the event occurs. 

{% alert note %}
If you're testing an iOS Push campaign, you must set the delay to 1 minute to allow yourself time to exit the app, since iOS doesn't deliver push notifications for the currently open app. Other types of campaigns can be set to deliver immediately.
{% endalert %}

![Test Message Delivery][16]

As described above, target the users as you would for testing using either a testing filter or simply targeting your own e-mail address and finish creating the campaign.

![Test Message Targeting][17]

Go into your app and complete the custom event, and the campaign will trigger, and you should see the message customized with the event property:

![Test Message Example][18]

Alternatively, if you are saving custom user IDs, you can also test the campaign by sending a customized test message to yourself. After writing the copy for your campaign, click the eye icon on the upper right corner of the preview, then select "Customized User". Add the custom event property on the bottom of the page, add your user ID or e-mail address to the top box and click "Send Test". You should receive a message personalized with the property.

![Testing Using Customized User][22]

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#user-preview
[8]: {% image_buster /assets/img_archive/test_segment.png %}
[9]: {% image_buster /assets/img_archive/testemail.png %}
[10]: {% image_buster /assets/img_archive/testpush.png %}
[11]: {% image_buster /assets/img_archive/testwebpush.png %}
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[14]: {% image_buster /assets/img_archive/test-in-app.png %}
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
