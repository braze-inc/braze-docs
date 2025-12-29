---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Cet article de référence présente le partenariat entre Braze et Radar, une plateforme de géorepérage permettant d’ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) est la principale plateforme de géorepérage et de localisation. La plateforme Radar comprend trois produits de base : [Géorepérages](https://radar.io/product/geofencing), [Suivi des déplacements](https://radar.io/product/trip-tracking) et [API de géolocalisation](https://radar.io/product/api). La combinaison de la plateforme d'engagement Braze, leader du secteur, et des capacités de géorepérage de Radar, leader du secteur, vous permet de générer du chiffre d'affaires et de la fidélisation grâce à un large éventail d'expériences de produits et de services basées sur l'emplacement/localisation. Il s'agit notamment du suivi des retraits ou livraisons des articles, des notifications déclenchées en fonction de l'emplacement, de la personnalisation contextuelle, de la vérification de l'emplacement, des localisateurs de magasins, de la saisie semi-automatique des adresses, et bien plus encore.

_Cette intégration est assurée par Radar._

## À propos de l'intégration

L'intégration de Braze et Radar vous permet d'accéder à des déclencheurs de campagne sophistiqués basés sur l'emplacement et à l'enrichissement du profil utilisateur grâce à des données d'emplacement/localisation riches et de première partie. Lorsque les événements de géorepérage ou de suivi de trajet de Radar sont générés, les événements personnalisés et les attributs clients sont envoyés à Braze en temps réel. Ces événements et attributs peuvent ensuite être utilisés pour déclencher des campagnes basées sur la localisation, alimenter les opérations de distribution sur le dernier kilomètre, surveiller la logistique des flottes et des déclencheurs, ou créer des segments d'utilisateurs basés sur des modèles d'emplacement/localisation. 

De plus, les API Radar Geo peuvent être exploitées pour enrichir ou personnaliser vos campagnes marketing grâce au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Radar | Un compte Radar est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Identifiant de l'application | L'[identifiant de votre application]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) peut être trouvé dans le tableau de bord de Braze en sélectionnant **Paramètres** > **Clés API**. |
| Clé API iOS<br>Clé API Android | Vous trouverez ces clés API dans le tableau de bord de Braze, sous **Paramètres** > **Paramètres de l'application**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

Pour mapper des données entre les SDK Braze et Radar, vous devez définir les mêmes ID ou alias d'utilisateur dans les deux systèmes. Pour ce faire, vous pouvez utiliser la méthode `changeUser()` du SDK Braze ou la méthode `setUserId()` du SDK Radar.

Pour activer l'intégration :

1. Dans Radar, recherchez Braze dans la page [Intégrations](https://radar.com/documentation/integrations).
1. Réglez l'option **Activé** sur **Oui.**
3. Collez l'identifiant de votre application et les clés API.

{% alert note %}
Vous pouvez définir des clés API distinctes pour les environnements de test et de production.
{% endalert %}

{:start="4"}
4\. Sélectionnez votre endpoint Braze.
5\. Saisissez tout filtrage d'événement ou d'attribut d'événement pour vous assurer que seules les données pertinentes sont envoyées à Braze pour le marketing d'engagement. Lorsque des événements Radar sont générés, Radar envoie des événements personnalisés et des attributs clients à Braze. Les événements provenant d'appareils iOS seront envoyés à l'aide de vos clés API iOS ; les événements et les attributs utilisateur provenant d'appareils Android seront envoyés à l'aide de vos clés API Android.

{% alert note %}
Par défaut, le paramètre `userId` Radar correspond au paramètre `external_id` Braze pour les utilisateurs connectés. Cependant, vous pouvez suivre les utilisateurs déconnectés ou spécifier des mappages personnalisés en définissant le paramètre `metadata.brazeAlias` ou `metadata.brazeExternalId` dans Radar. Si vous définissez `metadata.brazeAlias`, vous devez également ajouter un alias correspondant dans Braze avec le libellé d'alias `radarAlias`.
{% endalert %}

## Cas d'utilisation basés sur les événements et les attributs

Vous pouvez utiliser des événements et attributs personnalisés pour créer des segments basés sur l'emplacement ou déclencher des campagnes basées sur l'emplacement.

### Déclencher une notification d'arrivée en magasin pour le ramassage à domicile. 

Envoyez une notification push à l'utilisateur avec des instructions pour récupérer son article en bordure de rue.

![Campagne de livraison par action indiquant que la campagne sera livrée lorsque l'événement personnalisé "arrived_at_trip_destination" se produit et que les "trip_metadata" sont "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})

### Créez un segment d'audience composé des visiteurs récents de votre magasin.

Par exemple, ciblez tous les utilisateurs qui ont visité votre magasin au cours des 7 derniers jours, qu'ils aient effectué un achat ou non.

![Un segment où "radar_geofence_tags" inclut la valeur my_store et où "radar_updated_at" date de moins de 7 jours.]({% image_buster /assets/img_archive/radar-segment.png %})

## Contenu connecté

L'exemple suivant montre comment configurer une promotion pour inciter les utilisateurs se trouvant à proximité à se rendre en magasin avec une offre numérique. 

![Image Android d'un message push de contenu connecté affichant "New In Store Deals, Walmart and target near you".]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

Pour commencer, vous devez disposer de votre clé API publiable Radar, que vous utiliserez dans vos URL de requête.

Ensuite, dans une balise `connected_content`, créez une requête GET vers l'[API Rechercher des emplacements](https://radar.io/documentation/api#search-places). L'API de recherche d'emplacements renvoie les emplacements/localisations proches en se basant sur [Radar Places](https://radar.io/documentation/places): une base de données d'emplacements pour les lieux, les chaînes et les catégories qui offre une vue d'ensemble du monde.

L'extrait de code suivant est un exemple de ce que Radar renverra comme objet JSON à partir de l'appel API :

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Pour créer le contenu connecté ciblé et le message personnalisé de Braze, vous pouvez utiliser l'attribut `most_recent_location` de Braze comme entrée du paramètre `near` dans l'URL de la requête d'API. L'attribut `most_recent_location` est collecté via l'intégration des événements Radar ou directement via le SDK de Braze.

Dans l'exemple suivant, le filtrage de la chaîne Radar est appliqué aux emplacements/localisations de Target et Walmart, et le rayon de recherche des emplacements proches est fixé à 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Comme vous pouvez le voir dans la balise`connect_content`, l'objet JSON est stocké dans la variable locale `nearbyplaces` en ajoutant `:save nearbyplaces` après l'URL.
Vous pouvez tester la sortie en vous référant à {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Si l'on configure notre cas d'utilisation, voici à quoi ressemblerait la syntaxe de la campagne. Le code suivant parcourt l'objet `nearbyplaces.places`, extrait les valeurs uniques et les concatène avec des délimiteurs lisibles par l'homme pour le message.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
Consultez la [documentation Radar](https://radar.io/documentation/api) pour connaître toutes les API Radar qui peuvent être utilisées dans le contenu connecté.
{% endalert %}


