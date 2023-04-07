---
nav_title: "Objet WhatsApp"
article_title: Objet Envoi de messages WhatsApp
page_order: 15
page_type: reference
channel: WhatsApp
description: "Cet article de référence explique les différents composants de l’objet WhatsApp de Braze."

---

# Spécification d’objet WhatsApp

L’objet `whats_app` vous permet de modifier ou de créer des messages WhatsApp via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet WhatsApp

```json
{
    "app_id": (required, string) see App Identifier,
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "template_name": (required, string) the WhatsApp template name for the message,
    "template_language_code": (required, string) the language code of the WhatsApp template for the message,
    "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
    "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
    "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
    "header_image_uri" :(optional, string) URI to the header image, if the header is of type IMAGE in specified template_name
}
```

- [Identifiant d’application]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)

## Objet Variables d'en-tête

L’objet `header_variables` vous permet de spécifier des valeurs pour les variables d’en-tête dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.

```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Actuellement, seuls zéro ou une variable d'en-tête peuvent être spécifiés.


#### Exemple

```json
{
    "0": "Check it out!"
}
```

## Objet Variables du corps

L’objet `body_variables` vous permet de spécifier des valeurs pour les variables du corps dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.
```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

#### Exemple

```json
{
    "0": "Check it out!",
    "1": "It's pretty neat."
}
```

## Objet Variables de bouton

L’objet `button_variables` vous permet de spécifier des valeurs pour les variables du bouton dans le modèle WhatsApp. Chaque clé est l’index de variable du modèle WhatsApp (indexé à zéro) à remplacer par la valeur spécifiée.

```json
{
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Actuellement, une seule variable de bouton peut être spécifiée, à savoir le composant de chemin d’une URL d’appel à l’action. L’index de variable doit correspondre à l’index du bouton d’URL CTA dans le modèle. Par exemple, si votre bouton CTA est le deuxième bouton de votre modèle, utilisez l’index de variable « 1 ».

#### Exemple

```json
{
    "1": "/marketing/promotion123"
}
```
