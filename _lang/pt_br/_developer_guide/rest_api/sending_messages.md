---
nav_title: Enviar mensagens
article_title: Envio de mensagens usando a API REST
page_order: 1
page_type: reference
description: "Este artigo de referência cobre as duas maneiras de enviar mensagens programaticamente usando a API REST da Braze."
---

# Envio de mensagens usando a API REST

> Você pode enviar mensagens do seu backend em tempo real usando dois endpoints diferentes da Braze. Cada um tem uma forma de requisição diferente: um requer o conteúdo completo da mensagem na requisição; o outro requer um ID de campanha e envia o conteúdo definido no dashboard.

Essa abordagem funciona com qualquer canal de envio de mensagens suportado pela API (WhatsApp, e-mail, SMS, push, Cartões de Conteúdo, webhooks e mais).

## Duas maneiras de enviar

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **ID da campanha** | Opcional. Omitir para enviar sem rastreamento de campanha do dashboard, ou fornecer um ID de campanha da API mais `message_variation_id` em cada mensagem para rastrear no dashboard. | Necessário. |
| **Conteúdo das mensagens** | Você deve incluir um objeto `messages` na requisição (por exemplo, `messages.whats_app`, `messages.email`). | Não aceito. O conteúdo da mensagem é definido na campanha no dashboard da Braze. |
| **Caso de uso** | Envie uma mensagem com o conteúdo totalmente especificado na requisição da API. | Dispare uma campanha pré-construída (conteúdo no dashboard) para destinatários específicos via API. |

Para detalhes completos da requisição e resposta, veja as referências de endpoint [Enviar mensagens imediatamente (somente API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) e [Enviar campanhas usando entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

---

## Opção 1: Enviar com conteúdo da mensagem na requisição (`/messages/send`)

Use este endpoint quando quiser especificar o conteúdo completo da mensagem na requisição da API. Você **deve** incluir um objeto `messages` (por exemplo, `messages.whats_app`, `messages.email` ou `messages.sms`). Você pode omitir `campaign_id` para enviar sem rastreamento de campanha, ou incluir um ID de campanha da API e `message_variation_id` em cada mensagem para rastrear envios no dashboard (veja a [referência do endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para detalhes).

**Requerido:** Chave de API com a permissão `messages.send`.

{% alert important %}
Cada destinatário em `external_user_ids` deve já existir no Braze. Para criar usuários como parte de um envio, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) primeiro, ou use [Opção 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (campanha acionada por API) em vez disso.
{% endalert %}

### Exemplo: Mensagem de modelo do WhatsApp

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Para a especificação completa do objeto WhatsApp, veja [objeto WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
O endpoint `/messages/send` suporta apenas modelos do WhatsApp com cabeçalhos de TEXTO ou IMAGEM. Para tipos de cabeçalho de DOCUMENTO, VÍDEO ou outros tipos de mídia, use o [endpoint de campanha acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) ou o painel do Braze em vez disso.
{% endalert %}

### Exemplo: E-mail

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Para outros canais, veja [objetos de envio de mensagens]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Opção 2: Dispare uma campanha com conteúdo no painel (`/campaigns/trigger/send`)

Use este endpoint quando o conteúdo da mensagem for construído no painel do Braze (campanha acionada por API). Você envia um **obrigatório** `campaign_id` e destinatários; você não envia um `messages` objeto.

**Requerido:** Chave de API com a permissão `campaigns.trigger.send`.

### Etapa 1: Crie uma campanha acionada por API

1. No painel do Braze, acesse **Envio de Mensagens** > **Campanhas**.
2. Selecione **Criar Campanha**, depois **Campanha Acionada por API** (não "Campanha API").
3. Adicione seu canal de mensagem (WhatsApp, e-mail, SMS, etc.) e construa o conteúdo da mensagem no painel.
4. Observe o **ID da Campanha** (e **ID de Envio** se você usar várias variantes de mensagem). Você usará isso na solicitação da API.

Para mais informações sobre como construir campanhas acionadas por API, veja [entrega acionada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

### Etapa 2: Dispare a campanha via API

Envie uma solicitação POST para `/campaigns/trigger/send` com `campaign_id` e `recipients` (ou `broadcast`/`audience`). Não inclua um `messages` objeto—o conteúdo vem da campanha.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Para o corpo completo da solicitação (incluindo `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), consulte a referência do endpoint [Enviar campanhas usando entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body).

---

## Verifique sua integração

1. Envie uma solicitação usando uma das opções acima, com seu próprio ID de usuário como destinatário.
2. Confirme se a mensagem foi entregue.
3. Se estiver usando a Opção 2, verifique a campanha no dashboard do Braze para confirmar que o envio foi registrado.

## Considerações

- Use os recursos de [personalização do Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para adaptar o conteúdo onde for suportado.
- Garanta que seu envio de mensagens esteja em conformidade com as regulamentações relevantes e inclua opções de cancelamento e avisos de privacidade exigidos.
- Para mais endpoints (agendamento, gatilhos do Canvas, etc.), consulte [Endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/).
