---
nav_title: Implementation
article_title: In-App Message Implementation Guide for Roku
platform: Roku
page_order: 2
description: "This implementation guide covers Roku in-app message code considerations"
channel:
  - in-app messages
---

# In-app messaging implementation guide

 This implementation guide covers in-app message code considerations and accompanying code snippets.  While we provide a a sample implementation, you will probably need to implement custom code. Since your code will be unique to your app, so you don't need to handle all situations if you don't plan on using them.  For example, if you don't use delayed display of in-app messages, you don't need to implement that logic and edge cases.

### In-App Message Setup

To process in-app messages, you can add an observer on BrazeTask.BrazeInAppMessage:

```
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Then within your handler, you have access to the highest in-app message that has been triggered by your campaigns:

```
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## In-App Message fields
Here are the fields you'll need to handle the in-app message:

| `buttons` | List of buttons (could be an empty list) |
| `click_action` | When there are no buttons, this is what should happen when the user clicks "OK" when the IAM is displayed. Can be "URI" or "NONE" |
| `dismiss_type` | Can be "AUTO_DISMISS" or "SWIPE" |
| `display_delay` | How long (in seconds) to wait until displaying the in-app message |
| `duration` | How long (in milliseconds), the message should be displayed when dismiss_type is "AUTO_DISMISS" |
| `extras` | Key/value pairs |
| `header` | The header text of the in-app message |
| `id` | ID to use when logging impressions or clicks |
| `image_url` | Image URL |
| `message` | The body text of the in-app message |
| `uri` | When click_action is "URI", this should be displayed |
{: .reset-td-br-1 .reset-td-br-2}

# Styling fields
There are also various styling fields that you could choose to use from the dashboard.  Alternatively, you could implement the In-App Message and style it within your Roku application using a standard palette:

| `bg_color` | Background color |
| `close_button_color` | Close button color |
| `frame_color` | The color of the background screen overlay |
| `header_text_color` | Header text color |
| `message_text_color` | Message text color |
| `text_align` | Can be "START", "CENTER", or "END" |
{: .reset-td-br-1 .reset-td-br-2}

# Button fields
These are the fields on buttons:

| `click_action` | Can be "URI" to indicate to open the uri field. Can be "NONE" to indicate this button should close the in-app message |
| `id` | The ID value of the button itself |
| `text` | The text to display on the button |
| `uri` | When click_action is "URI", this should be displayed |
{: .reset-td-br-1 .reset-td-br-2}

### Handling interactions

You will need to make sure certain functions are called to handle the analytics for your campaign.<br />

When a message is displayed or seen, log an impression:
```
LogInAppMessageImpression(in_app_message.id, brazetask)
```

Once a user clicks on the message, log a click:
```
LogInAppMessageClick(in_app_message.id, brazetask)
```
and then process in_app_message.click_action

If the user clicks on a button, log the button click:
```
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
and then process inappmessage.buttons[selected].click_action

After processing in-app message, you should clear the field:
```
m.BrazeTask.BrazeInAppMessage = invalid
```
