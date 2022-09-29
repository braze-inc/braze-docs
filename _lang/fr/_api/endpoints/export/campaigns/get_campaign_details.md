---
nav_title: "GET : Informations relatives à la campagne"
article_title: "GET : Informations relatives à la campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Obtenir les informations relatives à la campagne."

---
{% api %}
# Endpoint Informations relatives à la campagne
{% apimethod get %}
/campaigns/details
{% endapimethod %}

Cet endpoint vous permet de récupérer des informations pertinentes sur une campagne spécifique, qui peuvent être identifiées par le `campaign_id`. Si vous souhaitez récupérer les données de Canvas, reportez-vous à l’endpoint [Informations relatives au Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Limite de débit

{% include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre     | Requis | Type de données | Description             |
| ------------- | -------- | --------- | ----------------------- |
| `campaign_id` | Requis      | Chaîne de caractères    | Voir [Identifiant API de campagne]({{site.baseurl}}/api/identifier_types/).<br><br> Le `campaign_id` pour les campagnes API se trouvent sur la page **Developer Console (Console du développeur)** et la page **Campaign Details (Informations relatives à la campagne)** dans votre tableau de bord, sinon vous pouvez utiliser l’[endpoint Liste de campagnes](#campaign-list-endpoint).   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponses

### Réponse API de l’endpoint Informations relatives à la campagne

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) date created as ISO 8601 date,
    "updated_at" : (string) date last updated as ISO 8601 date,
    "archived": (boolean) whether this campaign is archived,
    "draft": (boolean) whether this campaign is a draft,
    "name" : (string) campaign name,
    "description" : (string) campaign description,
    "schedule_type" : (string) type of scheduling action,
    "channels" : (array) list of channels to send via,
    "first_sent" : (string) date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) date and hour of last sent as ISO 8601 date,
    "tags" : (array) tag names associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) channel type of the message (as in, "email", "ios_push", "webhook", "content_card", "in-app_message", "sms"),
            "name": (string) name of the message in the dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) conversion event behaviors assigned to the campaign, see the following conversions behavior section.
}
```

### Messages

La réponse `messages` contiendra des informations sur chaque message. Voici des exemples de réponses de message pour chaque canal :

#### Canaux de notification push

```json
{
    "channel": (string) description of the channel, such as "ios_push" or "android_push"
    "alert": (string) alert body text,
    "extras": (hash) any key-value pairs provided
}
```

#### Canal d’e-mail

```json
{
    "channel": "email",
    "subject": (string) subject,
    "body": (string) HTML body,
    "from": (string) from address and display name,
    "reply_to": (string) reply-to for message, if different than "from" address,
    "title": (string) name of the email,
    "extras": (hash) any key-value pairs provided
}
```

#### Canal de message in-app

```json
{
    "type": (string) description of in-app message type, such as "survey",
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) display text for the header of the survey,
                    }
                "choices": [
                    {
                       "choice_id": (string) choice identifier,
                       "text": (string) display text, 
                       "custom_attribute_key": (string) custom attribute key, 
                       "custom_attribute_value": (sting) custom attribute value,
                       "deleted": (boolean) deleted from live campaign, 
                    },
                    ...
                ]
            }
        ]
    }
}
```

#### Canal de carte de contenu

```json
{
    "channel": "content_cards",
    "name": (string) name of variant,
    "extras": (hash) any key-value pairs provided; only present if at least one key-value pair has been set
}
```

#### Canal de webhook

```json
{
    "channel": "webhook",
    "url": (string) URL for webhook,
    "body": (string) payload body,
    "type": (string) body content type,
    "headers": (hash) specified request headers,
    "method": (string) HTTP method (e.g., "POST" or "GET"),
}
```

#### Canal SMS

```json
{
  "channel": "sms",
  "body": (string) payload body,
  "from": (string) list of numbers associated with the subscription group,
  "subscription_group_id": (string) API id of the subscription group targeted in the SMS message
}
```

#### Messages de contrôle

```json
{
    "channel": (string) description of the channel that the control is for,
    "type": "control"
}
```

### Comportements de conversion

Le tableau `conversion_behaviors` contiendra des informations sur chaque comportement relatif aux événements de conversion défini pour la campagne. Ces comportements sont dans l’ordre défini par la campagne. Par exemple, l’événement de conversion A sera le premier élément du tableau, l’événement de conversion B sera le deuxième, etc. Les listes suivantes présentent des exemples de comportement relatif aux événements de conversion :

#### Clique sur l’e-mail

```json
{
    "type": "Clicks Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Ouvre l’e-mail

```json
{
    "type": "Opens Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Achète (tout achat)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours
}
```

#### Achète (produit spécifique)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "product": (string) name of the product, i.e., - "Feline Body Armor"
}
```

#### Effectue un événement personnalisé

```json
{
    "type": "Performs Custom Event",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "custom_event_name": (string) name of the event, i.e., - "Used Feline Body Armor"
}
```

#### Met à niveau l’application

```json
{
    "type": "Upgrades App",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

#### Utilise l’application

```json
{
    "type": "Starts Session",
    "window": (integer) number of seconds during which the user can convert on this event, i.e., - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e., - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
