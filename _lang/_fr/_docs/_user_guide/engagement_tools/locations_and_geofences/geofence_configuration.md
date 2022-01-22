---
nav_title: Configuration du Geofence
article_title: Configuration du Geofence
page_order: 3
page_type: Référence
description: "Cet article de référence couvre diverses configurations de Geofence."
tool: Localisation
---

# Configuration du géorepérage

> Cet article de référence couvre diverses options de configuration de Geofence disponibles lors de la création de jeux de géorepéres.

## Latitude et longitude

Le centre géographique du géorepérage.

## Radius

Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Nous vous recommandons de fixer un rayon minimum de 100 mètres pour tous les géofences.

## Refroidissement

Les utilisateurs reçoivent des notifications déclenchées par géorepérage après l'entrée ou la sortie des géorepérages individuels. Après une transition, il y a une période de temps au cours de laquelle l'utilisateur peut ne pas effectuer la même transition sur cette fonction individuelle. Cette période de temps est appelée le « temps de recharge » et est prédéfinie par Braze comme 6 heures.

Si l'application est réinstallée, le refroidissement sera réinitialisé. Les temps de récupération sont par géorepérage et séparent pour l'entrée et la sortie, afin qu'un utilisateur puisse déclencher l'entrée et la sortie dans les 6 heures sur la même géorepérage, mais pas deux fois pour l'entrée ou deux fois pour la sortie.

Le but principal du temps de recharge est d'éviter les requêtes réseau inutiles.

## Partenaires technologiques

Vous pouvez également tirer parti des géorepérages avec certains de nos partenaires, par exemple :

- [Neura][1]
- [Radar][2]
- [Foursquare][3]

[1]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura_actions/
[2]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[3]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/