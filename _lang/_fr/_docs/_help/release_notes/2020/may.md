---
nav_title: Mai
page_order: 8
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour mai 2020."
---

# Mai 2020

## Gestionnaire de tags Google

Ajout de documentation et d'exemples sur la façon de déployer et de gérer le SDK Android de Braze en utilisant [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/android_google_tag_manager/).

## Nouveau point de terminaison de l'API de blacklist

Vous pouvez maintenant [blacklister]({{site.baseurl}}/api/endpoints/email/post_blacklist/) les adresses e-mail via l'API de Braze. La mise en liste noire d'une adresse e-mail désabonnera l'utilisateur de l'e-mail et le marquera comme étant rebondi dur.

## Changement de clé API pour les terminaux de l'API Braze

Depuis mai 2020, Braze a changé la façon dont nous lisons les clés API pour être plus sécurisés. Les clés API doivent maintenant être passées en tant qu'en-tête de requête. Des exemples peuvent être trouvés sur des pages individuelles de terminaux sous __Exemple de requête__, ainsi que dans __l'explication de la clé API__ ci-dessous.

Braze continuera à supporter le `api_key` passé par le corps de la requête et les paramètres de l'URL, mais sera éventuellement sunset (TBD). __Veuillez mettre à jour vos appels API en conséquence.__ Ces changements ont été mis à jour dans [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
Cet exemple utilise le point de terminaison /email/hard_bounces.

__Avant: clé API dans le corps de la requête__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key=YOUR-REST-API-KEY&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
__Maintenant : clé API dans l'en-tête__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
Cet exemple utilise le point de terminaison /user/track.

__Avant: clé API dans le corps de la requête__
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
    "api_key": YOUR-API-KEY-ICI ,
    "attributs": [ 
    {
      "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "attribut_tableau": ["banane", "pomme"]
    }
    ]
}'
```
__Maintenant : clé API dans l'en-tête__
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
    "attributes": [ 
    {
      "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "attribut_tableau": ["banane", "pomme"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


