---
nav_title: "WhatsApp-Objekt"
article_title: WhatsApp Messaging Objekt
page_order: 15
page_type: reference
channel: WhatsApp
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten des Braze WhatsApp-Objekts."

---

# WhatsApp-Objekt

> Das Objekt `whats_app` ermöglicht es Ihnen, WhatsApp-Nachrichten über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) zu ändern oder zu erstellen.

## WhatsApp-Objekt

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}
```

- [App Kennung]({{site.baseurl}}/api/identifier_types/)

### Nachrichtentypen

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

##### Kopfzeilen-Variablen Objekt

Mit dem Objekt `header_variables` können Sie Werte für Kopfvariablen in der WhatsApp-Vorlage angeben. Jeder Schlüssel ist der Index der WhatsApp-Vorlagevariable (null-indiziert), die durch den angegebenen Wert ersetzt werden soll.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Derzeit können nur null oder eine Kopfvariable angegeben werden.


###### Beispiel

```json
{
  "0": "Check it out!"
}
```

##### Körper Variablen Objekt

Mit dem Objekt `body_variables` können Sie Werte für Body-Variablen in der WhatsApp-Vorlage angeben. Jeder Schlüssel ist der Index der WhatsApp-Vorlagevariable (null-indiziert), die durch den angegebenen Wert ersetzt werden soll.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### Beispiel

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### Schaltfläche variables Objekt

Mit dem Objekt `button_variables` können Sie Werte für Schaltflächenvariablen in der WhatsApp-Vorlage angeben. Jeder Schlüssel ist der Index der WhatsApp-Vorlagevariable (null-indiziert), die durch den angegebenen Wert ersetzt werden soll.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Derzeit kann nur eine Schaltflächenvariable angegeben werden, nämlich die Pfadkomponente einer Call-to-Action-URL. Der Variablenindex muss mit dem Index der CTA-URL-Schaltfläche in der Vorlage übereinstimmen. Wenn Ihre CTA-Schaltfläche zum Beispiel die zweite Schaltfläche in Ihrer Vorlage ist, verwenden Sie den Variablenindex "1".

###### Beispiel

```json
{
  "1": "/marketing/promotion123"
}
```

### Responsive Messages

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

###### Beispiel

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

###### Beispiel

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

##### Schaltfläche Objekt

```json
{
  "text": (required, string) the text of the button
}
```

###### Beispiel

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

Der Typ `list_response_message` ermöglicht es Ihnen, in WhatsApp eine listenbasierte Nachricht zu versenden. Dieser Nachrichtentyp enthält eine Liste von Artikeln, mit denen der Empfänger:in interagieren kann.

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

#### Liste Abschnitt Objekt

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### Liste Zeilenobjekt

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### Einschränkungen

- **list_sections**: Muss mindestens einen Abschnitt haben.
- **list_rows**: Es können maximal 10 Zeilen in allen Abschnitten enthalten sein.
- **row_description**: Optional für jede Zeile.

##### Beispiel

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

Der Typ `flow_response_message` ermöglicht es Ihnen, in WhatsApp eine flussbasierte Nachricht zu versenden. Dieser Nachrichtentyp enthält einen interaktiven Ablauf, den der Empfänger:in abschließen kann.

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

##### Flow Button Objekt

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### Einschränkungen

- **flow_button**: Sie müssen sowohl die Bildunterschrift als auch `flow_id` enthalten.
- **Bildunterschrift**: Maximal 20 Zeichen.
- **flow_id**: Muss eine gültige veröffentlichte Flow ID sein.

##### Beispiel

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
