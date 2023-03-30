---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Cet article contient les notes de version de mai 2020."
---
# Mai 2020

## Google Tag Manager

Ajout de documents et exemples de déploiement et de gestion du SDK Android de Braze en utilisant [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/android_google_tag_manager/).

## Nouvel endpoint de l’API pour blacklister des adresses 

Vous pouvez désormais [blacklister]({{site.baseurl}}/api/endpoints/email/post_blacklist/) des adresses e-mail via l’API Braze. L’ajout d’une adresse e-mail à la liste noire entraîne le désabonnement de l’utilisateur à l’e-mail et le marque comme rebond élevé.

## Changement clé API pour les endpoints de l’API Braze

En mai 2020, Braze a modifié la façon dont nous lisons les clés API pour plus de sécurité. Les clés API doivent être transmises dans l’en-tête de la requête. Des exemples sont disponibles sur les pages des endpoints individuels sous **Example Request ** (Exemple de requête), ainsi que dans **API Key Explanation** (Explication de la clé API).

Braze continuera à prendre en charge la transmission du `api_key` dans le corps de la requête et les paramètres d’URL, mais cette prise en charge sera arrêtée un jour (à déterminer). **Mettez à jour vos appels API en conséquence.** Ces modifications ont été mises à jour dans [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details Explication de la clé API %}
{% tabs %}
{% tab GET Request %}
Cet exemple utilise l’endpoint /email/hard_bounces.

**Avant : Clé API dans le corps de requête**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key=YOUR-REST-API-KEY&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**Maintenant : Clé API dans l’en-tête**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
Cet exemple utilise l’endpoint /user/track.

**Avant : Clé API dans le corps de requête**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Maintenant : Clé API dans l’en-tête**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


