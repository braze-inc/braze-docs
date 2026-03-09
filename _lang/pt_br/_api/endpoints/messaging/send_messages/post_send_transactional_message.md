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
O e-mail de transação está atualmente disponível como parte de alguns pacotes Braze. Entre em contato com seu gerente de sucesso do cliente da Braze para mais detalhes.
{% endalert %}

Semelhante ao [endpoint Send triggered campaign (Enviar campanha disparada)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), esse tipo de campanha permite que você abrigue o conteúdo da mensagem dentro do dashboard do Braze e, ao mesmo tempo, dite quando e para quem a mensagem será enviada por meio de sua API. Ao contrário do ponto de extremidade Send triggered campaign (Enviar campanha disparada), que aceita um público ou segmento de mensagens para o qual enviar mensagens, uma solicitação a esse ponto de extremidade deve especificar um único usuário por meio de `external_user_id` ou `user_alias`, pois esse tipo de campanha foi criado para o envio de mensagens 1:1 de alertas, como confirmações de pedidos ou redefinições de senha.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `transactional.send`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

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
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Opcional | String |  Uma string compatível com Base64. Validado com o seguinte regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Este campo opcional permite que você passe um identificador interno para este envio específico, que é incluído em eventos enviados do postback de evento HTTP Transacional. Quando passado, este identificador também é usado como uma chave de deduplicação, que a Braze armazena por 24 horas. <br><br>Passar o mesmo identificador em outra solicitação não resulta em uma nova instância de envio pela Braze por 24 horas.|
|`trigger_properties`|Opcional|Objeto|Consulte [propriedades do disparador]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Pares de chave-valor de personalização que se aplicam ao usuário nesta solicitação. |
|`recipient`|Obrigatória|Objeto| O usuário para o qual você está direcionando esta mensagem. Pode conter `attributes` e um único `external_user_id` ou `user_alias`.<br><br>Observe que se você fornecer um ID de usuário externo que não existe na Braze, passar quaisquer campos para o objeto `attributes` cria este perfil de usuário na Braze e envia esta mensagem para o usuário recém-criado. <br><br>Se você enviar várias solicitações para o mesmo usuário com dados diferentes no objeto `attributes`, os atributos `first_name`, `last_name` e `email` são atualizados de forma síncrona e templateados em sua mensagem. Os atributos personalizados não têm essa mesma proteção, portanto, tenha cuidado ao atualizar um usuário por meio dessa API e ao passar diferentes valores de atributos personalizados em rápida sucessão.|
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

O endpoint de envio de e-mail transacional responde com o `dispatch_id` da mensagem, que representa a instância deste envio de mensagem. Esse identificador pode ser usado junto com eventos do postback do evento HTTP transacional para rastrear o status de um e-mail individual enviado a um único usuário.

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
| `The external reference has been queued.  Please retry to obtain send_id.` | O external_send_id foi criado recentemente, tente um novo external_send_id se você pretende enviar uma nova mensagem. |
| `Campaign does not exist` | O ID da campanha fornecido não corresponde a uma campanha existente. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | O ID da campanha fornecido corresponde a uma campanha arquivada. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | O ID da campanha fornecido corresponde a uma campanha pausada. |
| `campaign_id must be a string of the campaign api identifier` | O ID da campanha fornecido não é um formato válido. |
| `Error authenticating credentials` | A chave de API fornecida é inválida |
| `Invalid whitelisted IPs `| O endereço IP que está enviando a solicitação não está na lista de permissões de IP (se estiver sendo usada) |
| `You do not have permission to access this resource` | A chave de API usada não tem permissão para realizar essa ação |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A maioria dos endpoints na Braze tem uma implementação de limite de frequência que retorna um código de resposta 429 se você fizer muitas solicitações. O endpoint de envio transacional tem uma alocação horária paga medida em unidades (por exemplo, 50.000 unidades por hora, dependendo do seu pacote). Não há um limite de frequência separado por endpoint para este endpoint: você pode enviar além do seu volume alocado, mas apenas o volume alocado é coberto pelo SLA; solicitações acima dessa alocação ainda são enviadas, mas não são cobertas pelo SLA. As solicitações para este endpoint contam para o seu [limite geral de taxa de API externa]({{site.baseurl}}/api/api_limits/). Se você exceder esse limite (por exemplo, 250.000 solicitações por hora em todos os endpoints), a Braze retorna 429 e limita as solicitações até que o limite seja redefinido. A contagem de volume transacional é redefinida a cada hora. Entre em contato com o suporte da Braze se precisar de mais informações sobre essa funcionalidade.

## Postback de evento HTTP transacional

{% multi_lang_include http_event_postback.md %}

{% endapi %}