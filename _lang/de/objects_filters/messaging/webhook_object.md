---
nav_title: "Webhook-Objekt"
article_title: Webhook Messaging Objekt
page_order: 13
page_type: reference
channel: 
  - webhook
description: "Dieser Referenzartikel beschreibt das Braze Webhook-Objekt."

---

# Webhook-Objekt

> Mit dem Objekt `webhook` können Sie Webhook-Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) ändern oder erstellen.

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

Braze empfiehlt, für ein konsistentes und vorhersehbares Verhalten einen expliziten Wert für `Content-Type` im Feld `request_headers` anzugeben, da sich Absender und Server im Laufe der Zeit ändern können. Wenn für die Kopfzeile `Content-Type` kein Wert angegeben ist, wird dieser aus dem Text der Anfrage abgeleitet.
