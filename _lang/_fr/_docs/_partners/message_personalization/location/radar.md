---
nav_title: Radar
article_title: Radar
alias: /fr/partners/radar/
description: "Cet article décrit le partenariat entre Braze et Radar, une plate-forme de géorepérage, pour ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
page_type: partenaire
search_tag: Partenaire
---

# Radar

> [Radar](https://www.onradar.com/) est la première plateforme de géorepérage et de suivi de localisation. La plate-forme Radar a trois produits de base : [Geofences](https://radar.io/product/geofencing), [Tracking de voyage](https://radar.io/product/trip-tracking), et [API de géo](https://radar.io/product/api). La combinaison de la plateforme d’engagement leader dans l’industrie et des capacités de géorepérage de Radar vous permet de générer des revenus et de fidéliser vos produits grâce à une vaste gamme d’expériences de produits et de services géothermiques.

L'intégration de Radar et Braze vous permet d'accéder à des campagnes sophistiquées basées sur la localisation et d'enrichir votre profil utilisateur avec des données de localisation riches et de première partie.

Lorsque des événements de géorepérage Radar ou de suivi de voyage sont générés, Radar enverra des événements personnalisés et des attributs utilisateur à Braze en temps réel. Vous pouvez utiliser ces événements et attributs pour déclencher des campagnes basées sur la localisation, alimenter des opérations de ramassage et de livraison du dernier kilomètre. surveiller la logistique de la flotte et de l'expédition, ou construire des segments d'utilisateurs en fonction des modèles d'emplacement.

De plus, les API de Radar Geo peuvent être mises à profit pour enrichir ou personnaliser vos campagnes de marketing via [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/).

## Pré-requis

| Exigences                            | Libellé                                                                                                                                                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte radar                         | Un compte Radar est requis pour profiter de ce partenariat.                                                                                                                                                  |
| Braze clé API REST                   | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Identifiant du groupe                | L'identifiant de votre groupe peut être trouvé dans la page __Tableau de bord Braze -> Console développeur__.                                                                                                |
| Clé iOS API<br>clé Android API | Ces clés API se trouvent dans la page __du tableau de bord Braze -> Gérer les paramètres__.                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour mapper les données entre les SDK Braze et Radar, vous devez définir les mêmes identifiants d'utilisateur dans les deux systèmes. Cela peut être fait en utilisant la méthode `changeUser()` dans le Braze SDK et la méthode `setUserId()` dans le Radar SDK.

Pour activer l'intégration sur la page d'intégration [Radar](https://www.onradar.com/integrations) sous Brésil :
  - Définir __Activé__ à __Oui__
  - Définissez votre point de terminaison Braze
  - Coller l'identifiant de votre groupe et les clés API
  - Entrez le filtrage des attributs d'événement ou d'événement pour vous assurer que seules les données pertinentes sont envoyées à Braze pour un marketing d'engagement

{% alert note %}
Vous pouvez définir des clés API distinctes pour les environnements de test et de production.
{% endalert %}

À chaque fois que des événements Radar sont générés, Radar enverra des événements personnalisés et des attributs d'utilisateur à Braze. Les événements des appareils iOS seront envoyés à l'aide de vos clés d'API iOS ; les événements et les attributs des utilisateurs des appareils Android seront envoyés en utilisant vos clés API Android.

## Cas d'événements et d'attributs

Vous pouvez utiliser des événements personnalisés et des attributs utilisateur pour construire des segments basés sur la localisation ou déclencher des campagnes basées sur la localisation.

### Segment d'utilisateurs itinérants

Envoyer une notification push à l'utilisateur lorsqu'il est arrivé dans votre magasin pour un ramassage en bordure de la courbe.

![Segment Radar]({% image_buster /assets/img_archive/radar-segment.png %})

### Déclencher lorsqu'un utilisateur entre dans un emplacement avec une grande confiance

Envoyer une notification quand un utilisateur arrive dans votre boutique.

![Campagne radar]({% image_buster /assets/img_archive/radar-campaign.png %})

## Contenu connecté

L'exemple suivant montre comment faire une promotion pour conduire les utilisateurs à proximité en magasin avec une offre numérique.

!\[Exemple de contenu connecté\]\[1\]{: style="float:right;max-width:30%;border:0;"}

Pour commencer, vous devrez avoir à portée de main votre clé API Radar pour pouvoir l'utiliser dans les URLs de votre requête.

Ensuite, dans une balise `connected_content` , faites une requête GET à la [Search Places API](https://radar.io/documentation/api#search-places). La recherche place l'API renvoie les emplacements proches en se basant sur [Lieux radar](https://radar.io/documentation/places): une base de données de lieux des chaînes et des catégories qui offrent une vue d'ensemble du monde.

Afficher ci-dessous est un exemple de ce que Radar retournera en tant qu'objet JSON depuis l'appel API :

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Cible",
      "emplacement": {
        "type": "Point",
        "coordonnées": [
          -74. 2653983613333,
          40. 48302893822985
        ]
      },
      "catégories": [
        "shopping-retail",
        "Magasin de département"
      ],
      "chaîne": {
        "slug": "target",
        "name": "Target",
        "domaine": "target. om"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "emplacement": {
        "type": "Point",
        "coordonnées": [
          -74. 4121885326864,
          40. 54603296187224
        ]
      },
      "catégories": [
        "shopping-retail"
      ],
      "chaîne": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart. om"
      }
    }
  ]
}
```

Pour construire le contenu connecté ciblé et personnalisé message Braze vous pouvez tirer parti de l'attribut Braze `most_recent_location` comme entrée pour le paramètre `proche de` dans l'URL de la requête API. L'attribut `most_recent_location` est collecté via l'intégration de l'événement Radar ou directement à travers le Braze SDK.

Dans l'exemple ci-dessous, le filtrage de la chaîne Radar est appliqué pour les emplacements Target et Walmart, et le rayon de recherche pour les emplacements à proximité est fixé à 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Comme vous pouvez le voir depuis la balise `connect_content` ci-dessus, l'objet JSON est stocké dans la variable locale `à proximité` en ajoutant `:save à proximité` après l'URL. Vous pouvez tester ce que devrait être la sortie en référençant {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

En rassemblant notre cas d'utilisation, voici à quoi ressemblerait la syntaxe de la campagne. Le code ci-dessous itère à travers l'objet `nearbyplaces.places` , extrayant des valeurs uniques et les concaténant avec des délimiteurs lisibles par l'homme appropriés pour le message.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}. ongitude}}&chaînes=cible, almart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiteur = ", " %}
{% assigner des noms = à proximité. dentelles | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% noms elsifs. Taille > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assigner noms_final_str = noms_final_str | append: nom %}
{% elsif forloop.last == true %}
{% assigner noms_final_str = noms_final_str | append: ", and " | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiteur | append: name %}
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
Visitez [la documentation de Radar](https://radar.io/documentation/api) pour toutes les API Radar qui peuvent être exploitées dans le contenu connecté.
{% endalert %}
[1]: {% image_buster /assets/img/radar_example.png %}