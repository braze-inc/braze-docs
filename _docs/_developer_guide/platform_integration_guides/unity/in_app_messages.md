---
nav_title: In-App Messages
article_title: In-App Messages for the Braze Unity SDK
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "This reference article covers in-app messaging configuration guidelines for the Unity platform."
---

# In-app messages

> This reference article covers in-app messaging configuration guidelines for the Unity platform.

{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuring default in-app message behavior

{% tabs %}
{% tab Android %}

On Android, in-app messages from Braze are automatically displayed natively. To disable this functionality, deselect **Automatically Display In-App Messages** in the Braze configuration editor.

You may alternatively set `com_braze_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `braze.xml`.

The initial in-app message display operation can be set in Braze config via the "In App Message Manager Initial Display Operation".

{% endtab %}
{% tab iOS %}

On iOS, in-app messages from Braze are automatically displayed natively. To disable this functionality, set game object listeners in the Braze configuration editor and ensure **Braze Displays In-App Messages** is not selected.

The initial in-app message display operation can be set in Braze config via the "In App Message Manager Initial Display Operation".

{% endtab %}
{% endtabs %}

## Configuring in-app message display behavior

You may optionally change the display behavior of in-app messages at runtime via the following:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Displaying in-app messages on demand

You may display the next available in-app message in the stack via the `DisplayNextInAppMessage()` method. Messages are added to this stack of saved messages if `DISPLAY_LATER` or `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` is chosen as the in-app message display action.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Receiving in-app message data in Unity

You may register Unity game objects to be notified of incoming in-app messages. We recommend setting game object listeners from the Braze configuration editor. In the configuration editor, listeners must be set separately for Android and iOS.

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Parsing in-app messages

Incoming `string` messages received in your in-app message game object callback can be parsed into our pre-supplied model objects for convenience.

Use `InAppMessageFactory.BuildInAppMessage()` to parse your in-app message. The resulting object will either be an instance of [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) or [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) depending on its type.

### Example in-app message callback

```csharp
// Automatically logs a button click, if present.
void InAppMessageReceivedCallback(string message) {
  IInAppMessage inApp = InAppMessageFactory.BuildInAppMessage(message);
  if (inApp is IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    if (inAppImmersive.Buttons != null && inAppImmersive.Buttons.Count > 0) {
      inAppImmersive.LogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

## GIF Support

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Analytics

Clicks and impressions must be manually logged for in-app messages not displayed directly by Braze.

Use `LogClicked()` and `LogImpression()` on [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) to log clicks and impressions on your message.

Use `LogButtonClicked(int buttonID)` on [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) to log button clicks. Note that buttons are represented as lists of[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) instances, each of which contains a `ButtonID`.

## Custom action listeners

If you require more control over how a user interacts with in-app messages, use a `BrazeInAppMessageListener` and assign it to `Appboy.AppboyBinding.inAppMessageListener`. For any delegates you don't want to use, you can simply leave them as `null`.

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

