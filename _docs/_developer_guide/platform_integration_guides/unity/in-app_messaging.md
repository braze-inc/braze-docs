---
nav_title: In-App Messaging
platform: Unity
page_order: 2
---
# In-App Messaging

## In-App Message Types
There are four types of in-app messages: slideup, modal, full, and custom HTML. All in-app messages implement [`Appboy.Models.IInAppMessage.cs`][13], and modal and full in-app messages additionally implement [`Appboy.Models.IInAppMessageImmersive.cs`][12]. These interfaces provide ways in which you can interact with or customize Braze's in-app messages.

For more information, see [`Appboy.Models.InAppMessageBase`][6] and [`Appboy.Models.InAppMessageImmersiveBase`][11].

## Customization
Custom in-app messages can be handled in Unity via Braze's [InAppMessage models][1].

### Logging Clicks and Impressions

#### In-App Message Body

Clicks and impressions must be manually logged for in-app messages handled in Unity. You can use the `LogClicked()` and `LogImpression()` methods defined in [`Appboy.Models.IInAppMessage`][13].

#### In-App Message Buttons

Button clicks can be logged by calling the `LogButtonClicked(buttonID(int))` method in [`Appboy.Models.IInAppMessageImmersive`][12]. The `ButtonID` can be retrieved from [`Appboy.Models.InAppMessageButton`][8].

For more information, refer to [`Appboy.Models.InAppMessageImmersiveBase`][11].

### Customizing Display Behavior

#### Dismissal Behavior

You can customize in-app message dismissal behavior by setting the in-app message's `InAppDismissType` property to either `DismissType.AUTO_DISMISS` or `DismissType.SWIPE`.

For more information, see [`Appboy.Models.InAppMessage.IInAppMessage`][13] and [`Appboy.Models.DismissType`][5].

#### Slideup Behavior

For slideup in-app messages, you can set in-app messages to slide from the top or bottom by setting the in-app message's `SlideupAnchor` property to `SlideFrom.TOP` or `SlideFrom.BOTTOM`.

For more information, see [`Appboy.Models.InAppMessage.InAppMessageSlideup`][4] and [`Appboy.Models.SlideFrom`][3].

### Customizing Click Behavior

#### In-App Messages

To set the in-app click action, you can call `SetInAppClickAction()` and pass in `ClickAction.NEWS_FEED` or `ClickAction.NONE`, which will redirect to the News Feed or do nothing, respectively.

Alternatively, you can set the click action to redirect to a URI by calling

```csharp
SetInAppClickAction(ClickAction.URI, "https://www.braze.com");
```

For more information, see [`Appboy.Models.InAppMessage.IInAppMessage`][13] and [`Appboy.Models.ClickAction`][9].

#### In-App Message Buttons

You can also set the click action on an in-app message button via the `SetButtonClickAction()` methods on [`Appboy.Models.InAppMessageButton`][8]:

```csharp
SetButtonClickAction(ClickAction.NEWS_FEED);

SetButtonClickAction(ClickAction.URI, "https://www.braze.com");
```

### Customizing Appearance
Custom in-app messages should be handled in Unity, using [Braze's in-app message models][1].

### Sample Code
For sample implementation code, refer to the `InAppMessageReceivedCallback()` method in [BrazeBindingTester.cs][2].

[1]: https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Appboy/models/InAppMessage
[2]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Tests/AppboyBindingTester.cs
[3]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/SlideFrom.cs
[4]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/InAppMessageSlideup.cs
[5]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/DismissType.cs
[6]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/InAppMessageBase.cs
[8]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/InAppMessageButton.cs
[9]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/ClickAction.cs
[11]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/InAppMessageImmersiveBase.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessageImmersive.cs
[13]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessage.cs
