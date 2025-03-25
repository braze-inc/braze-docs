---
nav_title: "POST: Envie e-mails de transação usando a entrega disparada por API"
article_title: "POST: Envie e-mails de transação usando a entrega disparada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint do Braze Send transactional e-mail messages using API-triggered delivery."

---

{% api %}
# Envie e-mails de transação usando a entrega disparada por API
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens transacionais únicas e imediatas a um usuário designado.

Esse endpoint é usado juntamente com a criação de uma [campanha de e-mail de transação]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) do Braze e o ID de campanha correspondente.

{% alert important %}
O e-mail de transação está atualmente disponível como parte de alguns pacotes Braze. Entre em contato com seu gerente de sucesso do cliente da Braze para saber mais.
{% endalert %}

Semelhante ao [endpoint Send triggered campaign (Enviar campanha disparada)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), esse tipo de campanha permite que você abrigue o conteúdo da mensagem dentro do dashboard do Braze e, ao mesmo tempo, dite quando e para quem a mensagem será enviada por meio de sua API. Ao contrário do ponto de extremidade Send triggered campaign (Enviar campanha disparada), que aceita um público ou segmento de mensagens para o qual enviar mensagens, uma solicitação a esse ponto de extremidade deve especificar um único usuário por meio de `external_user_id` ou `user_alias`, pois esse tipo de campanha foi criado para o envio de mensagens 1:1 de alertas, como confirmações de pedidos ou redefinições de senha.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `transactional.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='e-mail de transação' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `campaign_id` | Obrigatória | String | ID da campanha |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Opcional | String |  Uma string compatível com Base64. Validado com o seguinte regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Esse campo opcional permite que você passe um identificador interno para esse envio específico, que será incluído nos eventos enviados a partir do postback de evento HTTP transacional. Quando passado, esse identificador também será usado como uma chave de deduplicação, que a Braze armazenará por 24 horas. <br><br>Passar o mesmo identificador em outra solicitação não resultará em uma nova instância de um envio do Braze por 24 horas.|
|`trigger_properties`|Opcional|Objeto|Consulte [propriedades do disparador]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Pares de valores-chave de personalização que serão aplicados ao usuário nessa solicitação. |
|`recipient`|Obrigatória|Objeto| O usuário para o qual você está direcionando esta mensagem. Pode conter `attributes` e um único `external_user_id` ou `user_alias`.<br><br>Note que, se você fornecer um ID de usuário externo que ainda não exista na Braze, a passagem de qualquer campo para o objeto `attributes` criará esse perfil de usuário na Braze e enviará essa mensagem para o usuário recém-criado. <br><br>Se você enviar várias solicitações para o mesmo usuário com dados diferentes no objeto `attributes`, as atribuições `first_name`, `last_name` e `email` serão atualizadas de forma síncrona e modeladas na sua mensagem. Os atributos personalizados não têm essa mesma proteção, portanto, tenha cuidado ao atualizar um usuário por meio dessa API e ao passar diferentes valores de atributos personalizados em rápida sucessão.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Resposta

O endpoint "Enviar e-mail transacional" responderá com a mensagem `dispatch_id`, que representa a instância desse envio de mensagens. Esse identificador pode ser usado junto com eventos do postback do evento HTTP transacional para rastrear o status de um e-mail individual enviado a um único usuário.

### Exemplos de respostas

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Solução de problemas

O endpoint também pode retornar um código de erro e uma mensagem legível em alguns casos, a maioria dos quais são erros de validação. Aqui estão alguns erros comuns que você pode receber ao fazer solicitações inválidas.

| Erro | Solução de problemas |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | O ID de campanha fornecido não é de uma campanha transacional. |
| `The external reference has been queued.  Please retry to obtain send_id.` | O external_send_id foi criado recentemente, tente um novo external_send_id se estiver pretendendo enviar uma nova mensagem. |
| `Campaign does not exist` | O ID da campanha fornecido não corresponde a uma campanha existente. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | O ID da campanha fornecido corresponde a uma campanha arquivada. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | O ID da campanha fornecido corresponde a uma campanha pausada. |
| `campaign_id must be a string of the campaign api identifier` | O ID da campanha fornecido não é um formato válido. |
| `Error authenticating credentials` | A chave de API fornecida é inválida |
| `Invalid whitelisted IPs `| O endereço IP que está enviando a solicitação não está na lista de permissões de IP (se estiver sendo usada) |
| `You do not have permission to access this resource` | A chave de API usada não tem permissão para realizar essa ação |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A maioria dos endpoints no Braze tem uma implementação de limite de frequência que retornará um código de resposta 429 se você tiver feito muitas solicitações. O endpoint de envio transacional funciona de forma diferente - se você exceder o limite de frequência atribuído, nosso sistema continuará a ingerir as chamadas da API, retornará códigos de sucesso e enviará as mensagens; no entanto, essas mensagens podem não estar sujeitas ao SLA contratual do recurso. Entre em contato se precisar de mais informações sobre essa funcionalidade.

## Postback de evento HTTP transacional

Todos os e-mails de transação são complementados com postbacks de status de evento enviados como uma solicitação HTTP de volta ao URL especificado. Isso permite analisar o status da mensagem em tempo real e tomar providências para alcançar o usuário por outros canais se a mensagem não for entregue ou voltar para o sistema interno, caso a Braze esteja enfrentando um período com latência.

Para associar os eventos de entrada a uma instância específica de envio, você pode optar por capturar e armazenar o Braze `dispatch_id` retornado na [resposta da API](#example-response) ou passar seu próprio identificador para o campo `external_send_id`. Um exemplo de um valor que você pode optar por passar para esse campo pode ser um ID de pedido, em que, após concluir o pedido 1234, uma mensagem de confirmação de pedido é disparada para o usuário por meio do Braze e o endereço `external_send_id : 1234` é incluído na solicitação. Todos os postbacks de eventos seguintes, como `Sent` e `Delivered`, incluirão `external_send_id : 1234` na carga útil, permitindo confirmar que o usuário recebeu com êxito o e-mail de confirmação do pedido.

Para começar a usar o Postback de evento HTTP de transação, navegue até **Configurações** > **Preferências de e-mail** no dashboard da Braze e localize a seção **Postback de status de evento de transação**. Insira o URL desejado para receber postbacks.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essa página está localizada em **Manage Settings** > **Email Settings (** **Gerenciar configurações** > **Configurações** **de e-mail**).
{% endalert %}

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### Corpo do postback

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Status da mensagem

|  Status | Descrição |
| ------------ | ----------- |
| `sent` | Mensagem enviada com sucesso para um parceiro de envio de e-mail do Braze |
| `processed` | O parceiro de envio de e-mail recebeu e preparou com êxito a mensagem para envio ao provedor da caixa de entrada do usuário |
| `aborted` | O Braze não conseguiu enviar a mensagem com êxito porque o usuário não tinha um endereço de e-mail ou a lógica de abortamento do Liquid foi chamada no corpo da mensagem. Todos os eventos abortados incluem um campo `reason` no objeto de metadados, indicando por que a mensagem foi abortada |
|`delivered`| A mensagem foi aceita pelo provedor da caixa de entrada de e-mail do usuário |
|`bounced`| A mensagem foi rejeitada pelo provedor da caixa de entrada de e-mail do usuário. Todos os eventos de bounce incluem um campo `reason` no objeto de metadados que reflete o código de erro de bounce fornecido pelo provedor da caixa de entrada |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Exemplo de postback
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}
