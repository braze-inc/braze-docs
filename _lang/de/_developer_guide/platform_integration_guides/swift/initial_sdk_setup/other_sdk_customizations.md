---
nav_title: Andere SDK-Anpassungen
article_title: Andere SDK-Anpassungen für Swift
platform: Swift
description: "Dieses Dokument enthält zusätzliche Schritte zur Konfiguration des Braze Swift SDK."
page_order: 3

---

# Andere SDK-Anpassungen für Swift

> Das Braze Swift SDK kann konfiguriert werden, indem Sie die Eigenschaften des `Braze.Configuration`-Objekts ändern, das mit Ihrer Braze-Instanz verbunden ist. Beachten Sie, dass die Konfiguration nur vor der Initialisierung der Braze-Instanz mit `Braze(configuration:)` vorgenommen werden kann.

Eine vollständige Liste der verfügbaren Konfigurationen finden Sie in der [Dokumentation zur KlasseBraze.Configuration ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

## Braze Protokollstufe

Die Standard-Protokollebene für das Braze Swift SDK ist `.error` in der folgenden Tabelle. Diese Stufe ist die minimalste Stufe über der vollständig deaktivierten Protokollierung.

Siehe die folgende Liste der verfügbaren Protokollebenen:

| Swift       | Objective-C              | Beschreibung                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | Debugging-Informationen protokollieren + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | Allgemeine SDK-Informationen protokollieren (Nutzer:innen-Änderungen, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Fehler protokollieren.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | Es erfolgt keine Protokollierung.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Einstellung der Protokollstufe

Die Protokollstufe kann zur Laufzeit auf Ihrem `Braze.Configuration`-Objekt zugewiesen werden:

{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Die vollständige Verwendung des Braze Logger finden Sie in der [Dokumentation der Klasse Logger](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

