---
nav_title: Intégrations mobiles
article_title: Intégrations des géorepérages pour appareils mobiles
page_order: 2
page_type: reference
description: "Cet article de référence couvre les intégrations mobiles nécessaires à l'utilisation des géorepérages."
tool: Location

---

# Intégrations mobiles

> Cet article de référence couvre les intégrations mobiles nécessaires à l'utilisation des géorepérages.

## Exigences interplateformes

Des campagnes déclenchées par géorepérage sont disponibles sur iOS et Android. Pour prendre en charge les géorepérages, assurez-vous de respecter les points ci-dessous :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages de Braze ou la collecte des données de localisation doivent être activés.
3. Pour les appareils iOS version 11 et ultérieure, les utilisateurs doivent toujours permettre l’accès aux données de localisation pour que les géorepérages fonctionnent.

{% alert important %}
À partir de la version 3.6.0 du SDK de Braze, la collecte des emplacements/localisations est désactivée par défaut. Pour vérifier qu'il est activé sur Android, confirmez que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

## Configuration des géorepérages

### Latitude et longitude

Le centre géographique de la géorepérage.

### Rayon

Le rayon de la géorepérage exprimé en mètres et mesuré par son centre géographique. Nous vous recommandons de définir un rayon minimum de 100 à 150 mètres pour tous les géorepérages.

Reportez-vous à ces guides pour plus d'informations en fonction de votre plateforme :
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### Temps de récupération

Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géofences individuelles. Après une transition, il existe un délai prédéfini pendant lequel l'utilisateur ne peut plus effectuer la même transition sur ce géorepérage individuel. Ce temps est appelé "cooldown" et est prédéfini par Braze. Son principal objectif est d’éviter les requêtes réseau inutiles.

### Partenaires technologiques

Vous pouvez également tirer parti des géorepérages avec certains de nos partenaires, par exemple : 

- [Radar][12]
- [Foursquare][13]

## Foire aux questions

Consultez notre [FAQ sur les géorepérages][5] pour obtenir des réponses aux questions fréquemment posées sur les géorepérages.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

