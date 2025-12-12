---
nav_title: "Objeto Webhook"
article_title: Objeto de mensajería webhook
page_order: 13
page_type: reference
channel: 
  - webhook
description: "Este artículo de referencia describe el objeto webhook Braze."

---

# Objeto Webhook

> El objeto `webhook` te permite modificar o crear mensajes webhook a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

Como mejor práctica, Braze recomienda proporcionar un valor explícito para `Content-Type` en el campo `request_headers` para un comportamiento coherente y predecible, ya que los remitentes y servidores pueden cambiar con el tiempo. Si no se especifica un valor para el encabezado `Content-Type`, se deducirá uno del cuerpo de la solicitud.
