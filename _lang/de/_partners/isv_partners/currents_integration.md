---
nav_title: Custom Currents Anschluss
alias: /currents_connector/
hidden: true
---

# Benutzerdefinierter Partner Currents-Anschluss

## Serialisierung und Datenformat

Das Zieldatenformat ist JSON über HTTPS. Die Ereignisse werden standardmäßig in Stapeln von 100 Ereignissen gruppiert und als JSON-Array mit allen Ereignissen an den Endpunkt gesendet. Die Lose werden in folgendem Format verschickt:

`{"events": [event1, event2, event3, etc...]}`

Es gibt ein JSON-Objekt der obersten Ebene mit dem Schlüssel "events", das auf ein Array weiterer JSON-Objekte verweist, die jeweils ein einzelnes Ereignis repräsentieren.

Die folgenden Beispiele beziehen sich auf _einzelne_ Ereignisse (so wie sie Teil eines größeren Arrays von JSON-Objekten wären, wobei jedes JSON-Objekt ein einzelnes Ereignis im Stapel darstellt).

### Ereignisse im Zusammenhang mit der Kampagne

Hier finden Sie einige Beispiel-Ereignis-Payloads für verschiedene Ereignisse, wie sie erscheinen würden, wenn sie mit einer Kampagne verbunden wären:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Canvas-assoziierte Ereignisse

Hier sind einige Beispiel-Nutzdaten für verschiedene Ereignisse, wie sie erscheinen würden, wenn sie mit einem Canvas verbunden wären:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Andere Ereignisse

Hier finden Sie einige Beispiel-Ereignis-Payloads für verschiedene andere Ereignisse, die weder mit Kampagnen noch mit Canvases verbunden sind:

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentifizierung

Falls erforderlich, erfolgt die Authentifizierung durch Übergabe eines Tokens im HTTP `Authorization` Header über das `Bearer` Autorisierungsschema, wie in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) beschrieben. In Zukunft kann Braze den `Authorization` Header verwenden, um ein benutzerdefiniertes (für Braze einzigartiges) Schlüssel-Wert-Paar-Autorisierungsschema zu implementieren, das [RFC 7235](https://tools.ietf.org/html/rfc7235) entspricht (so funktioniert zum Beispiel das benutzerdefinierte Autorisierungsschema von AWS).

Gemäß RFC 6750 sollte das Token ein Base64-kodierter Wert von mindestens einem Zeichen sein. Eine bemerkenswerte Besonderheit von RFC 6750 ist, dass das Token neben den normalen Base64-Zeichen auch die folgenden Zeichen enthalten darf: '-', '.', '_' und '~'. Partner und Kunden können frei entscheiden, ob sie diese Zeichen in ihren Token aufnehmen wollen oder nicht. Beachten Sie, dass Kunden dieses Token in Base64-Form bereitstellen müssen; Braze führt diese Kodierung nicht auf unserer Seite durch.

Gemäß RFC 6750 wird der Header, falls vorhanden, in folgendem Format erstellt:

`"Authorization: Bearer " + <token>`

Wenn das API-Token zum Beispiel `0p3n5354m3==` lautet, sieht der Authorization-Header wie folgt aus:

`Authorization: Bearer 0p3n5354m3==`

## Versionierung

Alle Anfragen von unseren integrierbaren HTTP-Konnektoren werden mit einem benutzerdefinierten Header gesendet, der die Version der Currents-Anfrage angibt, die gestellt wird:

`Braze-Currents-Version: 1`

Die Version wird immer `1` sein, es sei denn, wir nehmen schwerwiegende, rückwärtskompatible Änderungen an der Nutzlast oder der Semantik der Anfrage vor. Wir erwarten nicht, dass wir diese Zahl sehr oft erhöhen werden, wenn überhaupt.

Einzelne Ereignisse werden denselben Evolutionsregeln folgen wie unsere bestehenden S3 Avro-Schemata für den Export von Strömungsdaten. Das heißt, die Felder jedes Ereignisses sind garantiert abwärtskompatibel mit früheren Versionen der Ereignis-Payloads gemäß der Avro-Definition von Abwärtskompatibilität, einschließlich der folgenden Regeln:

- Bestimmte Ereignisfelder haben im Laufe der Zeit garantiert immer den gleichen Datentyp.
- Alle neuen Felder, die im Laufe der Zeit zu den Nutzdaten hinzugefügt werden, müssen von allen Parteien als optional betrachtet werden.
- Erforderliche Felder werden nie entfernt.

## Fehlerbehandlung und Wiederholungsmechanismus

Im Falle eines Fehlers stellt Braze die Anfrage in eine Warteschlange und wiederholt sie auf der Grundlage des empfangenen HTTP-Rückgabecodes. Jeder HTTP-Fehlercode, der unten nicht aufgeführt ist, wird als HTTP 5XX-Fehler behandelt.

{% alert important %}
Wenn unser Wiederholungsmechanismus mehr als 24 Stunden lang keine Ereignisse an ihren Endpunkt liefern kann, kommt es zu einem Datenverlust.
{% endalert %}

Die folgenden HTTP-Statuscodes werden von unserem Connector-Client erkannt:
- **2XX** \- Erfolg
  - Die Ereignisdaten werden nicht erneut gesendet.<br><br>
- **5XX** \- Serverseitiger Fehler
  - Die Ereignisdaten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn die Daten nicht innerhalb von 24 Stunden erfolgreich gesendet werden, werden sie verworfen.<br><br>
- **400** \- Client-seitiger Fehler
  - Unser Connector hat mindestens ein fehlerhaftes Ereignis gesendet. Wenn dies der Fall ist, werden die Ereignisdaten in Stapel der Größe 1 aufgeteilt und erneut gesendet. Alle Ereignisse in diesen Größe-1-Stapeln, die eine zusätzliche HTTP 400-Antwort erhalten, werden dauerhaft gelöscht. Partner und/oder Kunden werden gebeten, uns zu informieren, wenn sie dieses Problem bei sich entdecken.<br><br>
- **401** (Nicht autorisiert), **403** (Verboten), **404**
  - Der Connector wurde mit ungültigen Anmeldedaten konfiguriert. Die Ereignisdaten werden nach einer Verzögerung von 2 bis 5 Minuten erneut gesendet. Wenn der Kunde dieses Problem nicht innerhalb von 48 Stunden behebt, werden die Ereignisdaten gelöscht.<br><br>
- **413** \- Nutzlast zu groß
  - Die Ereignisdaten werden in kleinere Stapel aufgeteilt und erneut gesendet.<br><br>
- **429** \- Zu viele Anfragen
  - Zeigt eine Ratenbegrenzung an. Die Ereignisdaten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn die Daten nicht innerhalb von 24 Stunden erfolgreich gesendet werden, werden sie verworfen.