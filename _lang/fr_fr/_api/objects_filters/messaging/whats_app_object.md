---
nav_title: "Objet WhatsApp"
article_title: Objet Envoi de messages WhatsApp
page_order: 15
page_type: reference
channel: WhatsApp
description: "Cet article de référence explique les différents composants de l’objet Braze WhatsApp."

---

# Objet WhatsApp

> L'objet `whats_app` vous permet de modifier ou de créer des messages WhatsApp via nos [points d'extrémité de messagerie.]({{site.baseurl}}/api/endpoints/messaging)

## Objet WhatsApp

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message),
  "message": (required, object) message object specifying fields the required fields based on the specified message_type. See Message Types for field specifications.
}
```

- [Identifiant d’application]({{site.baseurl}}/api/identifier_types/)

### Types de messages

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

##### Objet Variables d'en-tête

L’objet `header_variables` vous permet de spécifier des valeurs pour les variables d’en-tête dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Actuellement, seuls zéro ou une variable d'en-tête peuvent être spécifiés.


###### Exemple

```json
{
  "0": "Check it out!"
}
```

##### Objet Variables du corps

L’objet `body_variables` vous permet de spécifier des valeurs pour les variables du corps dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### Exemple

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### Objet Variables de bouton

L’objet `button_variables` vous permet de spécifier des valeurs pour les variables du bouton dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Actuellement, une seule variable de bouton peut être spécifiée, à savoir le composant de chemin d’une URL d’appel à l’action. L’index de variable doit correspondre à l’index du bouton d’URL CTA dans le modèle. Par exemple, si votre bouton CTA est le deuxième bouton de votre modèle, utilisez l’index de variable « 1 ».

###### Exemple

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

###### Exemple

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

###### Exemple

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

##### Objet bouton

```json
{
  "text": (required, string) the text of the button
}
```

###### Exemple

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
