---
page_order: 2
nav_title: In-App Messages
page_title: In-app messages for the Braze Roku SDK
platform: Roku
channel: in-app messages
description: "This article covers an overview of Roku in-app messaging, including best practices and use cases."
---

# In-app messages

> [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

Check out our [case studies](https://www.braze.com/customers) to see examples of in-app messages.

![Three images of potential Roku in-app messages that a user could build. These examples include "fullscreen takeover", "homepage banner", and "corner notifier".]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## Setting up in-app messages

### Prerequisites

Before you can use this feature, you'll need to [integrate the Braze Roku SDK]({{site.baseurl}}/developer_guide/platforms/roku/sdk_integration/). Additionally, in-app messages will only be sent to Roku devices running the minimum supported SDK version:

{% sdk_min_versions roku:0.1.2 %}

### Step 1: Add an observer

To process in-app messages, you can add an observer on `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Step 2: Access triggered messages

Then within your handler, you have access to the highest in-app message that your campaigns have triggered:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Message fields

### Handling

The following lists the fields you will need to handle your in-app messages:

| Fields | Description |
| ------ | ----------- |
| `buttons` | List of buttons (could be an empty list). |
| `click_action` | `"URI"` or `"NONE"`. Use this field to indicate whether the in-app message should open to a URI link or close the message when clicked. When there are no buttons, this should happen when the user clicks "OK" when the in-app message is displayed. |
| `dismiss_type` | `"AUTO_DISMISS"` or `"SWIPE"`. Use this field to indicate whether your in-app message will auto dismiss or require a swipe to dismiss. |
| `display_delay` | How long (seconds) to wait until displaying the in-app message. |
| `duration` | How long (milliseconds) the message should be displayed when `dismiss_type` is set to `"AUTO_DISMISS"`. |
| `extras` | Key-value pairs. |
| `header` | The header text. |
| `id` | The ID used to log impressions or clicks. |
| `image_url` | In-app message image URL. |
| `message` | Message body text. |
| `uri` | Your URI users will be sent to based on your `click_action`. This field must be included when `click_action` is `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
For in-app messages containing buttons, the message `click_action` will also be included in the final payload if the click action is added prior to adding the button text.
{% endalert %}

### Styling

There are also various styling fields that you could choose to use from the dashboard:

| Fields | Description |
| ------ | ----------- |
| `bg_color` | Background color. |
| `close_button_color` | Close button color. |
| `frame_color` | The color of the background screen overlay. |
| `header_text_color` | Header text color. |
| `message_text_color` | Message text color. |
| `text_align` | "START", "CENTER", or "END". Your selected text alignment. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Alternatively, you could implement the in-app message and style it within your Roku application using a standard palette:

### Buttons

| Fields | Description |
| ------ | ----------- |
| `click_action` | `"URI"` or `"NONE"`. Use this field to indicate whether the in-app message should open to a URI link or close the message when clicked. |
| `id` | The ID value of the button itself. |
| `text` | The text to display on the button. |
| `uri` | Your URI users will be sent to based on your `click_action`. This field must be included when `click_action` is `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Handling analytics

You will need to make sure certain functions are called to handle the analytics for your campaign.

### For displayed messages

When a message is displayed or seen, log an impression:

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### For clicked messages

Once a user clicks on the message, log a click and then process `in_app_message.click_action`:

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### For clicked buttons

If the user clicks on a button, log the button click and then process `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### After processing a message

After processing an in-app message, you should clear the field:

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```

## Sending a Roku message

Create an in-app message for Roku by selecting **Roku Devices** as the in-app message platform.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})
