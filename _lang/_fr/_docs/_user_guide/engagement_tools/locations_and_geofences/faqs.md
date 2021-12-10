---
nav_title: Foire aux questions
article_title: Foire aux questions sur les emplacements & les géofences
page_order: 4
page_type: Foire Aux Questions
description: "Cet article de référence couvre certaines questions fréquemment posées concernant l'utilisation de Geofences."
tool: Localisation
---

# FAQ sur les lieux et les géorepérages

## Emplacements

### Quand Braze recueille-t-il les données de localisation ?

Braze ne recueille l'emplacement que lorsque l'application est au premier plan. Par conséquent, nos derniers filtres de localisation connus ciblent les utilisateurs en fonction de leur date de dernière ouverture.

## Géorepérages

### Puis-je stocker plus de X géo-encres ?

Par [documentation][3]d'Android, les applications Android ne peuvent stocker que jusqu'à 100 géorepérages localement à la fois. Braze est configuré pour stocker seulement jusqu'à 20 géofences localement par application. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

Les appareils iOS peuvent surveiller jusqu'à 20 [géorepérages][4] à la fois par application. Braze surveillera jusqu'à 20 emplacements si de la place est disponible. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

### Quelle est la précision des géorepérages de Braze ?

Les géofences de Braze utilisent une combinaison de tous les fournisseurs de localisation disponibles à un appareil pour trianguler l'emplacement de l'utilisateur. Il s'agit notamment du Wifi, du GPS et des tours cellulaires.

La précision typique est de 20-50m et la meilleure précision des cas sera dans la gamme 5-10m. Dans les zones rurales, la précision peut se dégrader de manière significative, pouvant atteindre plusieurs kilomètres. Braze recommande de créer des géorepérages avec un rayon plus large dans les zones rurales.

### Comment les géofences affectent-elles la durée de vie de la batterie?

Notre solution de géorepérage utilise le service système de géorepérage natif sur iOS et Android et est optimisée pour échanger intelligemment la précision et la puissance assurer une meilleure autonomie de la batterie et une meilleure performance au fur et à mesure que le service sous-jacent s'améliore.

### Combien de géorepérages puis-je télécharger en Brésil?

Vous pouvez créer ou télécharger un nombre illimité de géorepérages sur le tableau de bord, permettant à votre équipe de marketing de mettre en place des ensembles et des campagnes de géorepérage sans avoir à calculer le nombre de géofences. Cependant, chaque ensemble de géorepérage peut contenir un maximum de 10 000 géofences. Braze resynchronise dynamiquement les géorepérages qu'il suit pour chaque utilisateur individuel, en veillant à ce que les géorepérages les plus pertinents soient toujours disponibles.

### Quand les géorepérages sont-ils actifs?

Les géorepérages fonctionnent même lorsque votre application est fermée, à toutes les heures de la journée.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
