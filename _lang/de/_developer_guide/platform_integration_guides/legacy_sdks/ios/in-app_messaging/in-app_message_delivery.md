---
nav_title: Zustellung von In-App-Nachrichten
article_title: In-App Nachrichtenzustellung für iOS
platform: iOS
page_order: 3
description: "Dieser Referenzartikel beschreibt die Zustellung von iOS-In-App-Nachrichten. Außerdem behandelt er verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Auslösung von Events."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Zustellung von In-App-Nachrichten

## Auslöser-Typen

Mit unserem Produkt für In-App-Nachrichten können Sie die Anzeige von In-App-Nachrichten infolge verschiedener Event-Typen auslösen: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Außerdem enthalten die Trigger `Specific Purchase` und `Custom Event` robuste Eigenschaftsfilter.

{% alert note %}
Ausgelöste In-App-Nachrichten funktionieren nur bei angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Event (wie Kauf-Events) getriggert werden. Wenn Sie mit iOS arbeiten, lesen Sie unseren Artikel über [das Verfolgen von benutzerdefinierten Ereignissen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), um mehr zu erfahren.
{% endalert %}

## Semantik der Zustellung

Alle In-App-Nachrichten, für die ein Nutzer berechtigt ist, werden zu Beginn der Sitzung an das Gerät des Nutzers gesendet. Wenn durch ein Event zwei In-App-Nachrichten ausgelöst werden, wird die In-App-Nachricht mit der höheren Priorität angezeigt. Weitere Informationen über die Sitzungsstart-Semantik des SDK finden Sie unter [Lebenszyklus einer Sitzung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle). Bei der Zustellung ruft das SDK die Assets mittels Prefetching ab, damit sie zum Trigger-Zeitpunkt sofort verfügbar sind und die Anzeige-Latenzzeit minimiert wird.

Wenn ein Trigger-Event mit mehr als einer in Frage kommenden In-App-Nachricht verbunden ist, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort nach der Zustellung angezeigt werden (Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da die Assets nicht mittels Prefetching abgerufen werden.

## Mindestzeitintervall zwischen Auslösern

Standardmäßig begrenzen wir die Anzahl der In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu ermöglichen.

Sie können diesen Wert über `ABKMinimumTriggerTimeIntervalKey` im Parameter `appboyOptions` überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Stellen Sie `ABKMinimumTriggerTimeIntervalKey` auf den ganzzahligen Wert ein, den Sie als Mindestzeit in Sekunden zwischen In-App-Nachrichten angeben möchten:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Wenn kein passender Trigger gefunden wird

Wenn Braze keinen passenden Trigger für ein bestimmtes Event findet, wird die Methode [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) von [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html) aufgerufen. Implementieren Sie diese Methode in Ihrer Klasse und verwenden Sie dabei das Delegate-Protokoll für dieses Szenario. 

## Lokale Zustellung von In-App-Nachrichten

### In-App-Nachrichten-Stack

#### Anzeigen von In-App-Nachrichten

Wenn ein Nutzer zum Empfang einer In-App-Nachricht berechtigt ist, wird `ABKInAppMessageController` die neueste In-App-Nachricht aus dem In-App-Nachrichten-Stack angeboten. Der Stack hält nur gespeicherte In-App-Nachrichten im Speicher und wird zwischen den App-Starts aus dem angehaltenen Modus geleert.

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Tastatur auf dem Bildschirm angezeigt wird, da die Darstellung in diesem Fall undefiniert ist.
{% endalert %}

#### Hinzufügen von In-App-Nachrichten zum Stapel

In den folgenden Situationen sind Nutzer zum Empfang von In-App-Nachrichten berechtigt:

- Wenn ein Event zum Triggern einer In-App-Nachricht ausgelöst wird
- Bei einem Sitzungsstart-Event
- Die App wird über eine Push-Benachrichtigung geöffnet

Getriggerte In-App-Nachrichten werden auf den Stack platziert, wenn ihr Trigger-Event ausgelöst wird. Wenn sich mehrere In-App-Nachrichten im Stack befinden und darauf warten, angezeigt zu werden, zeigt Braze die zuletzt empfangene In-App-Nachricht zuerst an ("Last In-First Out"-Prinzip).

#### Rückgabe von In-App-Nachrichten an den Stack

Eine getriggerte In-App-Nachricht kann in den folgenden Situationen an den Stack zurückgegeben werden:

- Die In-App-Nachricht wird ausgelöst, wenn sich die App im Hintergrund befindet.
- Eine weitere In-App-Nachricht ist derzeit sichtbar.
- Die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` wurde nicht implementiert und die Tastatur wird derzeit angezeigt.
- Die [Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` oder die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` gibt `ABKDisplayInAppMessageLater` zurück.

#### Verwerfen von In-App-Nachrichten

Eine getriggerte In-App-Nachricht wird in den folgenden Situationen verworfen:

- Die [Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` oder die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` gibt `ABKDiscardInAppMessage` zurück.
- Das Asset (Bild oder ZIP-Datei) der In-App-Nachricht konnte nicht heruntergeladen werden.
- Die In-App-Nachricht ist zur Anzeige bereit, aber das Timeout wurde überschritten.
- Die Ausrichtung des Geräts stimmt nicht mit der Ausrichtung der ausgelösten In-App-Nachricht überein.
- Die In-App-Nachricht ist eine In-App-Nachricht des Typs "Full", enthält aber kein Bild.
- Die In-App-Nachricht ist eine modale In-App-Nachricht, die nur ein Bild enthält.

#### Manuelles Aufnehmen von In-App-Nachrichten in die Anzeigewarteschlange

Wenn Sie eine In-App-Nachricht zu anderen Zeiten in Ihrer App anzeigen möchten, können Sie die oberste In-App-Nachricht auf dem Stapel manuell anzeigen, indem Sie die folgende Methode aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Erstellung und Anzeige von In-App-Nachrichten in Echtzeit

In-App-Nachrichten können auch lokal in der App erstellt und über Braze angezeigt werden. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Echtzeit in der App auslösen möchten. Braze unterstützt keine Analyse von lokal erstellten In-App-Nachrichten.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab schnell %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

