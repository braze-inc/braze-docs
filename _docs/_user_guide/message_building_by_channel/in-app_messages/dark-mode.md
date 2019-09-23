---
nav_title: Dark Mode Themes
page_order: 5.20
hidden: true
---

{% alert note %}
This feature is currently in Early Access. Please speak to your Braze Success team for access or to provide any feedback.
{% endalert %}

# Dark Mode for In App Messages

Dark Mode introduces a new way for users to set a system-wide color preference on Android 10 and iOS 13. The "Dark" themes are intended to conserve battery life, and reduce strain on users' eyes, while providing app developers an easier way to implement the dark color themes that users prefer.

Braze In App Messages now support adding an alternate Dark theme to help deliver the right color message to your users based on their preference, and helps provide consistency with your app's design.

## How Dark Mode Works

Users with the latest versions of Android (10+) and iOS (13+) can toggle Dark Mode on or off in their phone's settings.

When Dark Mode is enabled, the phone's native menus and screens (push notifications, phone settings, etc.) will change to a dark grey. Apps can also choose to support dark mode by specifying the alternate themes in the app's code.

## Setting Dark Theme for App Messages

The new Dark Mode option located in the Style tab of In App Messages lets you easily add an alternate color theme for users who are in Dark Mode.

<img src="{% image_buster /assets/img_archive/iam-dark-mode.gif %}" style="width:100%;max-width:800px;" />

When this option is enabled, you can choose dark theme colors for your In App Message using the color picker, or by selecting existing [Color Profiles][2] to re-use existing Dark or Light themes.

{% alert note %}
You may still use this feature even if your app does not offer its own dark theme. However, devices which do not support Dark Mode will display the _light_ theme by default.
{% endalert %}

## Compatibility

- End users must be on iOS devices version 13 or higher, or Android devices version 10 or higher

- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ is required

## Using HTML In App Messages

To create a Dark and Light theme for HTML In App Messages, you can use the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS media feature to detect the user's preference.

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

[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/in_app_message_color_templates/#in-app-message-color-templates
