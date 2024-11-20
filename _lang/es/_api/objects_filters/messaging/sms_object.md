---
nav_title: "Objeto SMS"
article_title: Objeto de mensajería SMS
page_order: 10
page_type: reference
channel: SMS
description: "Este artículo de referencia explica los distintos componentes del objeto SMS Braze."

---
# Objeto SMS

> El objeto `sms` te permite modificar o crear mensajes SMS a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

```json
{
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message.    
}
```

- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)