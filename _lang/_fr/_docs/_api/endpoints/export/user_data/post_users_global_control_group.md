---
nav_title: "POST: Export du profil utilisateur par groupe de contrôle global"
article_title: "POST: Export du profil utilisateur par groupe de contrôle global"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les utilisateurs dans les groupes de contrôle mondial Braze terminal."
---

{% api %}
# Utilisateurs par groupe de contrôle global
{% apimethod post %}
/fr/users/export/global_control_group
{% endapimethod %}

Ce point de terminaison vous permet d'exporter tous les utilisateurs du Groupe de Contrôle Global. Les données utilisateur sont exportées sous la forme de plusieurs fichiers d'objets JSON utilisateur séparés par de nouvelles lignes (c'est-à-dire un objet JSON par ligne).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

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

Si vous n'avez pas les informations d'identification S3, la réponse à la requête fournit l'URL où un fichier zip contenant tous les fichiers de l'utilisateur peut être téléchargé. L'URL ne deviendra un emplacement valide que lorsque l'exportation sera prête. Veuillez noter que si vous n'avez pas les identifiants S3, il y a une limitation de la quantité de données que vous pouvez exporter à partir de ce terminal. Selon les champs que vous exportez et le nombre d’utilisateurs, le transfert de fichier peut échouer s’il est trop volumineux. Une meilleure pratique est de spécifier quels champs vous voulez exporter en utilisant « fields_to_export» et de spécifier uniquement les champs dont vous avez besoin, afin de garder la taille du transfert plus faible. Si vous voulez exporter tous vos utilisateurs et obtenir des erreurs de génération du fichier, envisagez de diviser votre base utilisateur en plus de segments basés sur un numéro de segment aléatoire (e. . Créer un segment où le numéro de segment est aléatoire <1000, entre 1000 et 2000, etc.).

Dans l'un ou l'autre des scénario, vous pouvez éventuellement fournir un `callback_endpoint` pour être notifié lorsque l'exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande de publication à l'adresse fournie lorsque le téléchargement sera prêt. Le corps du message sera "success":true. Si vous n'avez pas ajouté les identifiants S3 à Braze, alors le corps du message aura en plus l'attribut `url` avec l'url de téléchargement comme valeur.

De plus grandes bases d'utilisateurs se traduiront par des temps d'exportation plus longs. Par exemple, une application de 20 millions d'utilisateurs peut prendre une heure ou plus.

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
    "callback_endpoint" : (optionnel, string) endpoint pour poster une url de téléchargement lorsque l'exportation est disponible,
    "fields_to_export" : (requis, table de chaîne) nom des champs de données utilisateur à exporter, e. . ['first_name', 'email', 'purchases'],
    "output_format" : (optionnel, ) Lorsque vous utilisez votre propre segment S3, vous permet de spécifier le format de fichier en tant que 'zip' ou 'gzip'. Format de fichier zip
 } par défaut
```

{% alert warning %}
Les attributs personnalisés individuels ne peuvent pas être exportés. Cependant, tous les attributs personnalisés peuvent être exportés en incluant les attributs custom_attributes dans le tableau fields_to_export (par exemple [‘first_name’, ‘email’, ‘custom_attributes’]).
{% endalert %}

## Paramètres de la requête

| Paramètre           | Requis       | Type de données                  | Libellé                                                                                                                                                                                                                             |
| ------------------- | ------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | Optionnel    | Chaîne de caractères             | Point de terminaison vers lequel afficher une URL de téléchargement lorsque l'exportation est disponible.                                                                                                                           |
| `Champs à exporter` | Obligatoire* | Tableau de chaînes de caractères | Nom des champs de données utilisateur à exporter, vous pouvez également exporter des attributs personnalisés. <br><br>*À partir d'avril 2021, les nouveaux comptes doivent spécifier des champs spécifiques à exporter. |
| `Format de sortie`  | Optionnel    | Chaîne de caractères             | Lorsque vous utilisez votre propre compartiment S3, permet de spécifier le format de fichier comme `zip` ou `gzip`. Format de fichier ZIP par défaut.                                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
    "callback_endpoint" : "",
    "fields_to_export" : ["email", "braze_id"],
    "output_format" : "zip"
}'
```

## Champs à exporter

Ce qui suit est une liste de fields_to_export valide. Utiliser fields_to_export pour minimiser les données retournées peut améliorer le temps de réponse de cette API :

* `applications`
* `Campagne attribuée`
* `Source attribuée`
* `groupe_adgroup attribués`
* `publicité_attribuée`
* `braze_id`
* `Pays`
* `créé à`
* `attributs_personnalisés`
* `événements_personnalisé`
* `appareils`
* `chien`
* `Email`
* `id externe`
* `prénom`
* `Sexe`
* `ville_domicile`
* `Langue`
* `coordonnées_précédentes`
* `nom_de famille`
* `Téléphone`
* `achats`
* `seau_aléatoire`
* `fuseau horaire`
* `Revenus totaux`
* `désinstallé_à`
* `Alias utilisateur`

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (requis, chaîne) le statut de l'exportation, retourne 'success' si complété sans erreurs,
    "object_prefix": (requis, ) le préfixe de nom de fichier qui sera utilisé pour le fichier JSON produit par l'exportation, e. . 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (facultatif, string) l'url où les données d'exportation du segment peuvent être téléchargées si vous n'avez pas vos propres identifiants S3
}
```

Une fois disponible, l'url ne sera valide que pour quelques heures. À ce titre, nous vous recommandons fortement d’ajouter vos propres identifiants S3 au Brésil.

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
    "prénom" : (chaîne),
    "nom_famille" : (chaîne),
    "email" : (chaîne),
    "dob" : (chaîne) date de naissance de l'utilisateur,
    "home_city" : (chaîne),
    "country" : (string),
    "phone" : (string),
    "language" : (chaîne) ISO-639 code à deux lettres,
    "time_zone" : (chaîne),
    "last_coordinates" : (tableau de float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (chaîne),
    "attributed_ad" : (chaîne),
    "custom_attributes" : (objet) paires d'attributs clé-valeur,
    "custom_events" : [
        {
            "name" : (string),
            "premier" : (chaîne) date,
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
}
```

{% endapi %}