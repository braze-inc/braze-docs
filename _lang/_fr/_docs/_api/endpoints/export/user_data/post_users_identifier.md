---
nav_title: "POST: Export du profil utilisateur par identifiant"
article_title: "POST: Export du profil utilisateur par identifiant"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les utilisateurs par ID Braze terminal."
---

{% api %}
# Utilisateurs par identifiant de terminaison
{% apimethod post %}
/fr/users/export/ids
{% endapimethod %}

Ce point de terminaison vous permet d'exporter des données depuis n'importe quel profil utilisateur en spécifiant une forme d'identification utilisateur. Jusqu'à 50 `external_ids` ou `user_aliases` peuvent être inclus dans une seule requête. Si vous voulez spécifier `device_id` ou `email_address` seul un des deux identifiants peut être inclus par requête.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='users export ids' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optionnel, tableau de chaînes) Identifiants externes pour les utilisateurs que vous souhaitez exporter,
  "user_aliases": (optionnel, tableau d'alias d'objets utilisateurs) alias alias alias des alias pour les utilisateurs à exporter,
  "device_id": (optionnel, string) Identificateur de périphérique retourné par diverses méthodes SDK telles que `getDeviceId`,
  "braze_id": (optionnel, chaîne) Identifiant de Braze pour un utilisateur particulier,
  "email_address": (optionnel, chaîne) Adresse email de l'utilisateur,
  "phone": (optionnel, chaîne) Numéro de téléphone d'utilisateur,
  "fields_to_export": (optionnel, tableau de chaînes) Nom des champs de données utilisateur à exporter. Tout par défaut si non fourni
}
```

## Paramètres de la requête

| Paramètre           | Requis    | Type de données                                               | Libellé                                                                                                        |
| ------------------- | --------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `ID_externe`        | Optionnel | Tableau de chaînes                                            | Identifiants externes pour les utilisateurs que vous souhaitez exporter.                                       |
| `Alias utilisateur` | Optionnel | Tableau de l'objet alias de l'utilisateur                     | [Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) pour les utilisateurs à exporter. |
| `id de l'appareil`  | Optionnel | Chaîne de caractères                                          | Identificateur de périphérique, tel que retourné par diverses méthodes SDK telles que `getDeviceId`.           |
| `braze_id`          | Optionnel | Chaîne de caractères                                          | Identifiant Braze pour un utilisateur particulier.                                                             |
| `Adresse e-mail`    | Optionnel | Chaîne de caractères                                          | Adresse e-mail de l'utilisateur.                                                                               |
| `Téléphone`         | Optionnel | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Numéro de téléphone de l'utilisateur.                                                                          |
| `Champs à exporter` | Optionnel | Tableau de chaînes                                            | Nom des champs de données utilisateur à exporter. Tous par défaut si non fourni.                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [{
    "alias_name": "example_alias",
    "alias_label": "example_label"
  }],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "exemple@braze. om",
  "téléphone": "+11112223333",
  "fields_to_export": ["prénom", "e-mail", "achats"]
}'
```

## Champs à exporter

Ce qui suit est une liste de `fields_to_export valide`. L'utilisation de `fields_to_export` pour minimiser les données retournées peut améliorer le temps de réponse de cette API :

* `applications`
* `Campagne attribuée`
* `Source attribuée`
* `groupe_adgroup attribués`
* `publicité_attribuée`
* `braze_id`
* `campagnes_reçue`
* `toile_reçue`
* `Cartes cliquées`
* `Pays`
* `créé à`
* `attributs_personnalisés`
* `événements_personnalisé`
* `appareils`
* `chien`
* `Email`
* `Inscription par e-mail`
* `id externe`
* `prénom`
* `Sexe`
* `ville_domicile`
* `Langue`
* `coordonnées_précédentes`
* `nom_de famille`
* `Téléphone`
* `achats`
* `Poussez vous abonner`
* `Pousse_tokens`
* `seau_aléatoire`
* `fuseau horaire`
* `Revenus totaux`
* `désinstallé_à`
* `Alias utilisateur`

Veuillez noter que le point de terminaison `/users/export/ids` rassemblera l'ensemble du profil utilisateur pour cet utilisateur, y compris les données telles que toutes les campagnes et Canvases reçues, tous les événements personnalisés effectués, tous les achats effectués et tous les attributs personnalisés. Par conséquent, ce point de terminaison est plus lent que les autres terminaux de l'API REST.

Selon les données demandées, ce point de terminaison de l'API peut ne pas être en mesure de remplir votre limite horaire de taux d'API. Si vous prévoyez d'utiliser ce point de terminaison régulièrement pour exporter des utilisateurs, envisagez plutôt d'exporter les utilisateurs par segment, qui est asynchrone et plus optimisé pour les tirages de données plus grands. La documentation sur ce point de terminaison est ci-dessous.

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' lorsqu'il est terminé sans erreurs,
    "utilisateurs" : (tableau d'objet) les données pour chacun des utilisateurs exportés, peut être vide si aucun utilisateur n'est trouvé,
    "invalid_user_ids" : (optionnel, tableau de chaîne) chacun des identifiants fournis dans la requête qui ne correspond pas à un utilisateur connu
}
```

Pour un exemple des données accessibles via ce terminal, voir l'exemple ci-dessous.

### Exemple de sortie de fichier d'exportation utilisateur

Exportation de l'objet utilisateur (nous inclurons le moins de données possibles) - si un champ est manquant dans l'objet, il devrait être considéré comme null, false, ou vide) :

```json
{
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (chaîne)
      }
    ],
    "braze_id": (chaîne),
    "first_name" : (chaîne),
    "nom_famille" : (chaîne),
    "email" : (chaîne),
    "dob" : (chaîne) date de naissance de l'utilisateur,
    "home_city" : (string),
    "country" : (string),
    "phone" : (string),
    "language" : (chaîne) ISO-639 code à deux lettres,
    "time_zone" : (chaîne),
    "last_coordinates" : (tableau de float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (chaîne),
    "attributed_adgroup" : (chaîne),
    "attributed_ad" : (chaîne),
    "push_subscribe" : (chaîne) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (objet) paires d'attributs clé-valeur,
    "custom_events" : [
        {
            "name" : (string),
            "d'abord" : (chaîne) date,
            "dernier" : (chaîne) date,
            "count" : (int)
        },
...
    ],
    "achats" : [
        {
            "nome" : (chaîne),
            "d'abord" : (chaîne) date,
            "dernier" : (chaîne) date,
            "count" : (int)
        },
...
    ],
    "devices" : [
        {
            "model" : (string),
            "os" : (chaîne),
            "porteur" : (chaîne),
            "idfv" : (chaîne) uniquement inclus pour les périphériques iOS,
            "idfa" : (chaîne) uniquement inclus pour les appareils iOS lorsque la collection IDFA est activée,
            "google_ad_id" : (chaîne) uniquement inclus pour les appareils Android lorsque la collection Google Play Advertising Identifier est activée,
            "roku_ad_id" : (chaîne) inclus uniquement pour les périphériques Roku,
            "windows_ad_id" : (chaîne) inclus uniquement pour les périphériques Windows,
            "ad_tracking_enabled" : (bool)
        },
...
    ],
    "push_tokens" : [
        {
            "app" : (string) nom de l'application,
            "platform" : (string),
            "token" : (string)
        },
...
    ],
    "apps" : [
        {
            "name" : (string),
            "platform" : (chaîne),
            "version" : (chaîne),
            "sessions" : (entier),
            "first_used" : (chaîne) date,
            "last_used" : (chaîne) date
        },
...
    ],
    "campaigns_received" : [
        {
            "name" : (string),
            "last_received" : (chaîne) date,
            "engagé" : {
                "opened_email" : (bool),
                "opened_push" : (bool),
                "clicked_email" : (bool),
                "clicked_triggered_in_app_message" : (bool)
            },
            "converti" : (bool),
            "api_campaign_id" : (string),
            "variation_name" : (optionnel, chaîne) n'existe que s'il s'agit d'une campagne multivariée,
            "variation_api_id" : (optionnel, chaîne) n'existe que si c'est une campagne multivariée,
            "in_control" : (optionnel, bool) n'existe que si c'est une campagne multivariée
        },
...
    ],
    "canvases_received": [
        {
            "name": (string),
            "api_canvas_id": (chaîne),
            "last_received_message": (string) date,
            "last_entered": (string) date,
            "variation_name" : (chaîne),
            "in_control": (bool),
            "last_exited": (string) date,
            "steps_received": [
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                }
            ]
        },
...
    ],
    "cards_clicked" : [
        {
            "name" : (string)
        },
...
    ]
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
