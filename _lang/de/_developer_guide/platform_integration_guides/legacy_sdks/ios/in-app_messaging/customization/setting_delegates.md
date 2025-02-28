---
nav_title: Delegaten festlegen
article_title: In-App-Nachricht Delegierte für iOS einstellen
platform: iOS
page_order: 2
description: "Dieser Artikel referenziert die Einstellung von In-App-Nachrichtendelegierten für Ihre iOS-Anwendung."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Delegierte einstellen

Die Anzeige und Zustellung von In-App-Nachrichten kann im Code angepasst werden, indem Sie unsere optionalen Delegaten festlegen.

## In-App-Nachricht-Delegat

Der [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)-Delegat kann verwendet werden, um getriggerte In-App-Nachrichten zur weiteren Verarbeitung zu empfangen, Ereignisse im Lebenszyklus der Anzeige zu empfangen und die Anzeigezeit zu steuern. 

Setzen Sie Ihr `ABKInAppMessageUIDelegate`-Delegatenobjekt auf die Braze-Instanz, indem Sie Folgendes aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

In unserer [Beispiel-App](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) für In-App-Nachrichten sehen Sie ein Beispiel für die Implementierung. Beachten Sie, dass dieser Delegat nicht verfügbar ist, wenn Sie die Braze-UI-Bibliothek nicht in Ihr Projekt einbinden (ungewöhnlich).

## Hauptdelegat für In-App-Nachricht

Wenn Sie die Braze-UI-Bibliothek nicht in Ihr Projekt einbinden und getriggerte In-App-Nachricht-Payloads zur Weiterverarbeitung oder angepassten Anzeige in Ihrer App empfangen möchten, implementieren Sie das Protokoll [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/).

Setzen Sie Ihr `ABKInAppMessageControllerDelegate`-Delegatenobjekt auf die Braze-Instanz, indem Sie Folgendes aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Sie können alternativ Ihren zentralen In-App-Nachricht-Delegaten zur Initialisierungszeit über `appboyOptions` mit dem Schlüssel `ABKInAppMessageControllerDelegateKey` festlegen:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Methoden-Deklarationen

Weitere Informationen finden Sie in den folgenden Header-Dateien:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Beispiele für die Umsetzung

Siehe [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) in der Beispiel App für In-App-Nachrichten.


