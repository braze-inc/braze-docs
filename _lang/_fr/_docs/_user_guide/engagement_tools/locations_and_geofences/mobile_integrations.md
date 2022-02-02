---
nav_title: Intégrations mobiles
article_title: Intégrations de Geofence Mobile
page_order: 2
page_type: Référence
description: "Cet article de référence couvre les intégrations nécessaires à l'utilisation de Geofences."
tool: Localisation
---

# Intégrations mobiles

## Exigences inter-plateformes

Les campagnes déclenchées par le géofence sont disponibles sur iOS et Android. Pour soutenir les géofences, ce qui suit doit être en place :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages ou la collecte de localisation doivent être activés.
3. Pour les appareils sur iOS version 11 et supérieure, l'utilisateur doit toujours autoriser l'accès à la localisation pour que le géorepérage fonctionne.

{% alert important %}
La collection d'emplacement Braze SDK 3.6.0 Braze est désactivée par défaut. Pour vérifier que la collection d'emplacement est activée sur Android, assurez-vous que `com_braze_enable_location_collection` est défini à `true` dans votre `braze.xml`.
{% endalert %}

## Configuration du géorepérage

### Latitude et longitude

Le centre géographique du géorepérage.

### Radius

Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Nous vous recommandons de fixer un rayon minimum de 100 mètres pour tous les géofences.

### Refroidissement

Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géorepérages individuels. Après une transition, il y a une période de temps prédéfinie au cours de laquelle l'utilisateur peut ne pas effectuer à nouveau la même transition sur cette fonction individuelle. Cette période de temps est appelée le « temps de recharge » et est prédéfinie par le Brésil. Son principal objectif est d'éviter les requêtes réseau inutiles.

## Foire aux questions

Visitez notre page [FAQ][5] de Geofence pour les réponses aux questions les plus fréquemment posées sur les géofences.

[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
