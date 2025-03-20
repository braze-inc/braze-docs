---
nav_title: Fehler &amp; Antworten
article_title: API-Fehler &amp; Antworten
description: "Dieser Referenzartikel behandelt die verschiedenen Fehler und Serverantworten, die bei der Verwendung der Braze-API auftreten können, und wie Sie diese beheben können." 
page_type: reference
page_order: 2.3

---
# API-Fehler und Antworten

> Dieser Referenzartikel behandelt die verschiedenen Fehler und Serverantworten, die bei der Verwendung der Braze-API auftreten können, und wie Sie diese beheben können. 

{% raw %}

## Server-Antworten

Wenn Ihr POST-Payload von unseren Servern akzeptiert wurde, erhalten Sie auf erfolgreiche Nachrichten die folgende Antwort:

```json
{
  "message" : "success"
}
```

Beachten Sie, dass Erfolg nur bedeutet, dass die RESTful-API-Nutzdaten korrekt geformt und an unsere Push-Benachrichtigung, E-Mail oder andere Nachrichtendienste weitergeleitet wurden. Das bedeutet nicht, dass die Nachrichten tatsächlich zugestellt wurden, da weitere Faktoren die Zustellung verhindern könnten (z.B. könnte ein Gerät offline sein, das Push-Token könnte von Apples Servern abgelehnt werden, Sie könnten eine unbekannte Benutzer-ID angegeben haben).

Wenn Ihre Nachricht erfolgreich ist, aber nicht schwerwiegende Fehler aufweist, erhalten Sie die folgende Antwort:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

Im Falle eines Erfolgs werden alle Nachrichten, die nicht von einem Fehler im Array `errors` betroffen waren, weiterhin zugestellt. Wenn Ihre Nachricht einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Antworten für verfolgte Sende-IDs

Analysen sind für Kampagnen immer verfügbar. Darüber hinaus sind Analysen für eine bestimmte Kampagnen-Sendeinstanz verfügbar, wenn die Kampagne als Broadcast gesendet wird. Wenn die Nachverfolgung für einen bestimmten Kampagnenversand verfügbar ist, erhalten Sie die folgende Antwort:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

Die angegebene Sende-ID kann als Parameter für den Endpunkt `/send/data_series` verwendet werden, um sendungsspezifische Analysen abzurufen.

## Fehler

Das Statuscode-Element einer Serverantwort ist eine dreistellige Zahl, wobei die erste Ziffer des Codes die Klasse der Antwort definiert.

- Der Statuscode der **Klasse 2XX** (non-fatal) zeigt an, dass **Ihre Anfrage** erfolgreich empfangen, verstanden und akzeptiert wurde.
- Die **Klasse 4XX** des Statuscodes (fatal) weist auf einen **Client-Fehler** hin. In der Tabelle der schwerwiegenden Fehler finden Sie eine vollständige Liste der 4XX-Fehlercodes und deren Beschreibungen.
- Die **Klasse 5XX** des Statuscodes (fatal) weist auf einen **Serverfehler** hin. Es gibt mehrere mögliche Ursachen, z.B. kann der Server, auf den Sie zugreifen möchten, die Anfrage nicht ausführen, der Server wird gewartet und kann die Anfrage daher nicht ausführen, oder der Server hat ein hohes Verkehrsaufkommen. In diesem Fall empfehlen wir Ihnen, Ihre Anfrage mit exponentiellem Backoff zu wiederholen. Im Falle eines Vorfalls oder Ausfalls ist Braze nicht in der Lage, REST-API-Aufrufe, die während des Zeitfensters des Vorfalls fehlgeschlagen sind, wiederzugeben. Sie müssen alle Anrufe, die während des Störungsfensters fehlgeschlagen sind, erneut versuchen.

### Fatale Fehler

Die folgenden Statuscodes und zugehörigen Fehlermeldungen werden zurückgegeben, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt.

{% endraw %}
{% alert warning %}
Alle der folgenden Fehlercodes bedeuten, dass keine Nachrichten gesendet werden.
{% endalert %}
{% raw %}

| Fehler Code | Beschreibung |
|---|---|
| `5XX Internal Server Error` | Wiederholen Sie Ihre Anfrage mit exponentiellem Backoff.|
| `400 Bad Request` | Schlechte Syntax.|
| `400 No Recipients` | Es gibt keine externen IDs oder Segment-IDs oder keine Push-Tokens in der Anfrage.|
| `400 Invalid Campaign ID` | Es wurde keine Messaging-API-Kampagne für Ihre angegebene Kampagnen-ID gefunden.|
| `400 Message Variant Unspecified` | Sie geben eine Kampagnen-ID an, aber keine ID für die Nachrichtenvariation.|
| `400 Invalid Message Variant` | Sie haben eine gültige Kampagnen-ID angegeben, aber die ID der Nachrichtenvariation stimmt mit keiner der Nachrichten dieser Kampagne überein.|
| `400 Mismatched Message Type` | Sie haben für mindestens eine Ihrer Nachrichten eine Nachrichtenvariante des falschen Nachrichtentyps angegeben.|
| `400 Invalid Extra Push Payload` | Sie geben den Schlüssel `extra` entweder für `apple_push` oder `android_push` an, aber es handelt sich nicht um ein Wörterbuch.|
| `400 Max Input Length Exceeded` | Verursacht durch den Aufruf von mehr als 75 externen IDs beim Aufrufen des Endpunkts `/users/track`.|
| `400 The max number of external_ids and aliases per request was exceeded` | Verursacht durch den Anruf von mehr als 50 externen IDs.|
| `400 The max number of ids per request was exceeded` | Verursacht durch den Anruf von mehr als 50 externen IDs.|
| `400 No message to send` | Für die Nachricht ist keine Nutzlast angegeben.|
| `400 Slideup Message Length Exceeded` | Die Slideup-Nachricht enthält mehr als 140 Zeichen.|
| `400 Apple Push Length Exceeded` | Die JSON-Nutzlast ist größer als 1.912 Bytes.|
| `400 Android Push Length Exceeded` | Die JSON-Nutzlast beträgt mehr als 4.000 Bytes.|
| `400 Bad Request` | `send_at` datetime kann nicht geparst werden.|
| `400 Bad Request` | In Ihrer Anfrage ist `in_local_time` richtig, aber `time` ist in der Zeitzone Ihres Unternehmens vergangen.|
| `401 Unauthorized` | Ungültiger API-Schlüssel. |
| `403 Forbidden` | Der Tarifplan wird nicht unterstützt, oder das Konto ist aus anderen Gründen inaktiv.|
| `403 Access Denied` | Der von Ihnen verwendete REST-API-Schlüssel verfügt nicht über ausreichende Berechtigungen. Überprüfen Sie die API-Schlüssel-Berechtigungen auf der Seite **Einstellungen**.|
| `404 Not Found` | Ungültige URL. |
| `429 Rate Limited` | Über das Ratenlimit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}
