---
nav_title: Intégrations mobiles
article_title: Intégrations des geofences pour appareils mobiles
page_order: 2
page_type: reference
description: "Cet article de référence aborde les intégrations mobiles nécessaires pour utiliser les geofences."
tool: Location

---

# Intégrations mobiles

> Cet article de référence aborde les intégrations mobiles nécessaires pour utiliser les geofences.

## Exigences interplateformes

Des campagnes déclenchées par geofence sont disponibles sur iOS et Android. Pour prendre en charge les geofences, assurez-vous de respecter les points ci-dessous :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les geofences de Braze ou la collecte des données de localisation doivent être activés.
3. Pour les appareils iOS version 11 et ultérieure, les utilisateurs doivent toujours permettre l’accès aux données de localisation pour que les geofences fonctionnent.

{% alert important %}
À partir de la version 3.6.0 du SDK de Braze pour Android, la collecte des données de localisation de Braze est désactivée par défaut. Pour vérifier que la collecte des données de localisation est activée sur Android, assurez-vous que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

## Configuration des geofences

### Latitude et longitude

Le centre géographique de la geofence.

### Rayon

Le rayon de la geofence exprimé en mètres et mesuré par son centre géographique. Nous recommandons de définir un rayon minimum de 100 mètres pour toutes les geofences.

### Temps de récupération

Les utilisateurs reçoivent des notifications déclenchées par geofence après être entrés ou sortis de geofences distinctes. Ces transitions sont suivies d’une période prédéfinie pendant laquelle l’utilisateur ne peut pas effectuer la même transition par rapport à cette geofence. Cette période est appelée « temps de récupération » et est prédéfinie par Braze. Son principal objectif est d’éviter les requêtes réseau inutiles.

## Foire aux questions

Consultez notre [FAQ sur les geofences][5] pour obtenir des réponses aux questions fréquemment posées sur les geofences.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
