---
nav_title: Steuerung des Netzwerkverkehrs
article_title: Fine Network Traffic Control für iOS
platform: Swift
page_order: 2
description: "Dieser Artikel beschreibt, wie Sie die Steuerung des Netzwerkverkehrs für das Swift SDK implementieren."

---

# Steuerung des Netzwerkverkehrs

## Richtlinien für die Bearbeitung von Anfragen

Braze bietet Nutzern die Möglichkeit, den Netzwerkverkehr mit den folgenden Protokollen zu steuern:

### Automatische Bearbeitung von Anfragen

***`RequestPolicy` Enum-Wert: `automatic`***

Dies ist die Standardeinstellung für die **Anforderungsrichtlinie**. Bei diesem Wert werden sofortige Serveranfragen durchgeführt, wenn benutzerseitige Daten für Braze-Funktionen, wie z. B. In-App-Nachrichten, erforderlich sind.

Das Braze SDK verarbeitet automatisch die gesamte Serverkommunikation, darunter:
- Flushen der Daten von angepassten Events und Attributen an die Braze-Server
- Inhaltskarten und Geofences aktualisieren
- Anfordern neuer In-App-Nachrichten

Um die Serverlast zu verringern, führt Braze alle paar Sekunden Flushes neuer Nutzerdaten durch.

### Manuelle Bearbeitung von Anfragen

***`RequestPolicy` Enum-Wert: `manual`***

Dieses Protokoll entspricht der automatischen Anforderungsverarbeitung mit Ausnahme der folgenden Punkte:
- Benutzerdefinierte Attribute und benutzerdefinierte Ereignisdaten werden während der Benutzersitzung nicht automatisch an den Server übertragen.
- Braze führt weiterhin automatische Netzwerkanforderungen für interne Features durch, wie z. B. das Anfordern von In-App-Nachrichten, Liquid-Templates in In-App-Nachrichten, Geofences und Standortverfolgung. Weitere Einzelheiten finden Sie in der [Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) `Braze.Configuration.Api.RequestPolicy.manual`. Wenn diese internen Anfragen gestellt werden, können je nach Art der Anfrage lokal gespeicherte benutzerdefinierte Attribute und benutzerdefinierte Ereignisdaten an den Braze-Server übertragen werden.

### Manuelles Flushen von Nutzerdaten

Mit der folgenden Methode können die Daten jederzeit manuell auf die Braze-Server geflusht werden:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% endtabs %}
## Festlegen der Richtlinien für die Bearbeitung von Anfragen

### Festlegen der Anforderungsrichtlinie beim Starten der App

Diese Richtlinien können beim Starten der App festgelegt werden, wenn Sie die Braze-Konfiguration initialisieren. Legen Sie [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum) im Objekt `configuration` wie im folgenden Code-Snippet fest:

{% tabs %}
{% tab schnell %}

```swift
configuration.api.requestPolicy = .automatic
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```

{% endtab %}
{% endtabs %}


