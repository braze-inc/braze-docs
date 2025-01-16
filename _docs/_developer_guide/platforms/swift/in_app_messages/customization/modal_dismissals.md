---
nav_title: Modal Dismissal
article_title: Custom modal dismissals for the Braze Swift SDK
platform: Swift
description: "This reference article covers in-app messaging modal dismissal for the Swift SDK."
channel:
  - in-app messages
---

# Custom modal dismissals

> Learn how to customize the modal dismissals for in-app messages for the Braze Swift SDK.

## Customizing modal dismissals

To enable outside tap dismissals, you can modify the `dismissOnBackgroundTap` property on the `Attributes` struct of the in-app message type you wish to customize. 

For example, if you wish to enable this feature for modal image in-app messages, you can configure the following:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

Customization via `Attributes` is not available in Objective-C.

{% endtab %}
{% endtabs %}

The default value is `false`. This determines if the modal in-app message will be dismissed when the user taps outside of the in-app message.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `true`         | Modal in-app messages will be dismissed on outside tap.     |
| `false`        | Default, modal in-app messages will not be dismissed on outside tap. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details on in-app message customization, refer to this [article](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).
