---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Este artigo de referência descreve a parceria entre o Braze e o Lob.com, que permite enviar malas diretas, cartões postais e cheques pelo correio."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) é um serviço on-line que permite o envio de mala direta para seus usuários.

_Essa integração é mantida pela Lob._

## Sobre a integração

Com essa integração, você pode:

- Envie cartas, cartões postais e cheques pelo correio usando os webhooks do Braze e a API do Lob.
- Compartilhe eventos do Lob com o Braze como atributos e eventos personalizados usando a transformação de dados do Braze e webhooks do Lob.

## Pré-requisitos

|Requisito| Descrição|
| ---| ---|
|Conta da Lob | É necessário ter uma conta Lob para aproveitar essa parceria. |
| Chave de API do Lob | A sua chave de API da Lob pode ser encontrada na seção de configurações, abaixo do seu nome, no dashboard da Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Envio de correio eletrônico usando webhooks do Braze

### Etapa 1: Escolha um ponto de extremidade Lob

Dependendo do que deseja fazer no Lob, você precisará usar o endpoint correspondente na solicitação HTTP do webhook. Para obter informações detalhadas sobre cada ponto de extremidade, consulte [a documentação de referência da API do Lob](https://lob.com/docs#intro).

| URL de base | Pontos de extremidade disponíveis |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 2: Crie seu modelo de webhook do Braze

Para criar um modelo de webhook Lob para ser usado em futuras campanhas ou canvas, acesse **Templates** > **Webhook Templates** no dashboard do Braze. 

Se quiser criar uma campanha única de webhook no Lob ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

Em seu novo modelo de webhook, preencha os seguintes campos:

- **URL do webhook**: `<LOB_API_ENDPOINT>`
- **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A Lob requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores chave, mas na guia **Settings (Configurações)**, você deve substituir o `<LOB_API_KEY>` pela sua chave de API do Lob. Essa chave deve incluir um ":" logo após a chave e ser codificada em base 64. 

- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
  - **Autorização**: Básico `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![O código do corpo da solicitação e o URL do webhook são mostrados na guia do criador de webhooks do Braze.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Corpo da solicitação

A seguir, um exemplo de corpo de solicitação para o endpoint de cartões postais da Lob. Esse corpo de solicitação seja fornecido no modelo básico da Lob na Braze, mas você deverá ajustar seus campos Liquid se desejar usar outros endpoints.

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### Etapa 3: veja uma prévia da sua solicitação

Nesse ponto, sua campanha deve estar pronta para ser testada e enviada. Verifique o dashboard do Lob e os registros de mensagens de erro do console de desenvolvedor do Braze se encontrar erros. Por exemplo, o erro a seguir foi causado por um cabeçalho de autenticação formatado incorretamente. 

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

![Um registro de erros de mensagens que mostra a hora, o nome do app, o canal e a mensagem de erro. A mensagem de erro inclui o alerta de mensagem e o código de status.]({% image_buster /assets/img_archive/error_log.png %})

## Compartilhamento de eventos usando webhooks do Lob 

[O Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview) permite que você crie e gerencie webhooks para automatizar o fluxo de dados de plataformas externas para o Braze. Cada transformação recebe um endpoint exclusivo, que pode ser usado por outras plataformas como destinos de seus webhooks.

{% alert important %}
O modelo de transformação de dados do Lob envia eventos usando seu [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que consome pontos de dados no Braze. Recomendamos definir um limite de frequência nas configurações do webhook do Lob, para evitar o consumo excessivo de dados.
{% endalert %}

### Etapa 1: Criar uma transformação no Braze

1. No Braze Dashboard, acesse **Data Settings** > **Data Transformations** e selecione **Create Transformation**.
2. Digite um nome curto e descritivo para sua transformação.
3. Em **Experiência de edição**, selecione **Usar um modelo**, procure o Lob e marque a caixa.
4. Quando terminar, selecione **Create Transformation (Criar transformação**). Você será redirecionado para o editor de transformação, que será usado na próxima etapa.

### Etapa 2: Preencha o modelo Lob

Com esse modelo, você pode transformar um de seus eventos Lob em um evento personalizado ou atributo que pode ser usado no Braze. Siga os comentários in-line para concluir a criação do modelo.

{% alert tip %}
Para obter informações detalhadas sobre a estrutura da carga útil do webhook do Lob, consulte [Lob: Uso de webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Etapa 3: Criar um webhook no Lob

1. Quando terminar de criar o modelo, selecione **Ativar** e copie o **URL do webhook** para a área de transferência.
2. No Lob, [crie um novo webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1) e use seu URL de webhook do Braze para receber o webhook.
