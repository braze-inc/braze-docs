---
nav_title: "Objeto do WhatsApp"
article_title: Objeto de envio de mensagens do WhatsApp
page_order: 15
page_type: reference
channel: WhatsApp
description: "Este artigo de referência explica os diferentes componentes do objeto Braze WhatsApp."

---

# Objeto do WhatsApp

> O objeto `whats_app` permite que você modifique ou crie mensagens do WhatsApp por meio dos nossos endpoints de [envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

## Objeto do WhatsApp

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}
```

- [Identificador do app]({{site.baseurl}}/api/identifier_types/)

### Tipos de mensagens

#### template_message

```json
{
  "template_name": (required, string) the WhatsApp template name for the message,
  "template_language_code": (required, string) the language code of the WhatsApp template for the message,
  "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
  "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
  "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
  "header_image_uri" :(optional, string) URI to the header image, if the header is of type IMAGE in specified template_name
}
```

##### Objeto de variáveis de cabeçalho

O objeto `header_variables` permite especificar valores para variáveis de cabeçalho no modelo do WhatsApp. Cada chave é o índice da variável de modelo do WhatsApp (indexado a partir de zero) a ser substituído pelo valor especificado.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Atualmente, apenas zero ou uma variável de cabeçalho pode ser especificada.


###### Exemplo

```json
{
  "0": "Check it out!"
}
```

##### Objeto de variáveis do corpo

O objeto `body_variables` permite especificar valores para variáveis de corpo no modelo do WhatsApp. Cada chave é o índice da variável de modelo do WhatsApp (indexado a partir de zero) a ser substituído pelo valor especificado.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### Exemplo

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### Objeto de variáveis de botão

O objeto `button_variables` permite especificar valores para variáveis de botão no modelo do WhatsApp. Cada chave é o índice da variável de modelo do WhatsApp (indexado a partir de zero) a ser substituído pelo valor especificado.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Atualmente, apenas uma variável de botão pode ser especificada, que é o componente de jornada de um URL de chamada para ação. O índice da variável deve corresponder ao índice do botão de URL do CTA no modelo. Por exemplo, se o seu botão de CTA for o segundo botão no seu modelo, use o índice da variável "1".

###### Exemplo

```json
{
  "1": "/marketing/promotion123"
}
```

### Mensagens de resposta

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

###### Exemplo

```json
{
  "body": "Check out our new deals at https://braze.com",
  "preview_url": true
}
```

#### text_image_response_message

```json
{
  "image_uri": (required, string) the uri of the image to send,
  "caption": (optional, string) the caption for the image being sent
}
```

###### Exemplo

```json
{
  "image_uri": "https://braze.com/promotion.jpg",
  "caption": "This won't last for long, check it out!"
}
```

#### quick_reply_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "header_image_uri": (optional, string) the URI of the image to send as the message header (only valid if header_text not present),
  "header_text": (optional, string) the text to send as the message header (only valid if header_image_uri not present),
  "footer": (optional, string) the footer of the message to send,
  "buttons": (required, array) array of Button objects. Will render in message based on order in array.
}
```

##### Objeto botão

```json
{
  "text": (required, string) the text of the button
}
```

###### Exemplo

```json
{
  "body": "Want to keep hearing from us?",
  "buttons": [
    {
      "text": "Yes!"
    },
    {
      "text": "No thanks"
    }
  ]
}
```

#### list_response_message

O tipo `list_response_message` permite que você envie uma mensagem baseada em lista no WhatsApp. Esse tipo de mensagem inclui uma lista de itens com os quais o destinatário pode interagir.

```json
{
  "header": (optional, string) the header of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "list": (required, object) the list object that contains:
    "list_button_text": (required, string) the text that will appear on the list button,
    "list_sections": (required, array) an array of List Section Objects
}
```

#### Objeto de seção de lista

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### Objeto de linha de lista

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### Restrições

- **list_sections**: Deve ter pelo menos uma seção.
- **list_rows**: Um máximo de 10 linhas pode ser incluído em todas as seções.
- **row_description**: Opcional para cada linha.

##### Exemplo

```json
{
  "body": "Here is a list of options to choose from:",
  "list": {
    "list_button_text": "Choose an option",
    "list_sections": [
      {
        "section_title": "Section 1",
        "list_rows": [
          {
            "row_title": "Option 1"
          },
          {
            "row_title": "Option 2",
            "row_description": "Description for Option 2"
          }
        ]
      },
      {
        "section_title": "Section 2",
        "list_rows": [
          {
            "row_title": "Option 3"
          },
          {
            "row_title": "Option 4"
          },
          {
            "row_title": "Option 5"
          }
        ]
      }
    ]
  }
}
```

#### flow_response_message

O tipo `flow_response_message` permite que você envie uma mensagem baseada em fluxo no WhatsApp. Esse tipo de mensagem inclui um fluxo interativo que o destinatário pode concluir.

```json
{
  "header_text": (optional, string) the header text of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "flow_button": (required, object) the flow button object that contains:
    "caption": (required, string) the text that will appear on the flow button,
    "flow_id": (required, string) the unique identifier of the WhatsApp Flow,
  "generate_custom_attribute": (optional, boolean) whether to save flow response on the user profile and generate a custom attribute upon responding to this flow message
}
```

##### Objeto do botão de fluxo

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### Restrições

- **flow_button**: Deve incluir a legenda e o endereço `flow_id`.
- **legenda**: Máximo de 20 caracteres.
- **flow_id**: Deve ser um ID de fluxo publicado válido.

##### Exemplo

```json
{
  "body": "Please complete your order details",
  "flow_button": {
    "caption": "Start Order",
    "flow_id": "594425479261596"
  },
  "generate_custom_attribute": true
}
```
