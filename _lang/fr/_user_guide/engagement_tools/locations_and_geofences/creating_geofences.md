---
nav_title: Création de geofences
article_title: Création de geofences
page_order: 1
page_type: reference
description: "Cet article de référence présente les geofences et explique comment les créer et les configurer."
tool: 
  - Localisation

---
# Geofences

> Cet article de référence présente les geofences et explique comment les créer et les configurer.

Les « geofences » sont un concept qui fait partie intégrante des solutions de localisation en temps réel de Braze. Une geofence est une zone géographique virtuelle, représentée par des coordonnées latitudinales et longitudinales associées à un rayon, formant un cercle placé dans une position spécifique sur la carte. La taille de ces geofences peut varier, allant de la taille d’un bâtiment à celle d’une ville entière.

Vous pouvez définir des geofences sur le tableau de bord de Braze et déclencher des campagnes en temps réel lorsque vos utilisateurs entrent et sortent de ces zones dans le monde entier. Les geofences sont étroitement intégrées aux capacités de segmentation et de messagerie de Braze. Les campagnes peuvent être envoyées en temps réel aux utilisateurs, dès qu’ils sortent ou entrent dans des geofences, ou envoyées comme messages de suivi quelques heures ou jours plus tard. Lorsqu’ils entrent ou sortent de vos geofences, les utilisateurs apportent une nouvelle couche de données qui peut être utilisée pour segmenter et recibler vos utilisateurs.

Les geofences sont gérées sur la page **Locations (Emplacements)** de la section **Engagement**. Les geofences sont organisées en ensembles. Un ensemble est un groupe de geofences qui peut être utilisé pour segmenter ou contacter des utilisateurs sur toute la plateforme. `All Northeast Regional Stores` ou `September Events` sont deux exemples d’ensembles de geofences. Un ensemble de geofences peut contenir un maximum de 10 000 geofences.

## Créer manuellement des ensembles de geofences

À partir de la page **Locations (Emplacements)**, cliquez sur **+ Create Geofence Set (+ Créer un ensemble de geofences)**.

![Ensemble de geofences d’aéroports allemands avec un utilisateur qui dessine un rayon de deux mille mètres sur la carte de l’aéroport de Hambourg.][1]

Après avoir créé un ensemble de geofences, vous pouvez ajouter manuellement des geofences en les dessinant sur la carte. Nous recommandons de créer des geofences avec un rayon d’au moins 100 mètres pour qu’elles fonctionnent de manière optimale. Pour plus d’informations sur les options configurables, consultez l’article [Configuration des geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/geofence_configuration/).

## Créer des ensembles de geofence via un téléchargement en bloc {#creating-geofence-sets-via-bulk-upload}

Les geofences peuvent être téléchargées en bloc en tant qu’objet GeoJSON de type `FeatureCollection`. Chaque geofence est un `Point` géométrique dans le groupe de fonctions. Les propriétés de chaque fonction nécessitent un `"radius"` et une clé `"name"` facultative pour chaque geofence. Pour télécharger votre objet GeoJSON, cliquez sur **+ Create Geofence Set (+ Créer un ensemble de geofences)**, puis sur **Upload GeoJSON (Télécharger l’objet GeoJSON)**.

L’échantillon suivant représente l’objet GeoJSON approprié pour désigner deux geofences : une pour le siège de Braze à New York, et l’autre pour la statue de la Liberté au sud de Manhattan. Nous recommandons de télécharger des geofences avec un rayon d’au moins 100 mètres pour qu’elles fonctionnent de manière optimale.

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
    }, ...
  ]
```

Gardez les points suivants à l’esprit au moment de créer vos geofences :

- La valeur des `coordinates` de l’objet GeoJSON est au format [longitude/latitude].
- Le rayon maximal d’une geofence pouvant être téléchargé est de 100 000 mètres (100 kilomètres ou environ 62 miles).

## Utiliser des événements de geofence

Une fois les geofences configurées, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Déclencheurs

Pour utiliser les données de geofence avec des déclencheurs de campagne ou de Canvas, choisissez **Action-Based Delivery (Livraison par événement)** comme méthode de livraison. Ensuite, ajoutez une action de déclenchement `Trigger a Geofence`. Pour finir, choisissez l’ensemble de geofences et les types d’événements de transition de geofence pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l’aide des événements de geofence.

![][2]

### Personnalisation

Pour personnaliser votre message à l’aide des données de geofence, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Foire aux questions

Consultez nos [FAQ sur les geofences][3] pour obtenir des réponses aux questions fréquemment posées sur les geofences.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
