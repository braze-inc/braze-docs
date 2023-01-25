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

Utilisez cet endpoint pour récupérer des informations pertinentes sur une campagne spécifique, qui peuvent être identifiées par le `campaign_id`. Si vous souhaitez récupérer les données de Canvas, reportez-vous à l’endpoint [Informations relatives au Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre     | Requis | Type de données | Description             |
| ------------- | -------- | --------- | ----------------------- |
| `campaign_id` | Requis      | String    | Voir [Identifiant API de campagne]({{site.baseurl}}/api/identifier_types/).<br><br> Le `campaign_id` pour les campagnes API se trouvent sur la page **Developer Console (Console du développeur)** et la page **Campaign Details (Informations relatives à la campagne)** dans votre tableau de bord, sinon vous pouvez utiliser l’[endpoint Campaign List (Liste de campagnes)](#campaign-list-endpoint).   .|
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
    "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
    "created_at" : (string) la date de création en tant que date ISO 8601,
    "updated_at" : (string) la date de dernière mise à jour en tant que date ISO 8601,
    "archived": (boolean) si cette campagne est archivée ou non,
    "draft": (boolean) si cette campagne est un brouillon ou non,
    "name" : (string) le nom de la campagne,
    "description" : (string) la description de la campagne,
    "schedule_type" : (string) le type d’action de planification,
    "channels" : (array) la liste de canaux avec lesquels envoyer,
    "first_sent" : (string) la date et l’heure du premier envoi en tant que date ISO 8601,
    "last_sent" : (string) la date et l’heure du dernier envoi en tant que date ISO 8601,
    "tags" : (array) les noms de balise associés à la campagne,
    "messages": {
        "message_variation_id": (string) { // <=Ceci est l’ID réel
            "channel": (string) le type de message du canal qui doit être un e-mail, ios_push, webhook, content_card, in-app_messageou SMS,
            "name": (string) le nom du message dans le tableau de bord (par ex., « Variation 1 »)
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) les comportements d’événement de conversion assignés à la campagne, voir la section suivante sur le comportement des conversions.
}
```

### Messages

La réponse `messages` contiendra des informations sur chaque message. Voici des exemples de réponses de message pour chaque canal :

#### Canaux de notification push

```json
{
    "channel": (string) la description du canal, telle que « ios_push » ou « android_push »
    "alert": (string) le texte du corps de l’alerte,
    "extras": (hash) n’importe quelle paire clé-valeur fournie
}
```

#### Canal d’e-mail

```json
{
    "channel": "e-mail",
    "subject": (string) l’objet,
    "body": (string) le corps HTML,
    "from": (string) l’adresse d’émission et le nom affiché,
    "reply_to": (string) le champ « répondre à » pour les messages s’il est différent de l’adresse « de »,
    "title": (string) le nom de l’e-mail,
    "extras": (hash) n’importe quelle paire clé-valeur fournie
}
```

#### Canal de message in-app

```json
{
    "type": (string) la description du type de messages dans l’appli, telle que « sondage »,
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) le texte affiché pour l’en-tête du sondage,
                    }
                "choices": [
                    {
                       "choice_id": (string) l’identifiant de choix,
                       "text": (string) le texte affiché, 
                       "custom_attribute_key": (string) la clé d’attribut personnalisé, 
                       "custom_attribute_value": (string) la valeur d’attribut personnalisé,
                       "deleted": (boolean) supprimé d’une campagne active, 
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
    "name": (string) le nom de la variante,
    "extras": (hash) n’importe quelle paire clé-valeur fournie ; présent uniquement si au moins une paire clé-valeur a été définie
}
```

#### Canal de webhook

```json
{
    "channel": "webhook",
    "url": (string) l’URL du webhook,
    "body": (string) le corps des charges utiles,
    "type": (string) le type de contenu du corps,
    "headers": (hash) les en-têtes de requête spécifiés,
    "method": (string) la méthode HTTP, soit POST, soit GET
}
```

#### Canal SMS

```json
{
  "channel": "sms",
  "body": (string) le corps des charges utiles,
  "from": (string) la liste de nombres associés au groupe d’abonnement,
  "subscription_group_id": (string) l’ID d’API du groupe d’abonnement ciblé dans le message SMS
}
```

#### Messages de contrôle

```json
{
    "channel": (string) la description du canal pour lequel existe le contrôle,
    "type": "control"
}
```

### Comportements de conversion

Le tableau `conversion_behaviors` contiendra des informations sur chaque comportement relatif aux événements de conversion défini pour la campagne. Ces comportements sont dans l’ordre défini par la campagne. Par exemple, l’événement de conversion A sera le premier élément du tableau, l’événement de conversion B sera le deuxième, etc. Les listes suivantes présentent des exemples de comportement relatif aux événements de conversion :

#### Clique sur l’e-mail

```json
{
    "type": "Clique sur l’e-mail",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures
}
```

#### Ouvre l’e-mail

```json
{
    "type": "Ouvre l’e-mail",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures
}
```

#### Achète (tout achat)

```json
{
    "type": "Effectue n’importe quel achat",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures
}
```

#### Achète (produit spécifique)

```json
{
    "type": "Effectue un achat spécifique",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures,
    "product": (string) le nom du produit, par ex., - « Armure pour félin »"
}
```

#### Effectue un événement personnalisé

```json
{
    "type": "Effectue un événement personnalisé",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures,
    "custom_event_name": (string) le nom du produit, par ex., - « Armure pour félin d’occasion »"
}
```

#### Met à niveau l’application

```json
{
    "type": "Met à niveau l’application",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures,
    "app_ids": (array or null) tableau des ID d’application, par ex., - ["12345", "67890"] ou `null` si « Track sessions for any app » (Suivre les sessions pour toutes les applis) est sélectionné dans l’interface utilisateur
}
```

#### Utilise l’application

```json
{
    "type": "Lancer la session",
    "window": (integer) le nombre de secondes pendant lesquelles un utilisateur peut se convertir sur cet événement, par ex., - 86 400, qui représente 24 heures,
    "app_ids": (array or null) tableau des ID d’application, par ex., - ["12345", "67890"] ou `null` si « Track sessions for any app » (Suivre les sessions pour toutes les applis) est sélectionné dans l’interface utilisateur
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)..
{% endalert %}

{% endapi %}
