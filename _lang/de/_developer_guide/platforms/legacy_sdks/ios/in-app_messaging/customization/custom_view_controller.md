---
nav_title: Benutzerdefinierter View Controller
article_title: In-App Nachricht in einem benutzerdefinierten View Controller für iOS
platform: iOS
page_order: 7
description: "Dieser Referenzartikel beschreibt, wie Sie einen angepassten View Controller für In-App-Messaging für Ihre iOS-Anwendung nutzen können."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Anzeigen von In-App-Nachrichten in einem benutzerdefinierten View-Controller

In-App-Nachrichten können auch in einem angepassten View-Controller angezeigt werden, den Sie an Braze übergeben. Braze animiert die angepasste In-App-Nachricht und verarbeitet die Analytics der In-App-Nachricht. Der View Controller muss die folgenden Anforderungen erfüllen:

- Es muss eine Unterklasse oder eine Instanz von `ABKInAppMessageViewController` sein.
- Die Ansicht des zurückgegebenen View-Controllers sollte eine Instanz von `ABKInAppMessageView` oder seiner Unterklasse sein.

Die folgende UI-Delegate-Methode wird jedes Mal aufgerufen, wenn eine In-App-Nachricht auf `ABKInAppMessageViewController` angeboten wird, damit die App einen angepassten View-Controller für die Anzeige von In-App-Nachrichten an Braze übergeben kann:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab schnell %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Unsere [Controller für die In-App-Nachrichtenansicht](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) sind anpassbar. Sie können Unterklassen oder Kategorien verwenden, um die Anzeige oder das Verhalten von In-App-Nachrichten anzupassen.

## Methoden-Deklarationen

Weitere Informationen finden Sie in den folgenden Header-Dateien:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## Beispiele für die Umsetzung

Siehe [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) und [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/) in der Beispiel-App für In-App-Nachrichten.

