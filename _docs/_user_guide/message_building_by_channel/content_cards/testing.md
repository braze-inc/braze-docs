---
nav_title: Testing
article_title: Testing Content Cards
page_order: 3
description: "This reference article covers how to preview and test Content Cards, as well as some best practices."
channel:
  - content cards
  
---

# Testing Content Cards

It is extremely important to always test your Content Cards before sending your campaigns. Our preview and testing capabilities offer two ways to take a look at your Content Cards. You can preview your message to help you visualize as you compose it, as well as send a test message to yourself or a specific user's device. We recommend you take advantage of both.

## Preview

You can preview your card as you compose it. This should help you visualize what your final message will look like from your user's perspective.

In the __Preview__ tab of your composer, the view of your message might not be identical to its actual rendering on the user's device. We recommend always sending a test message to a device to ensure that your media, copy, personalization, and custom attributes generate correctly.

## Test

To send a test to either [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, push must be enabled on your test devices before sending. For iOS users, you must tap the push notification sent by Braze in order to view the test Content Card. This behavior only applies to test Content Cards.

### Preview message as user

You can also preview messages from the **Test** tab as if you were a user. You can select a specific user, a random user, or create a custom user.

![Custom_User_Preview][3]

### Test checklist

- Do the images and media show up and act as expected?
- Does the Liquid function as expected? Have you accounted for a [default attribute value]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
- Do your links direct the user to where they should go?

## Debug

After your Content Cards are sent, you can break down or debug any issues from the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) in the Developer Console. 

A common use case is trying to debug why a user can't see a particular Content Card. To do so, you can look in the **Event User Logs** for the Content Cards delivered to the SDK on session start, but prior to an impression, and trace those back to a specific campaign:

1. Go to the **Developer Console** and select the **Event User Log** tab.
2. Locate and expand the SDK Request for your test user.
3. Click **Raw Data**.
4. Find the `id` for your session. An example excerpt is shown below:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NjE4NTAwNWE5ZDliZWU3OTM4N2NjZTQzXyRfY2M9YzNiMjU3NDAtZjExMy1jMDQ3LTRiMWQtZDI5NmYyODBhZjRmJm12PTYxODUwMDViOWQ5YmVlNzkzODdjY2U0NSZwaT1jbXA="
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Use a decoding tool like [Base64 Decode and Encode](https://www.base64decode.org/) to decode the `id` from Base64 format and find the associated `campaign_id`. In our example above, this results in the following:

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Where `6185005a9d9bee79387cce43` is the `campaign_id`.<br><br>

6. Go to the **Campaigns** page and search for the `campaign_id`.

From there, you can review your message settings and content to drill down and determine why a user can't see a particular Content Card.

[3]: {% image_buster /assets/img/cc-user-preview.png %}
