---
nav_title: Custom on-click behavior
article_title: Customizing In-App Message On-Click Behavior for iOS
platform: iOS
page_order: 5
description: "This reference article covers custom in-app messaging on-click behavior for your iOS application."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Customizing in-app message behavior on click

The `inAppMessageClickActionType` property on the `ABKInAppMessage` defines the action behavior after the in-app message is clicked. This property is read-only. If you want to change the in-app message's click behavior, you can call the following method on `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

The `inAppMessageClickActionType` can be set to one of the following values:

| `ABKInAppMessageClickActionType` | On-Click Behavior |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | The given URI will be displayed when the message is clicked, and the message will be dismissed. Note that the `uri` parameter cannot be nil. |
| `ABKInAppMessageNoneClickAction` | The message will be dismissed when clicked. Note that the `uri` parameter will be ignored, and the `uri` property on the `ABKInAppMessage` will be set to nil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
For in-app messages containing buttons, the message `clickAction` will also be included in the final payload if the click action is added prior to adding the button text.
{% endalert %}

## Customizing in-app message body clicks

The following [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) delegate method is called when an in-app message is clicked:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Customizing in-app message button clicks

For clicks on in-app message buttons and HTML in-app message buttons (such as links), [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) includes the following delegate methods:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Each method returns a `BOOL` value to indicate if Braze should continue to execute the click action.

To access the click action type of a button in a delegate method, you can use the following code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

When an in-app message has buttons, the only click actions that will be executed are those on the `ABKInAppMessageButton` model. The in-app message body will not be clickable even though the `ABKInAppMessage` model will have the default click action assigned.

## Method declarations

For additional information, see the following header files:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

