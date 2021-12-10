---
nav_title: "GET: Détails de la campagne"
article_title: "GET: Détails de la campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison Get Campaign Details ."
---

{% api %}
# Point de terminaison des détails de la campagne
{% apimethod get %}
/fr/campaigns/details
{% endapimethod %}

Ce point de terminaison vous permet de récupérer des informations pertinentes sur une campagne spécifiée, qui peuvent être identifiées par le `campaign_id`. Si vous voulez récupérer les données de Canvas, reportez-vous au point de terminaison [Détails du Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## Paramètres de la requête

| Paramètre     | Requis | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id` | Requis | Chaîne de caractères | Voir [l'identifiant API de la campagne]({{site.baseurl}}/api/identifier_types/).<br><br> La `campaign_id` pour les campagnes API peut être trouvée sur la **Console développeur** et la **page de détails de campagne** de votre tableau de bord ; ou vous pouvez utiliser le [Liste de Campagne point d'extrémité](#campaign-list-endpoint). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponses

### Détails de la campagne de réponse API du point de terminaison

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsque complété sans erreurs,
    "created_at" : (chaîne) date créée en tant que date ISO 8601,
    "updated_at" : (chaîne) date dernière mise à jour en tant que date ISO 8601,
    "archivé" : (booléen) si cette campagne est archivée,
    "brouillon": (booléen) si cette campagne est un brouillon,
    "nome" : (chaîne) nom de la campagne,
    "description" : (chaîne) description de la campagne,
    "schedule_type" : (chaîne) type d'action de planification,
    "canaux" : (tableau) liste des canaux à envoyer via,
    "first_sent" : (chaîne) date et heure du premier envoi en tant que date ISO 8601,
    "last_sent" : (chaîne) date et heure de dernière envoi en date ISO 8601,
    "tags" : (tableau) noms de balises associés à la campagne,
    "messages": {
        "message_variation_id": (string) { // <=Ceci est l'id actuel
            "channel": (string) type de canal du message (comme dans , "email", "ios_push", "webhook", "content_card", "in-app_message", "sms"),
            "name": (chaîne) nom du message dans le tableau de bord (par ex. "Variation 1")
            ... champs spécifiques au canal pour ce message, voir ci-dessous ...
        }
    },
    "conversion_behaviors": (tableau) comportements d'événement de conversion assignés à la campagne (voir ci-dessous)
}
```

### Messages

La réponse `messages` contiendra des informations sur chaque message. Exemple de réponse de message pour les salons sont ci-dessous:

#### Chaînes Push

```json
{
    "channel": (string) description du canal, comme "ios_push" ou "android_push"
    "alert": (string) texte d'alerte du corps,
    "extras": (hash) toutes les paires clé-valeur fournies
}
```

#### Chaîne e-mail

```json
{
    "channel": "email",
    "subject": (string) sujet,
    "body": (string) HTML corps,
    "from": (string) à partir de l'adresse et du nom affiché,
    "reply_to": (chaîne) réponse pour message, si différent de l'adresse "from",
    "title": (chaîne) nom de l'email,
    "extras": (hash) toutes les paires clé-valeur fournies
}
```

#### Canal de message intégré

```json
{
    "type": (string) description du type de message dans l'application, comme "sondage",
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) affiche le texte de l'en-tête de l'enquête,
                    }
                "choices": [
                    {
                       "choice_id": (string) identifiant de choix,
                       "text": (chaîne) texte affiché, 
                       "custom_attribute_key": (string) clé d'attribut personnalisé, 
                       "custom_attribute_value": (sting) valeur d'attribut personnalisé,
                       "supprimé": (booléen) supprimé de la campagne live, 
                    },
...
                ]
            }
        ]
    }
}
```

#### Chaîne de la carte de contenu

```json
{
    "channel": "content_cards",
    "name": (string) nom de variante,
    "extras": (hash) toutes les paires clé-valeur fournies; seulement présent si au moins une paire clé-valeur a été définie
}
```

#### Canal Webhook

```json
{
    "channel": "webhook",
    "url": (string) url pour le webhook,
    "body": (string) payload body,
    "type": (chaîne) type de contenu du corps,
    "en-têtes": (hash) les en-têtes de requête spécifiées,
    "method": (string) méthode HTTP (e. ., "POST" ou "GET"),
}
```

#### Canal SMS

```json
{
  "channel": "sms",
  "body": (string) payload body,
  "from": (chaîne) liste de nombres associés au groupe d'abonnement,
  "subscription_group_id": (string) API id du groupe d'abonnement ciblé dans le message SMS
}
```

#### Contrôler les messages

```json
{
    "channel": (string) description du canal pour lequel le contrôle est effectué,
    "type": "control"
}
```

### Comportements de conversion

La table `conversion_behaviors` contiendra des informations sur chaque comportement d'événement de conversion défini pour la campagne. Ces comportements sont en ordre tel que défini par la campagne. Par exemple, l'événement de conversion A sera le premier élément du tableau, l'événement de conversion B sera le deuxième, etc. Exemple de réponse de comportement de conversion d'événements pour lesquels sont ci-dessous:

#### Clics email

```json
{
    "type": "Clics Email",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i. . - 86400, qui est 24 heures
}
```

#### Ouvre l'email

```json
{
    "type": "Ouvre l'Email",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i. . - 86400, qui est 24 heures
}
```

#### Effectue un achat (tout achat)

```json
{
    "type": "Fait tout achat",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i. . - 86400, qui est 24 heures
}
```

#### Fait l'achat (produit spécifique)

```json
{
    "type": "Effectue un achat spécifique",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i. . - 86400, qui est 24 heures,
    "produit": (chaîne) nom du produit, i.e. - "Armure du Corps de la Féline"
}
```

#### Effectue un événement personnalisé

```json
{
    "type": "Effectue un événement personnalisé",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i. . - 86400, qui est de 24 heures,
    "custom_event_name": (chaîne) nom de l'événement, i. . - "Armure corporelle du Chat utilisée"
}
```

#### Mettre à jour l'application

```json
{
    "type": "Application de mise à niveau",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i.e. - 86400, qui est de 24 heures,
    "app_ids": (tableau|null) tableau d'ID d'application, i.e. - ["12345", "67890"], ou `null` si "Track sessions for any app" est sélectionné dans l'interface utilisateur
}
```

#### Utilise l'application

```json
{
    "type": "Commence la session",
    "window": (entier) nombre de secondes au cours desquelles l'utilisateur peut convertir sur cet événement, i.e. - 86400, qui est de 24 heures,
    "app_ids": (tableau|null) tableau d'ID d'application, i.e. - ["12345", "67890"], ou `null` si "Track sessions for any app" est sélectionné dans l'interface utilisateur
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
