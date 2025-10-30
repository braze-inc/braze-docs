---
nav_title: Rastreamento de e-mails transacionais
article_title: Rastreamento de e-mails transacionais
page_order: 1
description: "Este artigo de referência aborda como configurar o rastreamento em tempo real para campanhas de e-mail transacionais."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Rastreamento de e-mails transacionais

> Esta página descreve como configurar o rastreamento em tempo real para [campanhas de e-mail transacionais]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/). Para obter mais informações sobre o endpoint em si, consulte [Enviar e-mails transacionais usando a entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Quando você envia e-mails transacionais, como confirmações de pedidos ou redefinições de senha, é essencial saber se eles chegam aos seus clientes. Com os postbacks de eventos HTTP transacionais do Braze, você obterá insights em tempo real sobre o status de cada e-mail transacional, para que possa agir rapidamente se houver algum problema.

Use esse recurso para:

- **Monitore seus e-mails em tempo real:** Veja imediatamente se as mensagens são enviadas, processadas, entregues ou se encontram problemas.
- **Responda proativamente:** Tente novamente as mensagens, mude para outro canal, como SMS, ou use sistemas de fallback para garantir que suas comunicações sejam entregues.

## Rastreamento de seus e-mails transacionais

{% multi_lang_include http_event_postback.md %}


