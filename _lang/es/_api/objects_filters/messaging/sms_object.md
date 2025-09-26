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
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.     
}
```

- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)
  - Cualquier `app_id` válido de una aplicación configurada en tu espacio de trabajo funcionará para todos los usuarios de tu espacio de trabajo, independientemente de si el usuario tiene la aplicación específica en su perfil o no.