## Subscribing to in-app messages

You may register Unity game objects to be notified of incoming in-app messages. We recommend setting game object listeners from the Braze configuration editor. In the configuration editor, listeners must be set separately for Android and iOS.

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Parsing messages

Incoming `string` messages received in your in-app message game object callback can be parsed into our pre-supplied model objects for convenience.

Use `InAppMessageFactory.BuildInAppMessage()` to parse your in-app message. The resulting object will either be an instance of [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) or [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) depending on its type.

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

## Logging message data

Clicks and impressions must be manually logged for in-app messages not displayed directly by Braze.

Use `LogClicked()` and `LogImpression()` on [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) to log clicks and impressions on your message.

Use `LogButtonClicked(int buttonID)` on [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) to log button clicks. Note that buttons are represented as lists of[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) instances, each of which contains a `ButtonID`.
