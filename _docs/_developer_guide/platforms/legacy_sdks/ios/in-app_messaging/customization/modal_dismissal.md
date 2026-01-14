---
nav_title: Modal dismissal
article_title: In-App Message Modal Dismissal for iOS
platform: iOS
page_order: 29
description: "This reference article covers in-app messaging modal dismissal for your iOS application."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Dismiss modal on outside tap

The default value is `NO`. This determines if the modal in-app message will be dismissed when the user taps outside of the in-app message.

To enable outside tap dismissals, add a dictionary named `Braze` to your `Info.plist` file. Inside the `Braze` dictionary, add the `DismissModalOnOutsideTap` boolean subentry and set the value to `YES`, as shown in the following code snippet. Note that prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

You can also enable the feature at runtime by setting `ABKEnableDismissModalOnOutsideTapKey` to `YES` in `appboyOptions`.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `YES`       | Modal in-app messages will be dismissed on outside tap.     |
| `NO`        | Default, modal in-app messages will not be dismissed on outside tap. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }