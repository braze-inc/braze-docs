---
nav_title: In-App-Messaging
article_title: In-App Messaging für Unity
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Dieser Artikel beschreibt die Konfigurationsrichtlinien für In-App-Nachrichten auf der Unity-Plattform."

---

# Integration von In-App-Nachrichten

> Dieser Artikel beschreibt die Konfigurationsrichtlinien für In-App-Nachrichten auf der Unity-Plattform.

## Standard-Verhalten bei In-App-Nachrichten konfigurieren

{% tabs %}
{% tab Android %}

Auf Android werden In-App-Nachrichten von Braze automatisch und nativ angezeigt. Um diese Funktion zu deaktivieren, deaktivieren Sie die Option **In-App-Nachrichten automatisch anzeigen** im Braze Konfigurationseditor.

Sie können alternativ `com_braze_inapp_show_inapp_messages_automatically` auf `false` in Ihrem Unity-Projekt `braze.xml` setzen.

Die anfängliche Anzeige der In-App-Nachricht kann in der Braze-Konfiguration über die Option "In-App Message Manager Initial Display Operation" eingestellt werden.

{% endtab %}
{% tab iOS %}

Auf iOS werden In-App-Nachrichten von Braze automatisch und nativ angezeigt. Um diese Funktion zu deaktivieren, stellen Sie im Braze-Konfigurationseditor Spielobjekt-Listener ein und stellen Sie sicher, dass **Braze zeigt In-App-Nachrichten** nicht ausgewählt ist.

Die anfängliche Anzeige der In-App-Nachricht kann in der Braze-Konfiguration über die Option "In-App Message Manager Initial Display Operation" eingestellt werden.

{% endtab %}
{% endtabs %}

## Konfigurieren der Anzeige von In-App-Nachrichten

Sie können das Anzeigeverhalten von In-App-Nachrichten zur Laufzeit optional über Folgendes ändern:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## On-Demand-Anzeige von In-App-Nachrichten

Sie können die nächste verfügbare In-App-Nachricht im Stack über die Methode `DisplayNextInAppMessage()` anzeigen. Diesem Stapel gespeicherter Nachrichten werden Nachrichten hinzugefügt, wenn `DISPLAY_LATER` oder `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` als Aktion zur Anzeige von In-App-Nachrichten gewählt wurde.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Empfang von In-App-Nachricht-Daten in Unity

Sie können Unity Spielobjekte registrieren, um über eingehende In-App-Nachrichten benachrichtigt zu werden. Wir empfehlen Ihnen, Spielobjekt-Listener über den Braze-Konfigurationseditor einzustellen. Im Konfigurationseditor müssen die Hörer für Android und iOS getrennt eingestellt werden.

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.IN_APP_MESSAGE` an.

## Parsen von In-App-Nachrichten

Eingehende `string` Nachrichten, die in Ihrem In-App-Nachricht Spielobjekt Callback empfangen werden, können der Einfachheit halber in unsere vorgefertigten Modellobjekte geparst werden.

Verwenden Sie `InAppMessageFactory.BuildInAppMessage()`, um Ihre In-App-Nachricht zu analysieren. Das resultierende Objekt ist entweder eine Instanz von [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) oder [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) abhängig von seinem Typ.

### Beispiel-Callback für In-App-Nachricht

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

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Analytics

Klicks und Impressionen müssen für In-App-Nachrichten, die nicht direkt von Braze angezeigt werden, manuell protokolliert werden.

Verwenden Sie `LogClicked()` und `LogImpression()` auf [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs), um Klicks und Impressionen auf die Nachricht zu protokollieren.

Verwenden Sie `LogButtonClicked(int buttonID)` auf [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs), um Klicks auf Buttons zu protokollieren. Beachten Sie, dass die Buttons als Listen von [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs)-Instanzen dargestellt werden, von denen jede eine `ButtonID` enthält.

## Angepasste Action Listener

Wenn Sie mehr Kontrolle darüber benötigen, wie Nutzer mit In-App-Nachrichten interagieren, verwenden Sie einen `BrazeInAppMessageListener` und weisen Sie ihn dem `Appboy.AppboyBinding.inAppMessageListener` zu. Delegaten, die Sie nicht verwenden möchten, können Sie einfach auf `null` gesetzt lassen.

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

