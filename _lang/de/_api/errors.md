---
nav_title: Fehler und Antworten
article_title: API-Fehler und Antworten
description: "Dieser Referenzartikel behandelt die verschiedenen Fehler und Server-Antworten, die bei der Verwendung der Braze API auftreten können, und wie Sie diese beheben können."
page_type: reference
page_order: 2.3

---
# API-Fehler und Antworten

> Dieser Referenzartikel behandelt die verschiedenen Fehler und Server-Antworten, die bei der Verwendung der Braze API auftreten können, und wie Sie diese beheben können.

## Server-Antworten

Wenn Ihre POST-Nutzlast von unseren Servern akzeptiert wurde, erhalten Sie bei erfolgreichen Nachrichten die folgende Antwort:

```json
{
  "message" : "success"
}
```

Beachten Sie, dass „success" lediglich bedeutet, dass die RESTful-API-Nutzlast korrekt erstellt und an unseren Push-Benachrichtigungsdienst, E-Mail-Dienst oder andere Messaging-Dienste übermittelt wurde. Dies bedeutet nicht, dass die Nachrichten tatsächlich zugestellt wurden, da zusätzliche Faktoren die Zustellung der Nachricht verhindern könnten (beispielsweise könnte ein Gerät offline sein, das Push-Token könnte von den Servern von Apple abgelehnt werden, oder Sie könnten eine unbekannte Nutzer-ID angegeben haben).

Bei Endpunkten wie [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), die keine Nachrichten senden, bedeutet eine Erfolgsmeldung lediglich, dass Braze die Anfrage zur Verarbeitung erhalten hat. Wenn nach der Verarbeitung keine Übereinstimmung für den Alias gefunden wird, wird die Anfrage abgebrochen.

Wenn Ihre Nachricht erfolgreich ist, jedoch nicht schwerwiegende Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

Im Falle eines Erfolgs werden alle Nachrichten, die nicht von einem Fehler im `errors`-Array betroffen waren, weiterhin zugestellt. Wenn Ihre Nachricht einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Antworten für getrackte Sende-IDs

Analytics sind immer für Kampagnen verfügbar. Darüber hinaus sind Analytics für eine bestimmte Instanz des Kampagnenversands verfügbar, wenn die Kampagne als Broadcast gesendet wird. Wenn Tracking für eine bestimmte Kampagnen-Instanz verfügbar ist, erhalten Sie die folgende Antwort:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

Die angegebene Sende-ID kann als Parameter für den Endpunkt `/send/data_series` verwendet werden, um sendespezifische Analytics abzurufen.

## Fehler

Das Statuscode-Element einer Server-Antwort ist eine dreistellige Zahl, wobei die erste Ziffer des Codes die Klasse der Antwort definiert.

- Die **Klasse 2XX** des Statuscodes (nicht schwerwiegend) zeigt an, dass **Ihre Anfrage** erfolgreich empfangen, verstanden und akzeptiert wurde.
- Die **Klasse 4XX** des Statuscodes (schwerwiegend) weist auf einen **Client-Fehler** hin. In der Tabelle der schwerwiegenden Fehler finden Sie eine vollständige Liste der 4XX-Fehlercodes und Beschreibungen.
- Die **Klasse 5XX** des Statuscodes (schwerwiegend) weist auf einen **Server-Fehler** hin. Es gibt mehrere mögliche Ursachen – beispielsweise kann der Server, auf den Sie zugreifen möchten, die Anfrage nicht ausführen, der Server wird gerade gewartet und kann die Anfrage daher nicht ausführen, oder der Server hat ein hohes Verkehrsaufkommen. In diesem Fall empfehlen wir Ihnen, Ihre Anfrage mit exponentiellem Backoff zu wiederholen. Im Falle eines Vorfalls oder Ausfalls ist Braze nicht in der Lage, REST-API-Aufrufe, die während des Vorfallszeitraums fehlgeschlagen sind, erneut abzuspielen. Sie müssen alle Aufrufe, die während des Vorfallszeitraums fehlgeschlagen sind, selbst wiederholen.
  - Ein **502-Fehler** ist ein Fehler, der auftritt, bevor die Anfrage den Zielserver erreicht.
  - Ein **503-Fehler** bedeutet, dass die Anfrage den Zielserver zwar erreicht hat, wir die Anfrage aber nicht abschließen können, weil die Kapazität nicht ausreicht, ein Netzwerkproblem vorliegt oder Ähnliches.
  - Ein **504-Fehler** zeigt an, dass ein Server keine Antwort von einem anderen vorgelagerten Server erhalten hat.

### Schwerwiegende Fehler

Die folgenden Statuscodes und zugehörigen Fehlermeldungen werden zurückgegeben, wenn bei Ihrer Anfrage ein schwerwiegender Fehler auftritt.

{% alert warning %}
Alle folgenden Fehlercodes weisen darauf hin, dass keine Nachrichten gesendet werden.
{% endalert %}

| Fehlercode | Beschreibung |
|---|---|
| `5XX Internal Server Error` | Wiederholen Sie Ihre Anfrage mit exponentiellem Backoff.|
| `400 Bad Request` | Fehlerhafte Syntax.|
| `400 No Recipients` | Es gibt keine externen IDs oder Segment-IDs oder keine Push-Token in der Anfrage.|
| `400 Invalid Campaign ID` | Es wurde keine Messaging-API-Kampagne für Ihre angegebene Kampagnen-ID gefunden.|
| `400 Message Variant Unspecified` | Sie geben eine Kampagnen-ID an, aber keine Nachrichtenvarianten-ID.|
| `400 Invalid Message Variant` | Sie haben eine gültige Kampagnen-ID angegeben, aber die Nachrichtenvarianten-ID stimmt mit keiner Nachricht dieser Kampagne überein.|
| `400 Mismatched Message Type` | Sie haben für mindestens eine Ihrer Nachrichten eine Nachrichtenvariante des falschen Nachrichtentyps angegeben.|
| `400 Invalid Extra Push Payload` | Sie geben den Schlüssel `extra` entweder für `apple_push` oder `android_push` an, aber es handelt sich nicht um ein Wörterbuch.|
| `400 Max Input Length Exceeded` | Für `/users/track` wird dieser Fehler durch das Überschreiten der maximalen Anzahl von Objekten in einer einzelnen Anfrage verursacht. Das Limit hängt vom Rate-Limit-Modell ab: Für die meisten Kund:innen unterstützt jede Anfrage bis zu 75 Objekte insgesamt, verteilt auf `attributes`, `events` und `purchases`. Für Kund:innen mit älteren Rate-Limits unterstützt jedes Array bis zu 75 Objekte unabhängig voneinander. Weitere Informationen finden Sie unter [POST: Nutzer:innen erstellen und aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).|
| `400 The max number of external_ids and aliases per request was exceeded` | Verursacht durch den Aufruf von mehr als 50 externen IDs.|
| `400 The max number of ids per request was exceeded` | Verursacht durch den Aufruf von mehr als 50 externen IDs.|
| `400 No message to send` | Für die Nachricht ist keine Nutzlast angegeben.|
| `400 Slideup Message Length Exceeded` | Die Slideup-Nachricht enthält mehr als 140 Zeichen.|
| `400 Apple Push Length Exceeded` | Die JSON-Nutzlast ist größer als 1.912 Bytes.|
| `400 Android Push Length Exceeded` | Die JSON-Nutzlast ist größer als 4.000 Bytes.|
| `400 Bad Request` | `send_at`-Datetime kann nicht geparst werden.|
| `400 Bad Request` | In Ihrer Anfrage ist `in_local_time` auf „true" gesetzt, aber `time` ist in der Zeitzone Ihres Unternehmens bereits verstrichen.|
| `401 Unauthorized` | Ungültiger API-Schlüssel. Häufige Ursachen sind:<br><br>- **Fehlender oder fehlerhafter Autorisierung-Header.** Der Header-Wert muss `Bearer` gefolgt von einem Leerzeichen und dann Ihrem API-Schlüssel sein: `Authorization: Bearer YOUR-API-KEY`. Häufige Fehler sind das Weglassen von `Bearer`, das Weglassen des Schlüssels nach `Bearer` oder das Einschließen des Werts in Anführungszeichen.<br>- **Falscher REST-Endpunkt.** Sie senden die Anfrage an die falsche [Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Wenn sich Ihr Konto beispielsweise auf unserer EU-Instanz (`https://dashboard-01.braze.eu`) befindet, sollte die Anfrage an `https://rest.fra-01.braze.eu` gesendet werden.<br>- **Unzureichende Berechtigungen.** Jeder API-Schlüssel ist einem bestimmten Workspace und bestimmten Berechtigungen zugeordnet. Überprüfen Sie die Berechtigungen des Schlüssels unter **Einstellungen** > **API-Schlüssel** im Dashboard.<br>- **Falscher API-Schlüssel.** API-Schlüssel sind Workspace-spezifisch. Ein Schlüssel aus einem Workspace kann nicht zur Authentifizierung von Anfragen für einen anderen Workspace verwendet werden. |
| `403 Forbidden` | Der Tarifplan unterstützt dies nicht, oder das Konto ist aus anderen Gründen deaktiviert.|
| `403 Access Denied` | Der von Ihnen verwendete REST-API-Schlüssel verfügt nicht über ausreichende Berechtigungen. Häufige Ursachen sind: {::nomarkdown}<ul><li><strong>API-Schlüssel wurde vor dem Feature erstellt.</strong> Wenn der API-Schlüssel erstellt wurde, bevor ein Feature eingeführt wurde (z. B. Abo-Gruppen oder Kataloge), erbt der Schlüssel diese Berechtigungen nicht automatisch. Erstellen Sie einen neuen API-Schlüssel mit den erforderlichen Berechtigungen unter <strong>Einstellungen</strong> &gt; <strong>API-Schlüssel</strong>.</li><li><strong>Fehlende endpunktspezifische Berechtigung.</strong> Jeder API-Endpunkt erfordert einen bestimmten Berechtigungsumfang (z. B. <code>users.track</code> oder <code>email.status</code>). Überprüfen Sie, ob die Berechtigungen des Schlüssels mit dem aufgerufenen Endpunkt übereinstimmen.</li><li><strong>Abschließender Schrägstrich oder Tippfehler in der URL.</strong> Beispielsweise kann <code>/users/track/</code> (mit abschließendem Schrägstrich) anstelle von <code>/users/track</code> unerwartete Fehler verursachen.</li></ul>{:/}|
| `404 Not Found` | Ungültige URL. |
| `415 Unsupported Media Type` | Der `Content-Type`-Anfrage-Header fehlt oder ist falsch. Fügen Sie auf der Seite **Einstellungen** `Content-Type` mit dem Wert `application/json` hinzu. |
| `429 Rate Limited` | Rate-Limit überschritten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }