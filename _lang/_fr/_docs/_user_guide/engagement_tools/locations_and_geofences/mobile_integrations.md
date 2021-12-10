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
La collection d'emplacement Braze SDK 3.6.0 Braze est désactivée par défaut. Pour vérifier que la collection d'emplacement est activée sur Android, assurez-vous que `com_appboy_enable_location_collection` est défini à `true` dans votre `braze.xml`.
{% endalert %}

## Configuration du géorepérage

### Latitude et longitude

Le centre géographique du géorepérage.

### Radius

Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Nous vous recommandons de fixer un rayon minimum de 100 mètres pour tous les géofences.

### Refroidissement

Les utilisateurs reçoivent des notifications déclenchées par la géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géorepérages individuels. Après une transition, il y a une période de temps prédéfinie au cours de laquelle l'utilisateur peut ne pas effectuer à nouveau la même transition sur cette fonction individuelle. Cette période de temps est appelée le « temps de recharge » et est prédéfinie par le Brésil. Son principal objectif est d'éviter les requêtes réseau inutiles.

## Foire aux questions

##### Comment les géofences affectent-elles la durée de vie de la batterie?

Notre solution de géorepérage utilise le service système de géorepérage natif sur iOS et Android et est optimisée pour échanger intelligemment la précision et la puissance assurer une meilleure autonomie de la batterie et une meilleure performance au fur et à mesure que le service sous-jacent s'améliore.

##### Combien de géorepérages puis-je télécharger en Brésil?

Vous pouvez créer ou télécharger un nombre illimité de géorepérages sur le tableau de bord, permettant à votre équipe de marketing de mettre en place des ensembles et des campagnes de géorepérage sans avoir à calculer le nombre de géofences. Cependant, chaque ensemble de géorepérage peut contenir un maximum de 10 000 géofences. Braze resynchronise dynamiquement les géorepérages qu'il suit pour chaque utilisateur individuel, en veillant à ce que les géorepérages les plus pertinents soient toujours disponibles.

##### Puis-je stocker plus de X géo-encres ?

Par [documentation][3]d'Android, les applications Android ne peuvent stocker que jusqu'à 100 géorepérages localement à la fois. Braze est configuré pour stocker seulement jusqu'à 20 géofences localement par application. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

Les appareils iOS peuvent surveiller jusqu'à 20 [géorepérages][4] à la fois par application. Braze surveillera jusqu'à 20 emplacements si de la place est disponible. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

##### Quand les géorepérages sont-ils actifs?

Les géorepérages fonctionnent même lorsque votre application est fermée, à toutes les heures de la journée.

##### Quelle est la précision des géorepérages de Braze ?

Les géofences de Braze utilisent une combinaison de tous les fournisseurs de localisation disponibles à un appareil pour trianguler l'emplacement de l'utilisateur. Il s'agit notamment du Wifi, du GPS et des tours cellulaires.

La précision typique est de 20-50m et la meilleure précision des cas sera dans la gamme 5-10m. Dans les zones rurales, la précision peut se dégrader de manière significative, pouvant atteindre plusieurs kilomètres. Braze recommande de créer des géorepérages avec un rayon plus large dans les zones rurales.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
