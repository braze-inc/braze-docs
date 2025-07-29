---
nav_title: Seguimiento de correos electrónicos transaccionales
article_title: Seguimiento de correos electrónicos transaccionales
page_order: 1
description: "Este artículo de referencia explica cómo configurar el seguimiento en tiempo real para campañas de correo electrónico transaccionales."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Seguimiento de correos electrónicos transaccionales

> Esta página describe cómo configurar el seguimiento en tiempo real para [campañas de correo electrónico transaccionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/). Para más información sobre el propio punto final, consulta [Enviar correos electrónicos transaccionales utilizando la entrega desencadenada por la API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Cuando envías correos electrónicos transaccionales -como confirmaciones de pedidos o restablecimiento de contraseñas- es esencial saber si llegan a tus clientes. Con las devoluciones de eventos HTTP transaccionales Braze, obtendrás información en tiempo real sobre el estado de cada correo electrónico transaccional, para que puedas actuar con rapidez si surge algún problema.

Utiliza esta característica para:

- **Controla tus correos electrónicos en tiempo real:** Comprueba inmediatamente si los mensajes se envían, procesan, entregan o tienen problemas.
- **Responde proactivamente:** Reintenta los mensajes, cambia a otro canal como el SMS, o utiliza sistemas de reserva para asegurarte de que tus comunicaciones se entregan.

## Seguimiento de tus envíos por correo electrónico transaccionales

{% multi_lang_include http_event_postback.md %}


