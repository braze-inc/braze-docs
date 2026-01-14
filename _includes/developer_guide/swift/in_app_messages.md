{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to enable in-app messages.

## Message types

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Enabling in-app messages

### Step 1: Create an implementation of `BrazeInAppMessagePresenter`

To let Braze display in-app messages, create an implementation of the `BrazeInAppMessagePresenter` protocol and assign it to the optional `inAppMessagePresenter` on your Braze instance. You can also use the default Braze UI presenter by instantiating a `BrazeInAppMessageUI` object.

Note that you will need to import the `BrazeUI` library to access the `BrazeInAppMessageUI` class.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### Step 2: Handle no matching triggers

Implement [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) within the relevant `BrazeDelegate` class. When Braze fails to find a matching trigger for a particular event, it will call this method automatically.
