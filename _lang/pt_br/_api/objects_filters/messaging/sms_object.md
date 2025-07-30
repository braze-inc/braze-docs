---
nav_title: "Objeto SMS"
article_title: Objeto de envio de mensagens SMS
page_order: 10
page_type: reference
channel: SMS
description: "Este artigo de referência explica os diferentes componentes do objeto Braze SMS."

---
# Objeto SMS

> O objeto `sms` permite que você modifique ou crie mensagens SMS por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

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

- [Identificador do app]({{site.baseurl}}/api/identifier_types/)
  - Qualquer `app_id` válido de um aplicativo configurado em seu espaço de trabalho funcionará para todos os usuários em seu espaço de trabalho, independentemente de o usuário ter ou não o aplicativo específico em seu perfil.