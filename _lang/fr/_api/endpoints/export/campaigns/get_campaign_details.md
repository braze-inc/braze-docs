---
nav_title: "GET : Exporter les informations relatives à la campagne"
article_title: "GET : Exporter les informations relatives à la campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les informations relatives à la campagne."

---
{% api %}
# Exporter les informations relatives à la campagne
{% apimethod get %}
/campaigns/details
{% endapimethod %}

Utilisez cet endpoint pour récupérer des informations pertinentes sur une campagne spécifique, qui peuvent être identifiées par le `campaign_id`. Si vous souhaitez récupérer les données de Canvas, reportez-vous à l’endpoint [Exporter les informations relatives au Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Requis | String | Voir [identifiant API de campagne]({{site.baseurl}}/api/identifier_types/).<br><br> Le `campaign_id` pour les campagnes API se trouvent sur la page **Developer Console (Console du développeur)** et la page **Campaign Details (Informations relatives à la campagne)** dans votre tableau de bord, sinon vous pouvez utiliser l’[endpoint Exporter la liste des campagnes](#campaign-list-endpoint). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponses

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the date created as ISO 8601 date,
    "updated_at" : (string) the date last updated as ISO 8601 date,
    "archived": (boolean) whether this campaign is archived,
    "draft": (boolean) whether this campaign is a draft,
    "name" : (string) the campaign name,
    "description" : (string) the campaign description,
    "schedule_type" : (string) the type of scheduling action,
    "channels" : (array) the list of channels to send via,
    "first_sent" : (string) the date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) the date and hour of last sent as ISO 8601 date,
    "tags" : (array) the tag names associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) the channel type of the message, must be either email, ios_push, webhook, content_card, in-app_message, or sms,
            "name": (string) the name of the message in the dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) the conversion event behaviors assigned to the campaign, see the following conversions behavior section.
}
```

### Messages par canal

La réponse `messages` contiendra des informations sur chaque message. Voici des exemples de réponses de message pour chaque canal :

#### Notification push

```json
{
    "channel": (string) the description of the channel, such as "ios_push" or "android_push"
    "alert": (string) the alert body text,
    "extras": (hash) any key-value pairs provided
}
```

#### E-mail

```json
{
    "channel": "email",
    "subject": (string) the subject,
    "body": (string) the HTML body,
    "from": (string) the from address and display name,
    "reply_to": (string) the reply-to for message, if different than "from" address,
    "title": (string) the name of the email,
    "extras": (hash) any key-value pairs provided
}
```

#### Messages in-app

```json
{
    "type": (string) the description of in-app message type, such as "survey",
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) the display text for the header of the survey,
                    }
                "choices": [
                    {
                       "choice_id": (string) the choice identifier,
                       "text": (string) the display text, 
                       "custom_attribute_key": (string) the custom attribute key, 
                       "custom_attribute_value": (sting) the custom attribute value,
                       "deleted": (boolean) deleted from live campaign, 
                    },
                    ...
                ]
            }
        ]
    }
}
```

#### Cartes de contenu

```json
{
    "channel": "content_cards",
    "name": (string) the name of variant,
    "extras": (hash) any key-value pairs provided; only present if at least one key-value pair has been set
}
```

#### Webhook

```json
{
    "channel": "webhook",
    "url": (string) the URL for webhook,
    "body": (string) the payload body,
    "type": (string) the body content type,
    "headers": (hash) the specified request headers,
    "method": (string) the HTTP method, either POST or GET
}
```

#### SMS

```json
{
  "channel": "sms",
  "body": (string) the payload body,
  "from": (string) the list of numbers associated with the subscription group,
  "subscription_group_id": (string) the API id of the subscription group targeted in the SMS message
}
```

#### Messages de contrôle

```json
{
    "channel": (string) the description of the channel that the control is for,
    "type": "control"
}
```

### Comportements de conversion

Le tableau `conversion_behaviors` contiendra des informations sur chaque comportement relatif aux événements de conversion défini pour la campagne. Ces comportements sont dans l’ordre défini par la campagne. Par exemple, l’événement de conversion A sera le premier élément du tableau, l’événement de conversion B sera le deuxième, etc. Les listes suivantes présentent des exemples de comportement relatif aux événements de conversion :

#### Clique sur l’e-mail

```json
{
    "type": "Clicks Email",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Ouvre l’e-mail

```json
{
    "type": "Opens Email",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Achète (tout achat)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Achète (produit spécifique)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "product": (string) the name of the product, i.e., - "Feline Body Armor"
}
```

#### Effectue un événement personnalisé

```json
{
    "type": "Performs Custom Event",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "custom_event_name": (string) the name of the event, i.e., - "Used Feline Body Armor"
}
```

#### Met à niveau l’application

```json
{
    "type": "Upgrades App",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

#### Utilise l’application

```json
{
    "type": "Starts Session",
    "window": (integer) the number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
