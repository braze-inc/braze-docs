{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Message types

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Enabling in-app messages

The Braze Flutter SDK automatically sets up the default in-app message presenter on both Android and iOS. In-app messages are displayed and forwarded to the Dart layer without additional setup.

### Customizing the in-app message presenter on iOS

To override the default in-app message presenter on iOS, use the `postInitialization` closure in `BrazePlugin.configure(_:postInitialization:)`. Your custom presenter must call `BrazePlugin.processInAppMessage(message)` to forward in-app message data to the Dart layer.

```swift
import BrazeUI

BrazePlugin.configure(
  { configuration in
    // Set non-API-key configurations here.
  },
  postInitialization: { braze in
    let customPresenter = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = customPresenter
  }
)
```

In the custom presenter class, call `BrazePlugin.processInAppMessage(message)` and `super.present(message: message)` to forward data to Dart and display the default UI.

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    BrazePlugin.processInAppMessage(message)
    super.present(message: message)
  }
}
```

For more information about accessing in-app message data, refer to [Logging in-app message data]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
