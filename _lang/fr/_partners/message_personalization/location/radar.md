---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Cet article de référence présente le partenariat entre Braze et Radar, une plateforme de géorepérage, pour ajouter le contexte et le suivi de l’emplacement à vos applications iOS et Android."
page_type: partner
search_tag: Partenaire

---

# Radar

> [Radar](https://www.onradar.com/) est la plateforme leader de géorepérage et de suivi de localisation. La plateforme Radar a trois produits principaux : [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking) et [API Geo](https://radar.io/product/api). La combinaison de la plateforme d’engagement Braze et des capacités de géorepérage de Radar, leader du secteur, vous permet de générer des revenus et de fidéliser vos clients grâce à une large gamme d’expériences de produits et de services géolocalisés. Cela inclut le suivi des collectes et des livraisons, les notifications déclenchées par emplacement, la personnalisation contextuelle, la vérification des emplacements, les localisateurs de magasin, l’adresse automatique, etc.

L’intégration de Braze et Radar vous permet d’accéder à des déclencheurs de campagne sophistiqués basés sur l’emplacement et à l’enrichissement de profils utilisateur avec des données de localisation riches et de première partie. Lorsque des événements de geofence ou de suivi de parcours sont générés par Radar, les événements personnalisés et les attributs utilisateur sont envoyés à Braze en temps réel. Ces événements et attributs peuvent ensuite être utilisés pour déclencher des campagnes de localisation, alimenter les opérations de collecte et de livraison du dernier kilomètre, surveiller la logistique de la flotte et des expéditions, ou créer des segments d’utilisateurs basés sur des modèles de localisation. 

De plus, les API de Radar Geo peuvent être exploitées pour enrichir ou personnaliser vos campagnes marketing via le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/). 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Radar | Un compte Radar est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Cela peut être créé dans le **Tableau de bord de Braze > Developer Console (Console du développeur) > REST API Key (Clé API REST) > Create New Api Key (Créer une nouvelle clé API)** |
| Identifiant du groupe | L’identifiant de votre groupe se trouve sur la page **Tableau de bord de Braze > Developer Console**. |
| Clé API iOS<br>Clé API Android | Ces clés d’API sont disponibles dans la page **Tableau de bord de Braze > Manage Settings (Gérer les paramètres)**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour mapper les données entre les SDK Braze et Radar, vous devez définir les mêmes ID utilisateur dans les deux systèmes. Pour ce faire, vous pouvez utiliser la méthode `changeUser()` du SDK Braze et la méthode `setUserId()` du SDK Radar.

Pour activer l’intégration sur la [page Radar integration (Intégration Radar)](https://radar.com/documentation/integrations) sous Braze :
  - Définissez **Enabled (Activé)** sur **Yes (Oui)**
  - Définissez votre endpoint Braze
  - Collez l’identifiant de votre groupe et les clés d’API
  - Saisissez tout filtrage d’événements ou d’attributs d’événements pour vous assurer que seules les données pertinentes sont envoyées à Braze pour le marketing d’engagement

{% alert note %}
Vous pouvez définir des clés d’API distinctes pour l’environnement de test et l’environnement réel.
{% endalert %}

Lorsque les événements Radar sont générés, Radar envoie des événements personnalisés et des attributs utilisateur à Braze. Les événements provenant des appareils iOS seront envoyés à l’aide de vos clés d’API iOS ; les événements et les attributs utilisateur provenant des appareils Android seront envoyés à l’aide de vos clés d’API Android.

## Cas d’utilisation d’événements et d’attributs

Vous pouvez utiliser des événements personnalisés et des attributs utilisateur pour créer des segments basés sur l’emplacement ou déclencher des campagnes basées sur l’emplacement.

### Déclencher une notification d’arrivée en magasin pour la collecte trottoir 

Envoyez une notification push à l’utilisateur avec les instructions d’arrivée lorsqu’il arrive à votre magasin pour une collecte trottoir.

![Une campagne de livraison par événement montrant que la campagne sera livrée lorsque l’événement personnalisé « arrived_at_trip_destination » se produit, et que « trip_metadata » est égal à « trottoir ».]({% image_buster /assets/img_archive/radar-campaign.png %})

### Construire un segment d’audience des visiteurs de magasin récents

Par exemple, cibler les utilisateurs qui ont visité votre magasin au cours des 7 derniers jours, qu’ils aient effectué un achat ou non.

![Un segment où « radar_geofence_tags » inclue la valeur my_store et où « radar_updated_at » correspond à une durée inférieure à sept jours.]({% image_buster /assets/img_archive/radar-segment.png %})

## Contenu connecté

L’exemple suivant montre comment exécuter une promotion pour attirer les utilisateurs à proximité en magasin avec une offre numérique. 

![Une image Android d’un message de notification push de Contenu connecté qui affiche « Nouvelles offres en magasin, Walmart et cible près de chez vous ».][1]{: style="float:right;max-width:30%;border:0;"}

Pour commencer, vous devez disposer de votre clé d’API publiable Radar à utiliser dans vos URL de demande.

Ensuite, dans une balise `connected_content`, effectuez une demande GET vers l’[API Search Places (API de recherche de lieux)](https://radar.io/documentation/api#search-places). L’API de recherche de lieux renvoie des emplacements à proximité en se basant sur [Radar Places](https://radar.io/documentation/places) : une base de données d’emplacements pour les lieux, les chaînes et les catégories qui offre une vue complète du monde.

L’extrait de code suivant est un exemple de ce que Radar renvoie en tant qu’objet JSON à partir de l’appel API :

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

Pour construire le message Braze de Contenu connecté ciblé et personnalisé, vous pouvez exploiter l’attribut Braze `most_recent_location` comme entrée pour le paramètre `near` dans l’URL de la demande API. L’attribut `most_recent_location` est collecté via l’intégration des événements Radar ou directement via le SDK Braze.

Dans l’exemple suivant, le filtrage de la chaîne Radar est appliqué aux emplacements Target et Walmart, et le rayon de recherche des emplacements proches est fixé à 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Comme vous pouvez le voir dans la balise `connect_content`, l’objet JSON est stocké dans la variable locale `nearbyplaces` en ajoutant `:save nearbyplaces` après l’URL.
Vous pouvez tester la sortie en faisant référence à {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

En rassemblant notre cas d’utilisation, voici à quoi ressemblerait la syntaxe de la campagne. Le code suivant itère à travers l’objet `nearbyplaces.places`, en extrayant les valeurs uniques et en les concaténant avec des délimiteurs lisibles par un humain pour le message.

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
Consultez la [documentation de Radar](https://radar.io/documentation/api) pour connaître toutes les API Radar qui peuvent être exploitées dans le Contenu connecté.
{% endalert %}

[1]: {% image_buster /assets/img/radar_example.png %}