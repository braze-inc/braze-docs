---
nav_title: SDK-Ersteinrichtung
article_title: Erste SDK-Einrichtung für Roku
platform: Roku
page_order: 0
page_type: reference
description: "Auf dieser Seite werden die Schritte zur Ersteinrichtung des Braze Roku SDK beschrieben."
search_rank: 1
---

# Erste SDK-Integration

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK für Roku installieren. Durch die Installation des Braze Roku SDK erhalten Sie grundlegende Analytics- und Segmentierungsfunktionen.

{% alert tip %}
Sehen Sie sich unsere Beispiel-Roku-App auf GitHub an: [TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv).
{% endalert %}

## Schritt 1: Dateien hinzufügen

Die Dateien des Braze SDK finden Sie im Verzeichnis `sdk_files` im [Braze Roku SDK Repository](https://github.com/braze-inc/braze-roku-sdk).

1. Fügen Sie `BrazeSDK.brs` zu Ihrer App im Verzeichnis `source` hinzu.
2. Fügen Sie `BrazeTask.brs` und `BrazeTask.xml` zu Ihrer App in das Verzeichnis `components` hinzu.

## Schritt 2: Referenzen hinzufügen

Fügen Sie einen Verweis auf `BrazeSDK.brs` in Ihre Hauptszene ein, indem Sie das folgende `script`-Element verwenden:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Schritt 3: Konfigurieren Sie

Legen Sie unter `main.brs` die Braze-Konfiguration auf dem globalen Knoten fest:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Den [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) und den API-Schlüssel können Sie dem Braze-Dashboard entnehmen.

## Schritt 4: Braze initialisieren

Initialisieren Sie die Braze-Instanz:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Protokollierung aktivieren (optional) {#logging}

Um Ihre Braze-Integration zu debuggen, können Sie die Roku Debug-Konsole für Braze-Protokolle anzeigen. Weitere Informationen finden Sie im Artikel [Debugging-Code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) von Roku Developers.

## Grundlegende SDK-Integration abgeschlossen

Braze sollte nun mit dem Braze Roku SDK Daten von Ihrer Anwendung erfassen. 

In den folgenden Artikeln erfahren Sie, wie Sie [Attribute]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/), [Events]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/) und [Käufe]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/) mit unserem SDK protokollieren.

Um mehr über In-App-Nachrichten für Roku zu erfahren, lesen Sie unseren [Leitfaden zur Integration von In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).


