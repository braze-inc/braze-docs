## About user IDs for Swift

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Setting a user ID

You should make the following call as soon as the user is identified (generally after logging in) to set the user ID:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**Do not call `changeUser()` when a user logs out. `changeUser()` should only be called when the user logs into the application.** Setting [`changeUser()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29) to a static default value will associate ALL user activity with that default "user" until the user logs in again.
{% endalert %}

Additionally, we recommend against changing the user ID when a user logs out, as it makes you unable to target the previously logged-in user with re-engagement campaigns. If you anticipate multiple users on the same device but only want to target one of them when your app is in a logged-out state, we recommend separately keeping track of the user ID you want to target while logged out and switching back to that user ID as part of your app's logout process.

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing users

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Swift" %}

