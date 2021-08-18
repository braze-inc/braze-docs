---
nav_title: Dark Mode Themes
article_title: Dark Mode for In-App Messages
page_order: 5.20
description: "Braze in-app messages support adding an alternate Dark theme to help deliver the right color message to your users based on their preference, and helps provide consistency with your app's design."
channel:
  - in-app messages

---

# Dark Mode for In-App Messages

Dark Mode offers users the opportunity to set a system-wide color preference (introduced on [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) and [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). The "Dark" themes are intended to conserve battery life, and reduce strain on users' eyes, while providing app developers an easier way to implement the dark color themes that users prefer.

Braze in-app messages support adding an alternate Dark theme to help deliver the right color message to your users based on their preference, and helps provide consistency with your app's design.

## How Dark Mode Works

Users with the latest versions of Android (10+) and iOS (13+) can toggle Dark Mode on or off in their device's settings.

When Dark Mode is enabled, the device's native menus and screens (push notifications, device settings, etc.) will change to a dark grey. Apps can also choose to support dark mode by specifying the alternate themes in the app's code.

## Setting a Dark Mode Theme

The new Dark Mode option, located in the Style tab when [creating an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), lets you easily add an alternate color theme for users who are in Dark Mode on their device.

<img src="{% image_buster /assets/img_archive/iam-dark-mode.gif %}" style="width:100%;max-width:800px;" />

When this option is enabled, you can choose dark theme colors for your in-app message using the color picker, or by selecting existing [Color Profiles][2] to re-use existing Dark or Light themes.

{% alert note %}
You may still use this feature even if your app does not offer its own dark theme. However, devices which do not support Dark Mode will display the _Light_ theme by default.
{% endalert %}

### Using Dark Mode Consistently

To use Dark Mode for all in-app messages, go to Templates & Media, then In-App Message Templates. From there, select [`Create Color Profile`][2] from the dropdown. Create a Color Profile that aligns with your Dark Mode theme. Then, anytime you create a Dark Mode version of an in-app message, you can select that Color Profile and keep the look of your in-app messages consistent.

## Compatibility
- End users must be on iOS devices version 13 or higher, or Android devices version 10 or higher.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ is required.

{% alert info %}
Dark Mode apps were introduced with Android 10 and iOS 13. Users who have not upgraded their phones to at least these versions will only be shown the light theme.

Campaigns will still be served to all users who are eligible for the audience you have selected, regardless of users' Dark Mode setting or OS version.
{% endalert %}

## Using HTML In-App Messages

To create a Dark and Light theme for HTML In-App Messages, you can use the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS media feature to detect the user's preference.

For example:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile
