---
nav_title: Création de géorepérages
article_title: Création de géorepérages
page_order: 1
page_type: reference
description: "Cet article de référence présente les géorepérages et explique comment créer et configurer les événements de géorepérage."
tool: 
  - Location
search_rank: 9
---

# Géorepérages

> Le « géorepérage » est un concept qui fait partie intégrante de nos solutions de localisation en temps réel. Une géorepérage est une zone géographique virtuelle, représentée par des coordonnées latitudinales et longitudinales associées à un rayon, formant un cercle autour d’une position générale spécifique. Ces géorepérages peuvent varier, allant de la taille d’un bâtiment à celle d’une ville entière.

Vous pouvez définir des géorepérages sur le tableau de bord de Braze et les utiliser pour déclencher des campagnes en temps réel quand l’utilisateur rentre ou sort de leurs limites, ou envoyer des campagnes de suivi des heures ou des jours plus tard. Les utilisateurs qui entrent ou sortent de vos géorepérages apportent une nouvelle couche de données qui peut être utilisée pour segmenter et recibler.

## Aperçu

Gérez les géorepérages à partir de **Audience** > **Localisations**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **Emplacements** sous **Engagement.**
{% endalert %}

Les géorepérages sont organisées en ensembles. Un ensemble est un groupe de géorepérages qui peut être utilisé pour segmenter ou contacter des utilisateurs sur toute la plateforme. Chaque ensemble de géorepérages peut contenir un maximum de 10 000 géorepérages.

Vous pouvez créer ou télécharger une quantité illimitée de géorepérages dans le tableau de bord, ce qui permet à votre équipe marketing de configurer des campagnes et des ensembles de géorepérages sans avoir à calculer le nombre de géorepérages. Braze synchronisera de façon dynamique les géorepérages qu’il suit pour chaque utilisateur, en veillant à ce que les géorepérages les plus pertinentes soient toujours disponibles.

- Les applications Android ne peuvent stocker localement que 100 géorepérages à la fois. Braze est configuré pour stocker jusqu’à 20 géorepérages par application en local.
- Les appareils iOS peuvent surveiller jusqu’à 20 géorepérages à la fois par application. Braze surveille jusqu’à 20 emplacements s’il y a suffisamment d’espace disponible. 
- Si l’utilisateur est éligible à la réception de plus de 20 géorepérages, Braze téléchargera le nombre maximal de positions selon leur proximité par rapport à l’utilisateur au moment du rafraîchissement du démarrage de session ou de notification push silencieuse
- Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n’utilise pas tous les emplacements de géorepérage disponibles.

## Créer des ensembles de géorepérages

### Créer des ensembles manuellement

Dans la page **Localisations**, cliquez sur **\+ Créer un ensemble de géorepérages**.

![Ensemble de géorepérages d’aéroports allemands avec un utilisateur qui dessine un rayon de deux mille mètres sur la carte de l’aéroport de Hambourg.][1]

Après avoir créé un ensemble de géorepérages, vous pouvez ajouter manuellement des géorepérages en les dessinant sur la carte. Nous recommandons de créer des géorepérages avec un rayon d’au moins 200 mètres pour qu’elles fonctionnent de manière optimale. Pour plus d'informations sur les options configurables, reportez-vous à la rubrique [Configuration des géorepérages]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### Création d’ensembles via le téléchargement en masse {#creating-geofence-sets-via-bulk-upload}

Les géorepérages peuvent être téléchargées en bloc en tant qu’objet GeoJSON de type `FeatureCollection`. Chaque géorepérage est un `Point` géométrique dans le groupe de fonctionnalités. Les propriétés de chaque fonctionnalité nécessitent un `"radius"` et une clé `"name"` facultative pour chaque géorepérage. Pour télécharger votre GeoJSON, cliquez sur **\+ Créer un ensemble de géorepérage**, puis sur **Télécharger GeoJSON**.

L'exemple suivant représente le GeoJSON correct pour spécifier deux géorepérages : l'un pour le siège de Braze à New York et l'autre pour la Statue de la Liberté au sud de Manhattan. Nous recommandons de télécharger des géorepérages avec un rayon d’au moins 100 mètres pour qu’elles fonctionnent de manière optimale.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

Gardez les points suivants à l’esprit au moment de créer vos géorepérages :

- La valeur `coordinates` dans le GeoJSON est formatée comme suit : [Longitude, Latitude].
- Le rayon maximal d’une géorepérage pouvant être téléchargé est de 100 000 mètres (100 kilomètres ou environ 62 miles).

## Mettre à jour des ensembles de géorepérages

Pour les utilisateurs actifs, le SDK de Braze ne demandera de géorepérages qu’une fois par jour au démarrage de la session. Cela signifie que si des modifications sont apportées aux ensembles de géorepérages après le début de la session, vous devrez attendre 24 heures à compter de la première collecte des ensembles pour recevoir l’ensemble mis à jour.

Pour les utilisateurs inactifs, si les notifications push sont activées en arrière-plan, Braze enverra également une notification push silencieuse toutes les 24 heures pour extraire les derniers emplacements de l’appareil.

{% alert note %}
Si les géorepérages ne sont pas chargées localement sur l’appareil, l’utilisateur ne pourra pas déclencher la géorepérage même s’il pénètre dans la zone délimitée.
{% endalert %}

### Mettre à jour pour des utilisateurs individuels

Mettre à jour les géorepérages pour des utilisateurs individuels peut être utile à des fins de tests. Pour mettre à jour les ensembles de géorepérages, accédez au bas de la page **Emplacements** et cliquez sur **Resynchroniser les géofences**. Vous serez invité à saisir le `external_id` ou le `email` des utilisateurs que vous désirez mettre à jour

## Utiliser des événements de géorepérage

Une fois les géorepérages configurés, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Déclencheurs

Pour utiliser les données de géorepérage dans le cadre des déclencheurs de campagne et de Canvas, choisissez la **livraison par événement** pour la méthode de livraison. Ensuite, ajoutez une action de déclenchement `Trigger a Geofence`. Pour finir, choisissez l’ensemble de géorepérages et les types d’événements de transition de géorepérage pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l’aide des événements de géorepérage.

![][2]

### Personnalisation

Pour personnaliser votre message à l’aide des données de géorepérage, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Foire aux questions

Consultez notre [FAQ sur les géorepérages][3] pour obtenir des réponses aux questions fréquemment posées sur les géorepérages.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
