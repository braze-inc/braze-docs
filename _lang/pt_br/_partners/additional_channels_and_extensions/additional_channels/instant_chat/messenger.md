---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Este artigo de referência descreve a parceria entre o Braze e o Facebook Messenger, uma das plataformas de envio de mensagens instantâneas mais populares do mundo."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [O Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) é uma das plataformas de envio de mensagens instantâneas mais populares do mundo, usada por quase um bilhão de usuários ativos por mês. Por meio dessa plataforma, as marcas podem criar chatbots envolventes para interagir de forma inteligente e automática com seus clientes.

A integração do Braze e do Facebook utiliza os recursos de webhooks, segmentação, personalização e disparo do Braze para enviar mensagens aos seus usuários no Facebook Messenger por meio da API da plataforma do Messenger. Um modelo personalizado de webhook do Facebook Messenger está incluído em nossa plataforma em **Templates** > **Webhook Templates**.

A plataforma Facebook Messenger é destinada a "mensagens não promocionais que facilitam uma transação pré-existente, fornecem outras ações de suporte ao cliente ou entregam conteúdo solicitado por uma pessoa". Para saber mais, consulte [as diretrizes da plataforma do Facebook](https://developers.facebook.com/docs/messenger-platform) e [os exemplos de casos de uso aceitáveis](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Pré-requisitos

Confirme o seguinte antes de prosseguir com a integração:
- O Facebook não permite o uso da plataforma Messenger para o envio de mensagens de marketing. 
- Será necessária a permissão explícita do usuário para o envio de mensagens da sua página. 
- Para enviar mensagens para usuários que não são usuários teste do seu aplicativo do Facebook, seu aplicativo precisará ser aprovado na [análise de aplicativos](https://developers.facebook.com/docs/messenger-platform/app-review) do Facebook.<br><br>

| Requisito| Origin| Acesso| Descrição|
| ---| ---| ---|
| Página do Messenger no Facebook| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Uma página do Facebook será usada como a identidade de seu bot. Quando as pessoas conversarem com seu app, elas verão o nome da página e a foto do perfil.|
| App do Facebook Messenger| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | O app do Facebook contém as configurações do seu bot do Messenger, incluindo os tokens de acesso.
| Revisão e aprovação do bot do app | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Quando estiver pronto para liberar seu bot para o público, você deverá enviá-lo ao Facebook para análise e aprovação. Esse processo de revisão nos permite garantir que seu bot do Messenger cumpra nossas políticas e funcione conforme o esperado antes de torná-lo disponível para todos no Messenger. |
| IDs de escopo de página (PSIDs) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | É necessário ter PSIDs de usuários para enviar mensagens no Facebook Messenger. Quando um usuário interage com o seu app via Messenger, o Facebook cria um PSID. Esse PSID pode ser enviado ao Braze como um atributo personalizado em forma de string.
| Token de acesso à página | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Esses tokens de acesso são semelhantes aos tokens de acesso do usuário, exceto pelo fato de fornecerem permissão às APIs que leem, gravam ou modificam os dados pertencentes a uma página do Facebook. Para obter um token de acesso à página, é necessário obter um token de acesso de usuário e solicitar o `manage_pagespermission`. Depois de ter o token de acesso do usuário, você obtém o token de acesso à página pela API Graph.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

A seguir, mostramos como configurar um webhook do Braze Facebook Messenger.
Para aqueles que precisam de ajuda adicional para configurar seu bot, um tutorial completo do bot Messenger e um código de exemplo podem ser encontrados no [repositório Braze GitHub](https://github.com/Appboy/appboy-fb-messenger-bot)!

### Etapa 1: Colete seus PSIDs

Para o envio de mensagens no Facebook Messenger, é necessário coletar os IDs específicos da página (PSIDs) dos seus usuários para identificá-los e interagir com eles de forma consistente. Os PSIDs não são os mesmos que a ID do Facebook do usuário. O Facebook cria esse identificador sempre que você envia uma mensagem a um cliente ou quando um cliente envia uma mensagem a você.

Os PSIDs podem ser encontrados usando um dos vários [pontos de entrada](https://developers.facebook.com/docs/messenger-platform/discovery) oferecidos pelo Facebook. Depois que o usuário enviar mensagens ao seu app ou realizar uma ação em uma conversa, como tocar em um botão ou enviar uma mensagem, o PSID dele será incluído na propriedade `sender.id` do evento do webhook, para que seu bot possa identificar quem realizou a ação.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Sempre que você enviar uma mensagem, seu PSID será incluído na propriedade `recipient.id` da solicitação para identificar quem deve receber a mensagem.

### Etapa 2: Enviar para o Braze como um atributo personalizado

Quando tiver certeza de que está recebendo PSIDs, coordene e compartilhe isso com seus desenvolvedores para enviar os PSIDs ao Braze como um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#custom-attributes). PSIDs são strings que podem ser acessadas por meio de uma [chamada de API](https://developers.facebook.com/docs/messenger-platform/reference/send-api).

### Etapa 3: Configure seu modelo de webhook

Em **Modelos e mídias**, acesse **Modelos de webhook** e escolha o **modelo de webhook do Facebook Messenger**.

1. Forneça um nome de modelo e adicione equipes e tags, conforme necessário.
2. Digite sua mensagem ou escolha um modelo de mensagem dentre [os disponibilizados pelo Facebook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). Você também pode escolher [o tipo](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) de mensagem ou [a tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags).
3. Inclua o PSID como um atributo personalizado. Isso pode ser feito usando o botão **+** azul e branco no canto da caixa **Request Body (Corpo da solicitação** ).
3. Adicione seu token de acesso à página no URL do webhook, substituindo `FACEBOOK_PAGE_ACCESS_TOKEN` pelo seu token.

#### Pré-visualização e teste de seu webhook

Antes de enviar sua mensagem, teste seu webhook. Certifique-se de que seu Messenger ID esteja salvo no Braze (ou encontre-o e teste como um usuário personalizado) e use a prévia para enviar a mensagem de teste:

![Guia Teste no modelo de webhook do Facebook Messenger mostrando que você pode fazer uma prévia da mensagem enviando-a para um usuário existente.]({% image_buster /assets/img_archive/fbm-test.png %})

Se a mensagem for recebida com êxito, você poderá definir as configurações de entrega.

## Usando esta integração

Depois de configurada, use essa integração para direcionar os usuários do Facebook Messenger. Se não estiver enviando mensagens usando os números de telefone dos usuários e planeja enviar mensagens do Messenger repetidamente, [crie um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) para todos os usuários para os quais o Messenger ID existe como um atributo personalizado e ative [o rastreamento de dados]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) para acompanhar as taxas de inscrição no Messenger ao longo do tempo. 

![Filtro de segmento "messenger_id" definido como "is not blank".]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Se você optar por não criar um segmento específico para assinantes do Messenger, certifique-se de incluir um filtro para o Messenger ID existente para evitar erros.

Você também pode usar outras segmentações para direcionar suas campanhas do Messenger e o restante do processo de criação de campanhas, como acontece com qualquer outra campanha.

