---
nav_title: "Objeto de WhatsApp"
article_title: Objeto de mensajería WhatsApp
page_order: 15
page_type: reference
channel: WhatsApp
description: "Este artículo de referencia explica los distintos componentes del objeto Braze WhatsApp."

---

# Objeto WhatsApp

> El objeto `whats_app` te permite modificar o crear mensajes de WhatsApp a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

## Objeto WhatsApp

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message),
  "message": (required, object) message object specifying fields the required fields based on the specified message_type. See Message Types for field specifications.
}
```

- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)

### Tipos de mensaje

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

##### Objeto variables de cabecera

El objeto `header_variables` te permite especificar valores para las variables de cabecera de la plantilla de WhatsApp. Cada clave es el índice de la variable de la plantilla WhatsApp (índice cero) que hay que sustituir por el valor especificado.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Actualmente, solo se pueden especificar cero o una variable del encabezado.


###### Ejemplo

```json
{
  "0": "Check it out!"
}
```

##### Objeto variables corporales

El objeto `body_variables` te permite especificar valores para las variables del cuerpo de la plantilla de WhatsApp. Cada clave es el índice de la variable de la plantilla WhatsApp (índice cero) que hay que sustituir por el valor especificado.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### Ejemplo

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### Objeto de variables de botón

El objeto `button_variables` te permite especificar valores para las variables de los botones en la plantilla de WhatsApp. Cada clave es el índice de la variable de la plantilla WhatsApp (índice cero) que hay que sustituir por el valor especificado.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Actualmente, sólo se puede especificar una variable de botón, que es el componente de ruta de una URL de llamada a la acción. El índice de la variable debe coincidir con el índice del botón URL CTA de la plantilla. Por ejemplo, si tu botón CTA es el segundo botón de tu plantilla, utiliza el índice variable "1".

###### Ejemplo

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

###### Ejemplo

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

###### Ejemplo

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

##### Objeto botón

```json
{
  "text": (required, string) the text of the button
}
```

###### Ejemplo

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
