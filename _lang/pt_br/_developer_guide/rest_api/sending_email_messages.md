---
nav_title: Enviar mensagens de e-mail
article_title: Enviando mensagens de e-mail usando a API REST
page_order: 3
page_type: reference
description: "Este artigo de referência explica como enviar mensagens de e-mail usando a API REST da Braze e uma campanha de API."
channel:
  - email
---

# Enviando mensagens de e-mail usando a API REST

> Use a API REST da Braze para enviar e-mails de transação a partir do seu backend em tempo real. Essa abordagem permite que você crie um serviço que envia e-mails de forma programática, enquanto rastreia a análise de dados de entrega junto com suas outras campanhas e canvas no dashboard da Braze.

Isso pode ser especialmente útil para envio de mensagens transacionais em que o conteúdo é definido nos seus sistemas de backend. Por exemplo, você pode notificar consumidores quando eles recebem uma mensagem de outro usuário, convidando-os a visitar seu site e verificar a caixa de entrada.

Com essa abordagem, você pode:

- Disparar e-mails a partir do seu backend em tempo real.
- Rastrear análise de dados junto com todas as suas campanhas e canvas gerenciados pelo marketing, incluindo aberturas, cliques e bounces.
- Usar dados de interação com mensagens para disparar mensagens subsequentes, como redirecionamento de acompanhamento.
- Estender o caso de uso com recursos adicionais da Braze, como postergação de mensagens e Testes A/B.
- Opcionalmente, mudar para [entrega disparada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) para definir seus modelos de e-mail no dashboard da Braze enquanto ainda dispara envios a partir do seu backend.

Para enviar um e-mail pela API REST, você precisa configurar uma campanha de API no dashboard da Braze e, em seguida, usar o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para enviar a mensagem.

## Pré-requisitos

Para concluir este guia, você precisa de:

| Requisito | Descrição |
| --- | --- |
| Chave da API REST da Braze | Uma chave com a permissão `messages.send`. Para criar uma, acesse **Configurações** > **APIs e Identificadores** > **Chaves de API**. |
| ID do app da Braze | O identificador do seu app dentro do seu espaço de trabalho. Para encontrá-lo, acesse **Configurações** > **APIs e Identificadores** e verifique a seção **Identificadores de app**. Esse valor é obrigatório no campo `app_id` do objeto de envio de mensagens de e-mail. Para saber mais, consulte [Identificador de app]({{site.baseurl}}/api/identifier_types/). |
| Conteúdo HTML do e-mail | O corpo HTML da sua mensagem de e-mail, preparado com antecedência. |
| Serviço de backend | Um serviço de backend ou ambiente de script capaz de fazer solicitações HTTP POST para a API REST da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 1: Criar uma campanha de API

1. No dashboard da Braze, acesse **Envio de mensagens** > **Campanhas**.
2. Selecione **Criar campanha** e, em seguida, selecione **Campanha de API**.
3. Insira um nome e uma descrição para sua campanha, como "Notificação de mensagem por e-mail".
4. Adicione tags relevantes para identificação e rastreamento.
5. Selecione **Adicionar canal de envio de mensagens** e, em seguida, selecione **E-mail**.
6. Anote o **ID da campanha** exibido na página da campanha. Você precisará desse valor ao construir sua solicitação de API. Opcionalmente, anote também o **ID da variação de mensagem** — inclua-o na sua solicitação se quiser atribuir estatísticas de envio a uma variação de mensagem específica.

## Etapa 2: Enviar um e-mail usando a API

Construa uma solicitação POST para o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Inclua o ID da campanha, o ID de usuário externo do destinatário e o conteúdo do e-mail na carga útil da solicitação.

{% alert important %}
Cada destinatário referenciado em `external_user_ids` já deve existir na Braze. Envios somente por API não criam novos perfis de usuário. Se você precisar criar usuários como parte de um envio, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) primeiro, ou use uma [campanha disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Exemplo de solicitação

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Substitua `YOUR_REST_ENDPOINT` pela [URL do endpoint REST]({{site.baseurl}}/api/basics/#endpoints) do seu espaço de trabalho.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

Substitua os valores de espaço reservado pelos seus IDs reais. O campo `from` deve usar o formato `"Nome de Exibição <email@endereco.com>"`. O campo `body` aceita HTML válido e suporta [personalização com Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), para que você possa adaptar o conteúdo do e-mail para cada destinatário. Para a lista completa de parâmetros suportados pelo objeto de envio de mensagens de e-mail, consulte [Objeto de e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

Após construir a solicitação, envie a solicitação POST do seu serviço de backend para a API REST da Braze.

## Etapa 3: Verificar sua integração

Após concluir a configuração, verifique sua integração:

1. Envie uma solicitação de API conforme descrito na [Etapa 2](#step-2-send-an-email-using-the-api), usando seu próprio ID de usuário como destinatário.
2. Confirme que o e-mail foi entregue na sua caixa de entrada.
3. No dashboard da Braze, acesse a página de resultados da campanha e confirme que o envio foi registrado.
4. Monitore os resultados de perto à medida que você escala sua campanha.

## Considerações

- Confirme que suas campanhas de e-mail estão em conformidade com as regulamentações relevantes, como GDPR e CAN-SPAM, incluindo as opções de cancelamento de inscrição e avisos de privacidade necessários. Para saber mais, consulte [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) e [Práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/).
- Use os [recursos de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) da Braze para adaptar o conteúdo do e-mail a consumidores individuais, incluindo conteúdo dinâmico e dados específicos do usuário.
- A API REST da Braze oferece [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) adicionais para agendar mensagens, disparar campanhas e muito mais.