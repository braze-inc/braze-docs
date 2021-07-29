---
nav_title: Sending Test Messages
page_order: 3
description: "THis reference article covers sending test messages for different channels."

---

# Sending Test Messages

Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. Creating and sending test messages to select devices or members of your team is very simple using the tools in the dashboard.

## Creating a Designated Test Segment <a class="margin-fix" name="test-segment"></a>

Once you set up a test segment, you can utilize it to test __any__ of our messaging channels. The process is very simple and if configured properly will only need to be done once.

Navigate to the "Segments" page in the dashboard and create a new segment. In the dropdown menu under "Add Filter", you'll find our testing filters at the bottom of the list.

![Testing Filters][1]

Our testing filters allow you to select users with specific email addresses or external [user IDs][2].

![Testing Filter Options][3]

These filters have three options:

  1) __"Equals"__ - This will look for an exact match of the email or user ID that you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID.

  2) __"Does Not Equal"__ - Use this if you want to exclude a particular email or user ID from test campaigns.

  3) __"Matches"__ - This will find users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users that have an "@yourcompany.com" address, allowing you to send messages to everyone on your team.

These filters can also be used in conjunction with each other to narrow down your list of test users. For example, the test segment could include an email address filter that "matches" "@braze.com" and another filter that "does not equal" "sales@braze.com". You can also select multiple specific emails by using the "matches" option and separating the email addresses with a <code>|</code> character (e.g. "matches" "email1@braze.com &#124; email2@braze.com").

After adding the testing filters to your test segment, you can verify that you've selected only the users you intended by clicking "Preview" at the top of the segment editor or by exporting that segment's user data to CSV by clicking on the gear icon in the right-hand corner of the editor and selecting "CSV Export All User Data" from the dropdown menu.

![Verify Test Segment][4]

>  Exporting the segment's User Data to CSV will give you the most accurate picture of who falls under that segment. The "Preview" tab is only a sample of the users in the segment - [see more details about this in our FAQ][9] - and therefore may appear to have not selected all intended members.

Once you've confirmed that you're only targeting the users that you want to receive the test message, you can either select this segment in an existing campaign that you want to test or click **Start Campaign** in the segment menu.

## Sending a Test Push Notification or In-App Messages <a class="margin-fix" name="push-inapp-test"></a>

To send test push notifications and/or in-app messages, you need to target your previously created test segment. Begin by creating your campaign and following the usual steps. When you reach the **Target Users** step, select your test segment as shown below.

![Test Segment][11]

Finish confirming your campaign and launch it to test your push notification and in-app messages.

>  Be sure to check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard if you intend to use a single campaign to send a test message to yourself more than once.

>  If you're only testing email messages, you do not have to set up a test segment. In the first step of the campaign wizard where you compose your campaign's email message, there is a "Send Test" button in the bottom left corner.

## Sending a Test Email Message

![Send Test Button][5]

Clicking on this button causes a window to appear where you can enter the email address you would like the test email to be sent to. Click "Send Test" and your test email will be delivered shortly.


## Testing In-App Messages and Push via CURL
Alternatively, if you'd like to test in-app and push notifications via the command-line you can follow the following examples below for each platform.

### Testing Push with iOS Apps via CURL

You can send a single notification through the terminal via CURL and the [Messaging API][13]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][14] page
- `YOUR_EXTERNAL_USER_ID` - available on the [User Profile Search Page][15]
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)


>  The examples below demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"apple_push\":{\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```

### Testing Push with Android Apps via CURL

You can send a single notification through the terminal via cURL and the [Messaging API][13]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][14] page
- `YOUR_EXTERNAL_USER_ID` - available on the [User Profile Search Page][15]
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

>  The examples below demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"android_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```

### Testing Push with Kindle Apps via CURL

You can send a single notification through the terminal via cURL and the [Messaging API][13]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][14] page
- `YOUR_EXTERNAL_USER_ID` - available on the [User Profile Search Page][15]
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"kindle_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```

### Testing Push with Windows Universal Apps via CURL

You can send a single notification through the terminal via cURL and the [Messaging API][13]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][14] page
- `YOUR_EXTERNAL_USER_ID` - available on the [User Profile Search Page][15]
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

>  The examples below demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"windows_push\":{\"push_type\":\"toast_text_01\",\"toast_text1\":\"test_title\"}}}" https://rest.iad-01.braze.com/messages/send
```

### Testing Push with Windows Phone Apps via CURL

You can send a single notification through the terminal via cURL and the [Messaging API][13]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][14] page
- `YOUR_EXTERNAL_USER_ID` - available on the [User Profile Search Page][15]
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

>  The examples below demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance please refer to our [API documentation][66] to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"windows_push\":{\"push_type\":\"toast\",\"toast_title\":\"test_title\",\"toast_content\":\"message_goes_here\",\"toast_navigation_uri\":\"uri_goes_here\"}}}" https://rest.iad-01.braze.com/messages/send
```

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#setting-user-ids
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[5]: {% image_buster /assets/img_archive/testmessages45.png %}
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[11]: {% image_buster /assets/img_archive/test_segment.png %}
[13]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[14]: https://dashboard-01.braze.com/app_settings/api_settings/
[15]: https://dashboard-01.braze.com/users/user_search/user-search/
[66]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
