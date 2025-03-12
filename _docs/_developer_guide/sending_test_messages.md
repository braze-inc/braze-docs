---
nav_title: Sending Test Messages
article_title: Sending Test Messages
page_order: 4.0
description: "This reference article covers sending test messages for different channels."

---

# Sending test messages

> Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. Creating and sending test messages to select devices or members of your team is very simple using the tools in the dashboard.

## Creating a designated test segment <a class="margin-fix" name="test-segment"></a>

Once you set up a test segment, you can use it to test **any** of our messaging channels. If configured properly, the process will only need to be done once.

To set up a test segment, navigate to the **Segments** page in the dashboard and create a new segment. Click **Add Filter** to choose one of the testing filters found toward the bottom of the dropdown menu.

![A Braze test campaign displaying the filters available in the targeting step.]({% image_buster /assets/img_archive/testmessages1.png %})

Two such testing filters allow you to select users with specific email addresses or external [user IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids).

![A dropdown menu displaying several filters listed under a heading that reads Testing]({% image_buster /assets/img_archive/testmessages2.png %})

The email address and external user ID filters both have three options:

  1) **"Equals"** - This will look for an exact match of the email or user ID that you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID.

  2) **"Does Not Equal"** - Use this if you want to exclude a particular email or user ID from test campaigns.

  3) **"Matches"** - This will find users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users that have an "@yourcompany.com" address, allowing you to send messages to everyone on your team.

You can select multiple specific emails by using the "matches" option and separating the email addresses with a &#124; character (for example, "matches" "email1@braze.com &#124; email2@braze.com").

These filters can also be used in conjunction with each other to narrow down your list of test users. For example, the test segment could include an email address filter that "matches" "@braze.com" and another filter that "does not equal" "sales@braze.com". 

After adding the testing filters to your test segment, you can verify that you've selected only the users you intended by clicking **Preview** at the top of the segment editor or by exporting that segment's user data to CSV by clicking on the gear icon in the right-hand corner of the editor and selecting **CSV Export All User Data** from the dropdown menu.

![A section of a Braze campaign titled Segment Details]({% image_buster /assets/img_archive/testmessages3.png %})

>  Exporting the segment's User Data to CSV will give you the most accurate picture of who falls under that segment. The **Preview** tab is only a sample of the users in the segment and therefore may appear to have not selected all intended members.

## Sending a test push notification or in-app messages <a class="margin-fix" name="push-inapp-test"></a>

To send test push notifications or in-app messages, you need to target your previously created test segment. Begin by creating your campaign and following the usual steps. When you reach the **Target Users** step, select your test segment from the dropdown menu.

![A Braze test campaign displaying the segments available in the targeting step.]({% image_buster /assets/img_archive/test_segment.png %})

Finish confirming your campaign and launch it to test your push notification and in-app messages.

>  Be sure to select **Allow users to become re-eligible to receive campaign** under the **Schedule** portion of the campaign composer if you intend to use a single campaign to send a test message to yourself more than once.

## Sending a test email message

If you're only testing email messages, you do not necessarily have to set up a test segment. In the first step of the campaign composer where you compose your campaign's email message, click **Send Test** and enter the email address to which you wish to send a test email. 

![A Braze campaign with the Test Send tab selected]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %} 
You can also enable or disable [TEST (or SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) being appended on your test messages.
{% endalert %}

## Testing from the command line

Alternatively, if you'd like to test push notifications via the command line you can follow the following examples for each platform.

### Testing push with iOS apps via cURL

You can send a single notification through the terminal via CURL and the [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available at **Settings** > **API Keys**
- `YOUR_EXTERNAL_USER_ID` - available on the the **Search Users** page
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), these pages are in a different location: <br>- **API Keys** is located at **Developer Console** > **API Settings** <br>- **Search Users** is located at **Users** > **User Search**
{% endalert %}

>  The following examples demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance, refer to our [API documentation]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Testing push with Android apps via cURL

You can send a single notification through the terminal via cURL and the [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` (Go to **Settings** > **API Keys**.)
- `YOUR_EXTERNAL_USER_ID` (Search for a profile on the **Search Users** page.)
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

>  The following examples demonstrate the appropriate API endpoints for customers on the `US-01` instance. If you are not on this instance, refer to our [API documentation]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) to see which endpoint to make requests to.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Testing push with Kindle apps via cURL

You can send a single notification through the terminal via cURL and the [Messaging API]({{site.baseurl}}/api/endpoints/messaging/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the **Developer Console** page
- `YOUR_EXTERNAL_USER_ID` - available on the the **User Search** page
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Limitations of test messages

There are a few situations where test messages don't have complete feature parity with launching a campaign or Canvas to a real set of users. In these instances, to validate this behavior, you should launch the campaign or Canvas to a limited set of test users.

- Viewing the Braze [preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) from **Test Messages** will cause the submit button to be grayed out
- The list-unsubscribe header is not included in emails sent by the test message functionality
- For in-app messages and Content Cards, the target user must have a push token for the target device

