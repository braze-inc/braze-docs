---
nav_title: "POST: Export du profil utilisateur par segment"
article_title: "POST: Export du profil utilisateur par segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les utilisateurs par Segment Braze endpoint."
---

{% api %}
# Utilisateurs par segment de terminaison
{% apimethod post %}
/fr/users/export/segment
{% endapimethod %}

Ce point de terminaison vous permet d'exporter tous les utilisateurs dans un segment. Les données utilisateur sont exportées sous la forme de plusieurs fichiers d'objets JSON utilisateur séparés par de nouvelles lignes (c'est-à-dire un objet JSON par ligne).

Notez qu'une entreprise peut fonctionner à un maximum d'un export par segment en utilisant ce point de terminaison à un moment donné. Veuillez attendre que votre exportation soit terminée avant de réessayer.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

{% alert important %}
À partir de décembre 2021, les modifications suivantes prendront effet pour cette API :<br><br>1. Le champ `fields_to_export` dans cette requête API sera __requis__. L'option par défaut à tous les champs sera supprimée.<br>2. Les champs pour `custom_events`, `achats`, `campagnes_received`, et `canvases_received` ne contiendra que les données des 90 derniers jours.
{% endalert %}

## Détails de la réponse basée sur les identifiants

Si vous avez ajouté vos identifiants S3 à Braze, alors chaque fichier sera téléchargé dans votre seau sous forme de fichier zip avec le format de clé qui ressemble à `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename. ip`. Nous allons créer 1 fichier par 5000 utilisateurs pour optimiser le traitement. Vous pouvez ensuite décompresser les fichiers et concaténer tous les fichiers `json` dans un seul fichier si nécessaire. Si vous spécifiez un `output_format` de `gzip`, l'extension du fichier sera `. z` au lieu de `.zip`.

{% details Export Pathing Breakdown for ZIP File %}
Format de fichier ZIP : `nom de bucket/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

Exemple de fichier ZIP : `braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Propriété                        | Détails du produit                                                            | Affiché dans l'exemple comme...        |
| -------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------- |
| `nom du seau`                    | Correction basée sur le nom de votre compartiment.                            | `Seau de docs`                         |
| `exportation de segment`         | Réparé.                                                                       | `exportation de segment`               |
| `ID du segment`                  | Inclus dans la demande d'exportation.                                         | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `AAAA-MM-jj`                     | La date de réception du rappel réussi.                                        | `2019-04-25`                           |
| `UUID de la ligne`               | Un UUID aléatoire hors de la boîte généré par Braze au moment de la requête.  | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `Date de début de l'exportation` | Temps Unix (secondes depuis 2017-01-01:00:00:00Z) que l'export a été demandé. | `1556044807`                           |
| `nom de fichier`                 | Aléatoire par fichier.                                                        | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% enddetails %}

Si vous n'avez pas les identifiants S3 fournis mais que vous avez une intégration Azure configurée avec Braze, les données peuvent y être exportées. Dans le cas contraire, la réponse à la requête fournit une URL obfusquée où un fichier zip contenant tous les fichiers de l'utilisateur peut être téléchargé. L'URL ne deviendra un emplacement valide que lorsque l'exportation sera prête. Nous suggérons fortement aux clients qui utilisent ce point de terminaison de mettre en place leurs propres identifiants S3 afin que les clients puissent appliquer leurs propres politiques de bucket S3 à l'exportation.

Veuillez noter que si vous n'avez pas les identifiants S3, il y a une limitation de la quantité de données que vous pouvez exporter à partir de ce terminal. Selon les champs que vous exportez et le nombre d’utilisateurs, le transfert de fichier peut échouer s’il est trop volumineux. Une meilleure pratique est de spécifier quels champs vous voulez exporter en utilisant « fields_to_export» et de spécifier uniquement les champs dont vous avez besoin, afin de garder la taille du transfert plus faible. Si vous voulez exporter tous vos utilisateurs et obtenir des erreurs de génération du fichier, envisagez de diviser votre base utilisateur en plus de segments basés sur un numéro de segment aléatoire (e. . Créer un segment où le numéro de segment est aléatoire <1000, entre 1000 et 2000, etc.).

Dans l'un ou l'autre des scénario, vous pouvez éventuellement fournir un `callback_endpoint` pour être notifié lorsque l'exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande de publication à l'adresse fournie lorsque le téléchargement sera prêt. Le corps du message sera "success":true. Si vous n'avez pas ajouté les identifiants S3 à Braze, alors le corps du message aura en plus l'attribut `url` avec l'URL de téléchargement comme valeur.

De plus grandes bases d'utilisateurs se traduiront par des temps d'exportation plus longs. Par exemple, une application de 20 millions d'utilisateurs peut prendre une heure ou plus.

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
    "segment_id" : (obligatoire, chaîne) identifiant pour le segment à exporter,
    "callback_endpoint" : (optionnel, chaîne) endpoint pour publier une url de téléchargement lorsque l'exportation est disponible,
    "fields_to_export" : (requis, table de chaîne) nom des champs de données utilisateur à exporter, vous pouvez également exporter des attributs personnalisés. *À partir d'avril 2021, les nouveaux comptes doivent spécifier des champs spécifiques à exporter.
    "output_format" : (optionnel, chaîne) lorsque vous utilisez votre propre compartiment S3, spécifie le format de fichier en tant que 'zip' ou 'gzip'. Format de fichier zip
 } par défaut
```

Le `segment_id` pour un segment donné peut être trouvé dans votre console de développement dans votre compte Braze ou vous pouvez utiliser le [point de terminaison de liste de segments]({{site.baseurl}}/api/endpoints/export/get_segment/).

{% alert warning %}
Les attributs personnalisés individuels ne peuvent pas être exportés. Cependant, tous les attributs personnalisés peuvent être exportés en incluant `custom_attributes` dans le tableau `fields_to_export` (par exemple ['first_name', 'email', 'custom_attributes']).
{% endalert %}

## Paramètres de la requête

| Paramètre             | Requis       | Type de données                  | Libellé                                                                                                                                                                                                                             |
| --------------------- | ------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifiant_segment` | Requis       | Chaîne de caractères             | Identifiant pour le segment à exporter. See [segment identifier]({{site.baseurl}}/api/identifier_types/).                                                                                                                           |
| `callback_endpoint`   | Optionnel    | Chaîne de caractères             | Point de terminaison vers lequel afficher une URL de téléchargement lorsque l'exportation est disponible.                                                                                                                           |
| `Champs à exporter`   | Obligatoire* | Tableau de chaînes de caractères | Nom des champs de données utilisateur à exporter, vous pouvez également exporter des attributs personnalisés. <br><br>*À partir d'avril 2021, les nouveaux comptes doivent spécifier des champs spécifiques à exporter. |
| `Format de sortie`    | Optionnel    | Chaîne de caractères             | Lorsque vous utilisez votre propre compartiment S3, permet de spécifier le format de fichier comme `zip` ou `gzip`. Format de fichier ZIP par défaut.                                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
    "segment_id" : "segment_identifier",
    "callback_endpoint" : "example_endpoint",
    "fields_to_export" : ["prénom", "email", "achats"],
    "output_format" : "zip"
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

## Rappels importants

- Les champs pour `custom_events`, `achats`, `campagnes_received`, et `canvases_received` ne contiendra que des données des 90 derniers jours.
- Les `custom_events` et `achats` contiennent des champs pour `premier` et `premier compte`. Ces deux champs reflèteront des informations de tous les temps et ne se limiteront pas aux seules données des 90 derniers jours. Par exemple, si un utilisateur en particulier a fait l'événement avant 90 jours, ceci sera reflété avec précision dans le champ `premier` et le champ `count` prendra en compte les événements qui se sont produits avant les 90 derniers jours également.
- Le nombre de segments simultanés exportés qu'une entreprise peut exécuter au niveau de terminaison est plafonné à 100. Les tentatives qui dépassent cette limite entraîneront une erreur.


## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' si complété sans erreurs,
    "object_prefix": (requis, ) le préfixe de nom de fichier qui sera utilisé pour le fichier JSON produit par l'exportation, e. . 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (facultatif, string) l'URL où les données d'exportation du segment peuvent être téléchargées si vous n'avez pas vos propres identifiants S3
}
```

Une fois mise à disposition, l'URL ne sera valide que pour quelques heures. À ce titre, nous vous recommandons fortement d’ajouter vos propres identifiants S3 au Brésil.

## Exemple de sortie de fichier d'exportation utilisateur

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
    "prénom" : (chaîne),
    "nom_famille" : (chaîne),
    "email" : (chaîne),
    "dob" : (chaîne) date de naissance de l'utilisateur,
    "home_city" : (string),
    "country" : (string),
    "téléphone" : (chaîne),
    "langue" : (chaîne) ISO-639 code à deux lettres,
    "time_zone" : (string),
    "last_coordinates" : (tableau de float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (chaîne),
    "attributed_ad" : (chaîne),
    "push_subscribe" : (string) "opted_in" "push_opted_in_at" | "subscribed" | "unsubscribed" "push_unsubscribed_at",
    "email_subscribe" : (string) "opted_in" "email_opted_in_at" | "subscribed" | "unsubscribed" "email_unsubscribed_at",
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
            "sessions" : (chaîne),
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
                "clicked_in_app_message" : (bool)
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
Pour obtenir de l'aide sur les exportations CSV et API, reportez-vous à [la fonction de dépannage d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
