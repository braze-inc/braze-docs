---
nav_title: "Apple Object"
article_title: Apple Messaging Object
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "This article lists and explains the different Apple objects used at Braze."

---

# Apple Push Object Specification

These objects are used to define or request information related to Apple Push and Apple Push Alert content.

## Apple Push Object

```json
{
   "badge": (optional, int) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device once you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple Push Action Button Objects) push action buttons to display
}
```

You must include an Apple Push Object in `messages` if you want users you have targeted to receive a push on their iOS Devices. The total number of bytes in your `alert` string, `extra` object and other optional parameters should not exceed 1912. The Messaging API will return an error if you exceed the message size allowed by Apple. Messages that include the keys `ab` or `aps` in the `extra` object will be rejected.

### Apple Push Alert Object

In most cases, `alert` can be specified as a string in an `apple_push` object.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button’s title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key
}
```

## Apple Push Action Button Object

You _must_ include the `category` field in the Apple Push Object to use iOS push action buttons. Including the `category` field will display any associated push action buttons; only include the `buttons` field if you want to additionally define the buttons' individual click actions. The Braze SDK provides a set of default push action buttons for you to use (see the table below). You can also use your own buttons if they have been registered in your app.

### Apple Push Action Button Object for Braze Default Buttons

| Category Identifier   | Button Text | Button Action Identifier | Allowed Actions         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Accept      | `ab_pb_accept`             | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_accept_decline` | Decline     | `ab_pb_decline`            | CLOSE                   |
| `ab_cat_yes_no`         | Yes         | `ab_pb_yes`                | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_yes_no`         | No          | `ab_pb_no`                 | CLOSE                   |
| `ab_cat_confirm_cancel` | Confirm     | `ab_pb_confirm`            | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_confirm_cancel` | Cancel      | `ab_pb_cancel`             | CLOSE                   |
| `ab_cat_more`           | More        | `ab_pb_more`               | OPEN_APP, URI, or DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Apple Push Action Button Object for Categories Defined by Your App

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```
