## Kontrolle des Netzwerkverkehrs

### Anfrage zu Richtlinien für die Verarbeitung

Braze erlaubt es den Nutzer, den Netzwerkverkehr mit den folgenden Protokollen zu steuern:

{% tabs local %}
{% tab automatic %}
Standardmäßig ist der `RequestPolicy` enum-Wert auf `automatic` eingestellt. Wenn diese Option eingestellt ist, werden sofortige Server-Anfragen durchgeführt, wenn benutzerseitige Daten für Braze-Features wie In-App-Nachrichten erforderlich sind.

Das Braze SDK verarbeitet automatisch die gesamte Serverkommunikation, darunter:

- Flushen der Daten von angepassten Events und Attributen an die Braze-Server
- Inhaltskarten und Geofences aktualisieren
- Anfordern neuer In-App-Nachrichten

Um die Serverlast zu minimieren, führt Braze regelmäßig alle paar Sekunden Flushes neuer Nutzerdaten durch.
{% endtab %}

{% tab manual %}
Wenn der `RequestPolicy` enum-Wert `manual` lautet, wird die gleiche Leistung wie bei der automatischen Verarbeitung von Anfragen erbracht, außer dass:

- Benutzerdefinierte Attribute und benutzerdefinierte Ereignisdaten werden während der Benutzersitzung nicht automatisch an den Server übertragen.
- Braze führt weiterhin automatische Netzwerkanforderungen für interne Features durch, wie z. B. das Anfordern von In-App-Nachrichten, Liquid-Templates in In-App-Nachrichten, Geofences und Standortverfolgung. Weitere Einzelheiten finden Sie in der [Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) `Braze.Configuration.Api.RequestPolicy.manual`. Bei diesen internen Anfragen kann Braze je nach Art der Anfrage lokal gespeicherte angepasste Attribute und angepasste Event-Daten an den Braze Server übertragen.
{% endtab %}
{% endtabs %}

### Manuelles Flushen von Nutzerdaten

Sie können die Daten jederzeit manuell auf die Braze Server übertragen, indem Sie die folgende Methode verwenden:

{% tabs %}
{% tab swift %}
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

### Festlegen der Richtlinien für die Bearbeitung von Anfragen

Diese Richtlinien können beim Starten der App festgelegt werden, wenn Sie die Braze-Konfiguration initialisieren. Legen Sie [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum) im Objekt `configuration` wie im folgenden Code-Snippet fest:

{% tabs %}
{% tab swift %}
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
