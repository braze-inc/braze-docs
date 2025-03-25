---
nav_title: "WhatsApp Objekt"
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
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message),
  "message": (required, object) message object specifying fields the required fields based on the specified message_type. See Message Types for field specifications.
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
