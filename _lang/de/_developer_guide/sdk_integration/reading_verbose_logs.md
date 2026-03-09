---
page_order: 1.5
nav_title: Ausführliche Protokolle lesen
article_title: Ausführliche Protokolle lesen
description: "Erfahren Sie, wie Sie die ausführliche Protokollausgabe des Braze SDK lesen und interpretieren, einschließlich der wichtigsten Einträge für Push-Benachrichtigungen, In-App-Nachrichten, Content-Cards und Deeplinks."
---

# Ausführliche Protokolle lesen

> Auf dieser Seite wird erläutert, wie die ausführliche Protokollausgabe des Braze SDK interpretiert werden kann. Für jeden Messaging-Kanal finden Sie die wichtigsten Protokolleinträge, die Sie suchen sollten, deren Bedeutung und häufige Probleme, auf die Sie achten sollten.

Bevor Sie beginnen, stellen Sie bitte sicher, dass Sie [die ausführliche Protokollierung aktiviert]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) haben und wissen, wie Sie Protokolle auf Ihrer Plattform erfassen können.

## Sitzungen

Sitzungen bilden die Grundlage für Analytics und die Zustellung von Braze. Viele Messaging-Features – einschließlich In-App-Nachrichten und Content-Cards – erfordern eine gültige Sitzung, bevor sie funktionieren können. Sollten Sitzungen nicht korrekt protokolliert werden, überprüfen Sie dies bitte zunächst. Weitere Informationen zum Enablement des Sitzungsverfolgens finden Sie in [Schritt 5: Bitte aktivieren Sie das Tracking von ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking)Benutzersitzungen.

### Wichtige Protokolleinträge

{% tabs %}
{% tab Swift %}

**Beginn der Sitzung:**

```
Started user session (id: <SESSION_ID>)
```

**Sitzung beendet:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Beginn der Sitzung:**

Bitte suchen Sie nach den folgenden Eingängen:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtern Sie Netzwerk-Anfragen für Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), um das Ereignis „Sitzung gestartet (`ss`)“ anzuzeigen.

**Sitzung beendet:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Bitte überprüfen Sie, ob beim Start der App ein Protokoll zum Sitzungsbeginn angezeigt wird.
- Sollten Sie keinen Sitzungsstart feststellen, überprüfen Sie bitte, ob das SDK ordnungsgemäß initialisiert ist und ob`openSession`(Android) aufgerufen wird.
- Bitte überprüfen Sie auf Android, ob eine Netzwerkanfrage an den Braze-Endpunkt gesendet wird. Sollten Sie dies nicht sehen, überprüfen Sie bitte Ihren API-Schlüssel und Ihre Konfiguration des Endpunkts.

## Push-Benachrichtigungen

Mithilfe von Protokollen für Push-Benachrichtigungen können Sie überprüfen, ob Gerätetoken registriert sind, Benachrichtigungen zugestellt werden und Klickereignisse nachverfolgt werden.

### Token-Registrierung

Zu Beginn einer Sitzung registriert das SDK das Push-Token des Geräts bei Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie in den Attributen des`push_token` Anfragetextes nach:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Bitte überprüfen Sie auch, ob die Informationen zum Gerät Folgendes enthalten:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Bitte suchen Sie das FCM-Registrierungsprotokoll:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Bitte überprüfen Sie Folgendes:

- `com_braze_firebase_cloud_messaging_registration_enabled` ist`true`.
- Die FCM-Absender-ID entspricht Ihrem Firebase-Projekt.

Ein häufiger Fehler ist `SENDER_ID_MISMATCH`, was bedeutet, dass die konfigurierte ID des Absenders nicht mit Ihrem Firebase-Projekt übereinstimmt.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Falls in der `push_token`Anfrage der Text fehlt, wurde der Token nicht erfasst. Bitte überprüfen Sie die Push-Einstellungen in Ihrer App-Konfiguration.
- Wenn`ios_push_auth`  angezeigt wird`denied`oder `provisional`, hat die Nutzer:in keine vollständige Push-Berechtigung erteilt.
- Wenn Sie auf Android die Meldung sehen`SENDER_ID_MISMATCH`, aktualisieren Sie bitte Ihre FCM-Sender-ID, damit sie mit Ihrem Firebase-Projekt übereinstimmt.

### Zustellung und Klick

Wenn eine Push-Benachrichtigung angetippt wird, protokolliert das SDK die Verarbeitungs- und Klickereignisse.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Gefolgt vom Klick-Ereignis:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Wenn die Push-Benachrichtigung einen Deeplink enthält, wird Ihnen außerdem Folgendes angezeigt:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Anschließend werden die Push-Nutzlast und die Anzeigelogdateien bereitgestellt. Für Deeplinks suchen Sie bitte nach den Einträgen „Deep `UriAction`Link Delegate“ oder „Deep Link“.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Bitte überprüfen Sie, ob die Push-Nutzlast die erwarteten `title`,`body` , und alle Deeplinks (`ab_uri`) enthält.
- Bitte bestätigen Sie, dass ein`pushClick`Ereignis nach dem Antippen protokolliert wird.
- Sollte das Klick-Ereignis fehlen, überprüfen Sie bitte, ob Ihr App-Delegate oder Benachrichtigungs-Handler Push-Ereignisse ordnungsgemäß an das Braze SDK weiterleitet.

## In-App-Nachrichten

Die In-App-Nachrichtenprotokolle zeigen Ihnen den gesamten Lebenszyklus: Zustellung vom Server, Auslösung basierend auf Ereignissen, Anzeige, Impression-Protokollierung und Klick-Tracking.

### Zustellung von Nachrichten

Wenn ein Nutzer eine Sitzung startet und für eine In-App-Nachricht berechtigt ist, empfängt das SDK die Nachrichten-Nutzlast vom Server.

{% tabs %}
{% tab Swift %}

Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), die die In-App-Nachricht-Daten enthalten.

Der Antworttext enthält die Nutzlast der Nachricht, einschließlich:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Bitte suchen Sie nach dem Protokoll, das das auslösende Ereignis triggert:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Dies bestätigt, dass die In-App-Nachricht mit einem Auslöseereignis abgeglichen wurde.

{% endtab %}
{% endtabs %}

### Anzeige und Impression der Nachricht

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Es folgt das Protokoll der Impressionen:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Klick- und Button-Ereignisse

Wenn ein Nutzer:in auf einen Button tippt oder die Nachricht schließt:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Wenn keine weiteren getriggerten Nachrichten übereinstimmen, wird außerdem Folgendes angezeigt:

```
No matching trigger for event.
```

Dies ist das erwartete Verhalten, wenn für das Ereignis keine zusätzlichen In-App-Nachrichten konfiguriert sind.

{% endtab %}
{% tab Android %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach Ereignissen mit dem Namen`sbc`(Button-Klick) oder`si`(Impression) im Anfragetext.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Sollte die In-App-Nachricht nicht angezeigt werden, überprüfen Sie bitte zunächst, ob ein Sitzungsstart protokolliert wurde.
- Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt, um zu bestätigen, dass die Nachrichtennutzlast zugestellt wurde.
- Falls keine Impressionen protokolliert werden, überprüfen Sie bitte, ob Sie einen benutzerdefinierten`inAppMessageDisplay`Delegaten implementiert haben, der die Protokollierung unterdrückt.
- Wenn „Kein passender Auslöser für Ereignis“ angezeigt wird, ist dies normal und bedeutet, dass für dieses Ereignis keine zusätzlichen In-App-Nachrichten konfiguriert sind.

## Content-Cards

Mithilfe von Content-Card-Protokollen können Sie überprüfen, ob Karten mit dem Gerät synchronisiert und den Nutzern angezeigt werden und ob Interaktionen (Impressionen, Klicks, Ablehnungen) nachverfolgt werden.

### Kartensynchronisierung

Content-Cards werden zu Beginn der Sitzung und bei einer manuellen Anfrage synchronisiert. Wenn keine Sitzung protokolliert ist, werden keine Content-Cards angezeigt.

{% tabs %}
{% tab Swift %}

Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), die die Kartendaten enthalten.

Der Antworttext enthält die Karten-Daten, darunter:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Schlüsselfelder:
- `v` (angesehen):`0`  = nicht angesehen,`1`  = angesehen
- `cl` (mit Klick):`0`  = nicht angeklickt,`1`  = angeklickt
- `p` (angeheftet):`0`  = nicht angeheftet,`1`  = angeheftet
- `tp` (Typ): `short_news`, `captioned_image`, `classic`, usw.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Anschließend wird eine POST-Anfrage an den von Ihnen konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) gesendet, die Informationen zu Nutzern und Geräten enthält.

{% endtab %}
{% endtabs %}

### Impressionen, Klicks und Ablehnungen

{% tabs %}
{% tab Swift %}

**Impression:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Klicken Sie bitte hier:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Wenn die Karte eine URL enthält, wird außerdem Folgendes angezeigt:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Entlassung:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach Ereignisnamen im Anfragetext:
- `cci` — Eindruck der Content-Card
- `ccc` — Klicken Sie auf die Content-Card
- `ccd` — Content-Card geschlossen

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- **Keine Karten angezeigt**: Bitte überprüfen Sie, ob der Beginn einer Sitzung protokolliert wurde. Content-Cards erfordern eine aktive Sitzung, um synchronisiert zu werden.
- **Fehlende Karten für neue Nutzer:innen**: Neue Nutzer:innen sehen möglicherweise bei ihrer ersten Sitzung keine Content-Cards, bis sie die nächste Sitzung starten. Dies ist das erwartete Verhalten.
- **Die Karte überschreitet die Größenbeschränkung**: Content-Cards, die größer als 2 KB sind, werden nicht angezeigt, und die Nachricht wird abgebrochen.
- **Die Karte bleibt nach Beendigung der Kampagne persistent**: Bitte überprüfen Sie, ob die Synchronisierung nach Beendigung der Kampagne abgeschlossen wurde. Content-Cards werden nach einer erfolgreichen Synchronisierung vom Gerät entfernt. Bitte stellen Sie beim Beenden einer Kampagne sicher, dass die Option zum Entfernen aktiver Karten aus den Feeds der Nutzer:innen ausgewählt ist.

## Deeplinks

Deeplink-Protokolle werden in Push-Benachrichtigungen, In-App-Nachrichten und Content-Cards angezeigt. Die Protokollstruktur ist unabhängig vom Quellkanal konsistent.

{% tabs %}
{% tab Swift %}

Wenn das SDK einen Deeplink verarbeitet:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Wobei  eines der folgenden`<SOURCE_CHANNEL>` Elemente ist: `notification`,`inAppMessage` , oder `contentCard`.

{% endtab %}
{% tab Android %}

Für Deeplinks suchen Sie bitte in Logcat nach den Einträgen **„Deep Link Delegate“** oder **„UriAction**“. Um die Auflösung von Deeplinks unabhängig zu testen, führen Sie bitte den folgenden Befehl aus:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Dies bestätigt, ob der Deeplink außerhalb des Braze SDK korrekt aufgelöst wird.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Bitte überprüfen Sie, ob die Deeplink-URL mit der in der Kampagne konfigurierten URL übereinstimmt.
- Falls der Deeplink über einen Kanal (z. B. Push) funktioniert, jedoch nicht über einen anderen (z. B. Content-Cards), überprüfen Sie bitte, ob Ihre Deeplink-Implementierung alle Kanäle unterstützt.
- Unter iOS erfordern Universal Links eine zusätzliche Bearbeitung. Sollten Universal Links über Braze-Kanäle nicht funktionieren, überprüfen Sie bitte, ob Ihre App das`BrazeDelegate`Protokoll für die URL-Verarbeitung implementiert hat.
- Bitte überprüfen Sie bei Android, ob die automatische Verarbeitung von Deeplinks deaktiviert ist, falls Sie einen angepassten Handler verwenden. Andernfalls kann es zu Konflikten zwischen dem Standard-Handler und Ihrer Implementierung kommen.

## Benutzeridentifikation

Wenn eine Nutzer:in mit einem Bezeichner `external_id`identifiziert wird, protokolliert das SDK ein Ereignis zur Benutzeränderung.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Wichtige Informationen:
- Bitte `changeUser`rufen Sie an, sobald sich die Nutzer:innen angemeldet haben – je früher, desto besser.
- Wenn sich ein Nutzer:in abmeldet, gibt es keine Möglichkeit, ihn wieder in einen anonymen Nutzer:in zurückzuversetzen`changeUser`.
- Wenn Sie keine anonymen Nutzer:innen wünschen, rufen Sie bitte`changeUser` während des Sitzungsstarts oder beim Start der App auf.

{% endtab %}
{% tab Swift %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie im Anfragetext nach der Identifikation der Nutzer:innen:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Netzwerfanfragen

Ausführliche Protokolle enthalten vollständige Details zu HTTP-Anfragen und -Antworten für die SDK-Kommunikation mit Braze-Servern. Diese sind hilfreich bei der Diagnose von Verbindungsproblemen.

### Anfragestruktur

Bitte verwenden Sie einen Filter für Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com). Die Anfragestruktur umfasst:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- **API-Schlüssel**: Bitte überprüfen Sie, ob`XBraze-ApiKey` dies mit dem API-Schlüssel Ihres Workspaces übereinstimmt.
- **Endpunkt**: Bitte überprüfen Sie, ob die Anfrage-URL mit Ihrem konfigurierten SDK-Endpunkt übereinstimmt.
- **Wiederholungsversuche**:`XBraze-Req-Attempt`**Ein Wert** größer als 1 bedeutet, dass das SDK eine fehlgeschlagene Anfrage erneut versucht, was auf Verbindungsprobleme hindeuten kann.
- **Rate-Limiting**:`XBraze-Req-Tokens-Remaining`Zeigt die verbleibenden Token für Anfragen an. Ein niedriger Wert kann darauf hindeuten, dass das SDK die Rate-Limits erreicht.
- **Fehlende Anfragen**: Wenn Sie unter Android nach dem Start der Sitzung keine Anfrage an den Braze-Endpunkt sehen, überprüfen Sie bitte Ihren API-Schlüssel und die Endpunktkonfiguration.

## Gängige Abkürzungen für Veranstaltungen

In ausführlichen Protokoll-Nutzdaten verwendet Braze abgekürzte Ereignisnamen. Hier ist eine Referenz:

| Abkürzung | Event |
|---|---|
| `ss` | Beginn der Sitzung |
| `se` | Ende der Sitzung |
| `si` | Anzeige von In-App-Nachrichten |
| `sbc` | Klick auf den Button für In-App-Nachrichten |
| `cci` | Eindruck der Content-Card |
| `ccc` | Content-Card anklicken |
| `ccd` | Content-Card geschlossen |
| `lr` | Aufgezeichneter Standort |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }