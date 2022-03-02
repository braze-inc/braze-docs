---
nav_title: Integration
article_title: In-App Message Integration Guide for Roku
platform: Roku
page_order: 2
description: "This Integration guide covers Roku in-app message code considerations"
channel:
  - in-app messages
---

# In-app messaging implementation guide

This implementation guide covers in-app message code considerations and accompanying code snippets. While we provide a sample out-of-the-box implementation, you will need to build a container for your payload and most likely implement custom code for your desired UI. Because your code will be unique to your app, you do not need to handle all situations listed below if not relevant to your use case. For example, if you don't use delayed display of in-app messages, you will not need to implement that logic and edge cases.

## SDK requirements {#supported-sdk-versions}

In-app messages will only be sent to Roku devices running the minimum supported SDK version:

{% sdk_min_versions roku:0.1.0 %}

## In-app message setup

To process in-app messages, you can add an observer on `BrazeTask.BrazeInAppMessage`:

```
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Then within your handler, you have access to the highest in-app message that your campaigns have triggered:

```
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## In-app message fields

Listed below are the fields you will need to handle your in-app messages:

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
{: .reset-td-br-1 .reset-td-br-2}

### Styling fields
There are also various styling fields that you could choose to use from the dashboard:

| Fields | Description |
| ------ | ----------- |
| `bg_color` | Background color. |
| `close_button_color` | Close button color. |
| `frame_color` | The color of the background screen overlay. |
| `header_text_color` | Header text color. |
| `message_text_color` | Message text color. |
| `text_align` | "START", "CENTER", or "END". Your selected text alignment. |
{: .reset-td-br-1 .reset-td-br-2}

Alternatively, you could implement the in-app message and style it within your Roku application using a standard palette:

### Button fields

| Fields | Description |
| ------ | ----------- |
| `click_action` | `"URI"` or `"NONE"`. Use this field to indicate whether the in-app message should open to a URI link or close the message when clicked. |
| `id` | The ID value of the button itself. |
| `text` | The text to display on the button. |
| `uri` | Your URI users will be sent to based on your `click_action`. This field must be included when `click_action` is `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2}

## Handling interactions

You will need to make sure certain functions are called to handle the analytics for your campaign.

##### When a message is displayed

When a message is displayed or seen, log an impression:
```
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### When a user clicks on a message
Once a user clicks on the message, log a click and then process `in_app_message.click_action`:
```
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### When a user clicks a button
If the user clicks on a button, log the button click and then process `inappmessage.buttons[selected].click_action`:

```
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### After processing an in-app message
After processing an in-app message, you should clear the field:
```
m.BrazeTask.BrazeInAppMessage = invalid
```
