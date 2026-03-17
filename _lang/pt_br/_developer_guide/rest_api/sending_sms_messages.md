---
nav_title: Enviar mensagens SMS
article_title: Envio de mensagens SMS usando a API REST
page_order: 2
page_type: reference
description: "Este artigo de referência explica como enviar mensagens SMS usando a API REST do Braze e uma campanha de API."
channel:
  - SMS
---

# Envio de mensagens SMS usando a API REST

> Use a API REST do Braze para enviar mensagens SMS transacionais do seu backend em tempo real. Essa abordagem permite que você construa um serviço que envia mensagens SMS programaticamente enquanto rastreia a análise de entrega junto com suas outras campanhas e Canvases no dashboard do Braze.

Isso pode ser especialmente útil para mensagens transacionais de alto volume, onde o conteúdo é definido em seus sistemas de backend. Por exemplo, você pode notificar os consumidores quando eles receberem uma mensagem de outro usuário, convidando-os a visitar seu site e verificar sua caixa de entrada.

Com essa abordagem, você pode:

- Disparar mensagens SMS do seu backend em tempo real.
- Rastrear análises junto com todas as suas campanhas e Canvases de marketing.
- Ampliar o caso de uso com recursos adicionais do Braze, como atrasos de mensagens, redirecionamento de acompanhamento e testes A/B.
- Opcionalmente, mude para [entrega acionada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) para definir seus modelos de mensagem no dashboard do Braze enquanto ainda dispara envios do seu backend.

Para enviar uma mensagem SMS através da API REST, você precisa configurar uma campanha de API no dashboard do Braze, e então usar o [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint para enviar a mensagem.

## Pré-requisitos

Para completar este guia, você precisa:

| Requisito | Descrição |
| --- | --- |
| Chave da API REST do Braze | Uma chave com a permissão `messages.send`. Para criar uma, vá para **Configurações** > **APIs e Identificadores** > **Chaves de API**. |
| Grupo de inscrição SMS | Um grupo de inscrição SMS configurado no seu espaço de trabalho Braze. |
| Serviço de backend | Um serviço de backend ou ambiente de script capaz de fazer requisições HTTP POST para a API REST do Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 1: Criar uma campanha de API

1. No painel do Braze, acesse **Envio de Mensagens** > **Campanhas**.
2. Selecione **Criar Campanha**, depois selecione **Campanhas de API**.
3. Digite um nome e descrição para sua campanha, como "notificação de mensagem SMS".
4. Adicione tags relevantes para identificação e rastreamento.
5. Selecione **Adicionar Canal de Envio de Mensagens**, depois selecione **SMS**.
6. Anote o **ID da Campanha** e o **ID da Variação da Mensagem** exibidos na página da campanha. Você precisará de ambos os valores ao construir sua solicitação de API.

## Etapa 2: Envie uma mensagem SMS usando a API

Construa uma solicitação POST para o [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint. Inclua o ID da campanha, o ID do usuário externo do destinatário e o conteúdo do SMS na carga útil da solicitação.

{% alert important %}
Cada destinatário referenciado em `external_user_ids` deve já existir no Braze. Envios apenas de API não criam novos perfis de usuário. Se você precisar criar usuários como parte de um envio, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) primeiro, ou use uma [campanha acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) em vez disso.
{% endalert %}

### Exemplo de solicitação

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Substitua `YOUR_REST_ENDPOINT` pela [URL do endpoint REST]({{site.baseurl}}/api/basics/#endpoints) para seu espaço de trabalho.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Substitua os valores de espaço reservado pelos seus IDs reais. O campo `body` suporta [personalização Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), para que você possa adaptar o conteúdo da mensagem para cada destinatário. Para a lista completa de parâmetros suportados pelo objeto de envio de SMS, veja [objeto SMS]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

Após construir a solicitação, envie a solicitação POST do seu serviço de backend para a API REST do Braze.

## Etapa 3: Verifique sua integração

Após concluir a configuração, verifique sua integração:

1. Envie uma solicitação de API conforme descrito em [Etapa 2](#step-2-send-an-sms-message-using-the-api), usando seu próprio ID de usuário como destinatário.
2. Confirme se a mensagem SMS foi entregue ao seu telefone.
3. No dashboard do Braze, Acesse a página de resultados da campanha e confirme se o envio está registrado.
4. Monitore os resultados de perto à medida que você expande sua campanha.

## Considerações

- Confirme que suas campanhas de SMS estão em conformidade com as regulamentações relevantes e os requisitos da operadora. Inclua instruções de opt-out (como "Envie STOP para cancelar") em cada mensagem. Para saber mais, veja [leis e regulamentações de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) e [palavras-chave de aceitação e cancelamento]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/).
- Use os recursos de personalização do Braze [para adaptar o conteúdo de SMS]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para consumidores individuais, incluindo conteúdo dinâmico e dados específicos do usuário.
- A API REST do Braze oferece [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) adicionais para agendar mensagens, acionar campanhas e mais.
