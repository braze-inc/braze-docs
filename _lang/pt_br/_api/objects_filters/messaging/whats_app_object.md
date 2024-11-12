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
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message),
  "message": (required, object) message object specifying fields the required fields based on the specified message_type. See Message Types for field specifications.
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
