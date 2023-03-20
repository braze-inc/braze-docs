---
nav_title: Configuration des geofences
article_title: Configuration des geofences
page_order: 3
page_type: reference
description: "Cet article de référence présente plusieurs options de configuration des geofences."
tool: Position

---

# Configuration des geofences

> Cet article de référence présente les options de configuration disponibles pour les geofences au moment de créer des ensembles de geofences.

## Latitude et longitude

Le centre géographique de la geofence.

## Rayon

Le rayon de la geofence exprimé en mètres et mesuré depuis son centre géographique. Nous recommandons de définir un rayon minimum de 200 mètres pour toutes les geofences. Seules les geofences se trouvant dans un rayon de 2 000 kilomètres sont envoyées à l’appareil des utilisateurs.

## Temps de récupération

Les utilisateurs reçoivent des notifications déclenchées par la geofence après être entrés ou sortis de geofences distinctes. Ces transitions sont suivies d’une période pendant laquelle l’utilisateur ne peut pas effectuer la même transition par rapport à cette geofence. Cette période est appelée « temps de récupération » et est prédéfinie par Braze sur six heures.

Si l’application est réinstallée, le temps de récupération le sera également. Les temps de récupération des geofences sont calculés individuellement et séparés pour les entrées et les sorties. Un utilisateur peut déclencher une geofence en entrant puis en sortant de la zone dans un délai de 6 heures, mais pas deux fois pour une entrée ou deux fois pour une sortie.

L’objectif principal du temps de récupération est d’éviter les requêtes réseau inutiles.

## Technology Partners

Vous pouvez également tirer parti des geofences avec certains de nos partenaires, par exemple : 

- [Radar][2]
- [Foursquare][3]

[2]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[3]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/