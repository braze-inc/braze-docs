---
nav_title: Dark Mode Themes
article_title: Dark Mode for In-App Messages
page_order: 5.20
description: "Braze in-app messages support adding an alternate Dark theme to help deliver the right color message to your users based on their preference, and helps provide consistency with your app's design."
channel:
  - in-app messages

---

# Dark Mode for in-app messages

Dark Mode offers users the opportunity to set a system-wide color preference (introduced on [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) and [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). The "Dark" themes are intended to conserve battery life, and reduce strain on users' eyes, while providing app developers an easier way to implement the dark color themes that users prefer.

Braze in-app messages support adding an alternate Dark theme to help deliver the right color message to your users based on their preference, and helps provide consistency with your app's design.

## How Dark Mode works

Users with versions of at least Android 10 or iOS 13 and later can toggle Dark Mode on or off in their device's settings.

When Dark Mode is enabled, the device's native menus and screens (push notifications, device settings, etc.) will change to a dark grey. Apps can also choose to support dark mode by specifying the alternate themes in the app's code.

## Setting a Dark Mode theme

The new Dark Mode option, located in the Style tab when [creating an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), lets you easily add an alternate color theme for users who are in Dark Mode on their device.

![User switching between Light Mode style and Dark Mode styles in the Style tab when creating an in-app message.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

When this option is enabled, you can choose dark theme colors for your in-app message using the color picker, or by selecting existing [Color Profiles][2] to re-use existing Dark or Light themes.

{% alert note %}
You may still use this feature even if your app does not offer its own dark theme. However, devices which do not support Dark Mode will display the Light theme by default. Changing the devices theme on Android while an in-app message is being displayed won't change which theme is used for that in-app message.
{% endalert %}

### Using Dark Mode consistently

To use Dark Mode for all in-app messages, go to **Templates & Media**, then **In-app Message Templates**. From there, select [Create Color Profile][2] from the dropdown. Create a Color Profile that aligns with your Dark Mode theme. Then, anytime you create a Dark Mode version of an in-app message, you can select that Color Profile and keep the look of your in-app messages consistent.

## Compatibility

- End users must be on iOS devices version 13 or higher, or Android devices version 10 or higher.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ is required.

{% alert note %}
Dark Mode apps were introduced with Android 10 and iOS 13. Users who have not upgraded their phones to at least these versions will only be shown the light theme. <br><br>Campaigns will still be served to all users who are eligible for the audience you have selected, regardless of users' Dark Mode setting or OS version.
{% endalert %}

## Using HTML in-app messages

To create a Dark and Light theme for HTML in-app messages, you can use the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS media feature to detect the user's preference.

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
