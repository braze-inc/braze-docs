---
nav_title: Configuration du Geofence
article_title: Configuration du Geofence
page_order: 3
page_type: Référence
description: "Cet article de référence couvre diverses configurations de Geofence."
tool: Localisation
---

# Configuration du géorepérage

## Latitude et longitude

Le centre géographique du géorepérage.

## Radius

Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Nous vous recommandons de fixer un rayon minimum de 100 mètres pour tous les géofences.

## Refroidissement

Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géorepérages individuels. Après une transition, il y a une période de temps prédéfinie au cours de laquelle l'utilisateur peut ne pas effectuer à nouveau la même transition sur cette fonction individuelle. Cette période de temps est appelée le « temps de recharge » et est prédéfinie par le Brésil. Son principal objectif est d'éviter les requêtes réseau inutiles.

## Partenaires technologiques

Vous pouvez également tirer parti des géorepérages avec certains de nos partenaires, par exemple :

- [Neura][1]
- [Radar][2]
- [Foursquare][3]

[1]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura_actions/
[2]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[3]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/