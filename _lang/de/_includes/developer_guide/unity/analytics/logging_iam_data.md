## In-App-Nachrichten abonnieren

Sie können Unity Spielobjekte registrieren, um über eingehende In-App-Nachrichten benachrichtigt zu werden. Wir empfehlen Ihnen, Spielobjekt-Listener über den Braze-Konfigurationseditor einzustellen. Im Konfigurationseditor müssen die Hörer für Android und iOS getrennt eingestellt werden.

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.IN_APP_MESSAGE` an.

## Parsing von Nachrichten

Eingehende `string` Nachrichten, die in Ihrem In-App-Nachricht Spielobjekt Callback empfangen werden, können der Einfachheit halber in unsere vorgefertigten Modellobjekte geparst werden.

Verwenden Sie `InAppMessageFactory.BuildInAppMessage()`, um Ihre In-App-Nachricht zu analysieren. Das resultierende Objekt ist entweder eine Instanz von [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) oder [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) abhängig von seinem Typ.

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

## Protokollierung von Nachrichten-Daten

Klicks und Impressionen müssen für In-App-Nachrichten, die nicht direkt von Braze angezeigt werden, manuell protokolliert werden.

Verwenden Sie `LogClicked()` und `LogImpression()` auf [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs), um Klicks und Impressionen auf die Nachricht zu protokollieren.

Verwenden Sie `LogButtonClicked(int buttonID)` auf [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs), um Klicks auf Buttons zu protokollieren. Beachten Sie, dass die Buttons als Listen von [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs)-Instanzen dargestellt werden, von denen jede eine `ButtonID` enthält.
