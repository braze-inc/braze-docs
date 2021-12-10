---
nav_title: Création de géorepérages
article_title: Création de géorepérages
page_order: 1
page_type: Référence
description: "Cet article de référence couvre la façon de créer et de configurer Geofences."
tool:
  - Localisation
---

# Géorepérages

> cet article de référence couvre la façon de créer et de configurer des géofences.

Au cœur de l'offre de l'emplacement en temps réel de Braze se trouve le concept de "géorepérage". Un géorepérage est une zone géographique virtuelle, représentée par des paires de latitude/longitude combinées à un rayon, formant un cercle dans une position spécifique sur le globe. Les Geofences peuvent varier de la taille d'un bâtiment à la taille d'une ville entière.

Vous pouvez définir des géorepérages sur le tableau de bord de Braze et déclencher des campagnes en temps réel lorsque les utilisateurs entrent et les quittent à travers le monde. Les géofences sont profondément intégrées dans les capacités de segmentation et de messagerie de Brase. Les campagnes peuvent être livrées en temps réel aux utilisateurs lorsqu'ils quittent ou entrent dans les géofences, ou envoyées sous forme de suivi des heures ou des jours plus tard. Au fur et à mesure que les utilisateurs saisissent ou quittent vos géorepérages, ils ajoutent une nouvelle couche de données utilisateur qui peut être utilisée pour la segmentation et le re-ciblage.

Les géorepérages sont gérés dans la page **Emplacements** dans la section **Engagement**. Les géorepérages sont organisés en ensembles de géorepérage - un groupe de géorepérages qui peuvent être utilisés pour segmenter ou engager les utilisateurs sur toute la plate-forme. Les ensembles d'exemples de géorepérage incluent `Tous les magasins régionaux du nord-est` ou `les événements de septembre`. Un ensemble de géorepérage donné ne peut contenir que 10 000 géorepéres.

## Création manuelle de jeux de géorepérage

!\[Écran principal d'emplacement Geofence\]\[1\]

Une fois que vous avez créé un ensemble de géorepérages, vous pouvez ajouter manuellement des géorepérages en les dessinant sur la carte. Nous recommandons de créer des géorepérages avec un rayon d'au moins 100 mètres pour une fonctionnalité optimale.

## Création des ensembles de géorepérage via envoi groupé

Les géorepérages peuvent être téléchargés en vrac en tant qu'objet GeoJSON de type `FeatureCollection`. Chaque géorepérage individuel est un type de géométrie `point` dans la collection de fonctionnalités. Les propriétés de chaque fonctionnalité requièrent une clé `"radius"` et une clé facultative `"nom"` pour chaque géorepérage.

L'échantillon ci-dessous représente le GeoJSON correct pour spécifier deux géoreences: un pour le siège de Braze à NYC, et un pour la Statue de la Liberté au sud de Manhattan. Nous recommandons de télécharger des géorepérages avec un rayon d'au moins 100 mètres pour une fonctionnalité optimale.

```
{
  "type": "FeatureCollection",
  "caractéristiques": [
    {
      "type": "Fonctionnalité",
      "géométrie": {
        "type": "Point",
        "coordonnées": [-73. 92473, 40. 55669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Fonctionnalité",
      "géométrie": {
        "type": "Point",
        "coordonnées": [-74. 44468, 40. 89225]
       },
      "propriétés": {
        "radius": 100,
        "name": "Statue de la Liberté"
      }
    }, ...
  ]
```
> La valeur "coordonnées" dans le GeoJSON doit être formatée [Longitude, Latitude]

> Le rayon maximal de géorepérage qui peut être téléchargé est de 100000 mètres (100km/62mi).

## Utiliser les événements de géorepérage

Une fois les géorepérages configurés, vous pouvez les utiliser pour améliorer et enrichir la façon dont vous communiquez avec vos utilisateurs.

### Déclenchement

Pour utiliser les données de géorepérage dans le cadre de la campagne et des déclencheurs de Canvan, choisissez « la livraison basée sur l'action » pour sa méthode de livraison. Ensuite, ajoute une action de déclenchement de `déclenche une zone de géorepérage`. Enfin, choisissez les types d'événements de transition de géorepérage et de géorepérage pour votre message. Vous pouvez également faire avancer les utilisateurs à travers un Canvas en utilisant des événements de géorepérage.

!\[action_based_geofence_trigger\]\[2\]

### Personnalisation

Pour utiliser les données de géorepérage pour personnaliser un message, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`

* `{{event_properties.${geofence_set_name}}}`
{% endraw %}
[1]: {% image_buster /assets/img_archive/locations_main_screen.png %} [2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
