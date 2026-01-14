---
nav_title: Steuerung des Netzwerkverkehrs
article_title: Fine Network Traffic Control für iOS
platform: iOS
page_order: 1
description: "Dieser Artikel befasst sich mit der Implementierung der Feinsteuerung des Netzwerkverkehrs für Ihre iOS-Anwendung."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Feinsteuerung des Netzwerkverkehrs

## Richtlinien für die Bearbeitung von Anfragen

Braze erlaubt es den Nutzer, den Netzwerkverkehr mit den folgenden Protokollen zu steuern:

### Automatische Bearbeitung von Anfragen

***`ABKRequestProcessingPolicy` Enum-Wert: `ABKAutomaticRequestProcessing`***

- Dies ist der **Standardwert für die Anfragenrichtlinie**.
- Das Braze SDK kümmert sich automatisch um die gesamte Serverkommunikation, darunter:
    - Flushen der Daten von angepassten Events und Attributen an die Braze-Server
    - Updates von Content-Cards und Geofences
    - Anfordern neuer In-App-Nachrichten
- Unmittelbare Server-Anfragen werden durchgeführt, wenn für Braze Features, wie z. B. In-App-Nachrichten, benutzerseitige Daten erforderlich sind.
- Um die Serverlast zu minimieren, führt Braze regelmäßig alle paar Sekunden Flushes neuer Nutzerdaten durch.

Sie können die Daten jederzeit manuell auf die Braze Server übertragen, indem Sie die folgende Methode verwenden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### Manuelle Bearbeitung von Anfragen

***`ABKRequestProcessingPolicy` Enum-Wert: `ABKManualRequestProcessing`***

- Dieses Protokoll ist dasselbe wie die automatische Anforderungsverarbeitung, mit der Ausnahme, dass es sich um ein Protokoll handelt:
    - Benutzerdefinierte Attribute und benutzerdefinierte Ereignisdaten werden während der Benutzersitzung nicht automatisch an den Server übertragen.
- Braze führt weiterhin automatische Netzwerkanforderungen für interne Features durch, wie z. B. das Anfordern von In-App-Nachrichten, Liquid-Templates in In-App-Nachrichten, Geofences und Standortverfolgung. Weitere Einzelheiten finden Sie in der Erklärung `ABKRequestProcessingPolicy` in [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h). Wenn diese internen Anfragen gestellt werden, können je nach Art der Anfrage lokal gespeicherte benutzerdefinierte Attribute und benutzerdefinierte Ereignisdaten an den Braze-Server übertragen werden.

Sie können die Daten jederzeit manuell auf die Braze Server übertragen, indem Sie die folgende Methode verwenden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## Festlegen der Richtlinien für die Bearbeitung von Anfragen

### Festlegen der Anfragenrichtlinie bei App-Start

Diese Richtlinien kann beim Start der App mit der Methode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) festgelegt werden. Setzen Sie im Wörterbuch `appboyOptions` den `ABKRequestProcessingPolicyOptionKey` wie im folgenden Code Snippet gezeigt:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab schnell %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Festlegen der Anfragenrichtlinie bei Laufzeit

Die Richtlinie für die Verarbeitung von Anfragen kann auch während der Laufzeit über die Eigenschaft `requestProcessingPolicy` auf `Appboy` festgelegt werden:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab schnell %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Manuelle Abschaltung von In-Flight-Serverkommunikation

Wenn zu irgendeinem Zeitpunkt eine "In-Flight"-Serverkommunikation angehalten werden muss, müssen Sie die folgende Methode aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

Nach dem Aufruf dieser Methode müssen Sie den Bearbeitungsmodus der Anfrage auf automatisch zurücksetzen. Aus diesem Grund empfehlen wir, diese Funktion nur dann aufzurufen, wenn das Betriebssystem Sie dazu zwingt, Hintergrundaufgaben oder ähnliches zu beenden.

