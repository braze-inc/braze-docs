---
nav_title: "Objeto WhatsApp"
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
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
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

### Mensajes de respuesta

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

#### list_response_message

El tipo `list_response_message` te permite enviar un mensaje basado en una lista en WhatsApp. Este tipo de mensaje incluye una lista de elementos con los que el destinatario puede interactuar.

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

#### Lista Sección Objeto

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### Lista Fila Objeto

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### Restricciones

- **list_sections**: Debe tener al menos una sección.
- **list_rows**: Se puede incluir un máximo de 10 filas en todas las secciones.
- **row_description**: Opcional para cada fila.

##### Ejemplo

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

El tipo `flow_response_message` te permite enviar un mensaje basado en flujo en WhatsApp. Este tipo de mensaje incluye un flujo interactivo que el destinatario puede completar.

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

##### Objeto Botón de flujo

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### Restricciones

- **flow_button**: Debe incluir tanto el pie de foto como `flow_id`.
- **pie de foto**: Máximo 20 caracteres.
- **flow_id**: Debe ser un ID de flujo publicado válido.

##### Ejemplo

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
