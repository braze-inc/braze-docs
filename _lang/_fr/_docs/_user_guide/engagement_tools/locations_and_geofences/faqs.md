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

Braze ne recueille l'emplacement que lorsque l'application est ouverte au premier plan. Résultat: notre filtre `Emplacement le plus récent` cible les utilisateurs en fonction de leur date de dernière ouverture de l'application (également appelé démarrage de la session).

Vous devriez également garder à l'esprit les nuances suivantes :

- Si l'emplacement est désactivé, le filtre `Emplacement le plus récent` affichera le dernier emplacement enregistré.
- Si un utilisateur a déjà eu un emplacement stocké sur son profil, il se qualifiera pour le filtre `Lieu disponible` , Même s'ils ont choisi de ne plus suivre la localisation depuis lors.

### Quelle est la différence entre les filtres de localisation de périphérique le plus récent et ceux les plus récents ?

La `Localisation de périphériques la plus récente` provient des paramètres du périphérique de l'utilisateur. Par exemple, cela apparaît pour les utilisateurs de l'iPhone dans leur appareil sous **Paramètres** > **Général** > **Langue & Région**. Ce filtre est utilisé pour capturer la langue et le formatage régional, tels que les dates et les adresses, et est indépendant du filtre `Position la plus récente`.

La `localisation la plus récente` est la dernière localisation GPS connue de l'appareil. Ceci est mis à jour au démarrage de la session.

### Si un utilisateur choisit de ne pas suivre de localisation, ses anciennes données de localisation seront-elles supprimées du Brésil ?

NON ! Si un utilisateur a déjà eu un emplacement stocké sur son profil, ces données ne seront pas automatiquement supprimées si elles se retirent plus tard du suivi de l'emplacement.

## Géorepérages

### Combien de géorepérages puis-je stocker ?

Par [documentation][3]d'Android, les applications Android ne peuvent stocker que jusqu'à 100 géorepérages localement à la fois. Braze est configuré pour stocker seulement jusqu'à 20 géofences localement par application. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

Les appareils iOS peuvent surveiller jusqu'à 20 [géorepérages][4] à la fois par application. Braze surveillera jusqu'à 20 emplacements si de la place est disponible. Pour que les géorepérages fonctionnent correctement, vous devez vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

### Combien de géorepérages puis-je télécharger en Brésil?

Vous pouvez créer ou télécharger un nombre illimité de géorepérages sur le tableau de bord, permettant à votre équipe de marketing de mettre en place des ensembles et des campagnes de géorepérage sans avoir à calculer le nombre de géofences. Cependant, chaque ensemble de géorepérage peut contenir un maximum de 10 000 géofences. Braze resynchronise dynamiquement les géorepérages qu'il suit pour chaque utilisateur individuel, en veillant à ce que les géorepérages les plus pertinents soient toujours disponibles.

### Quelle est la précision des géorepérages de Braze ?

Les géofences de Braze utilisent une combinaison de tous les fournisseurs de localisation disponibles à un appareil pour trianguler l'emplacement de l'utilisateur. Il s'agit notamment du WiFi, du GPS et des tours cellulaires.

La précision typique est de 20-50m et la meilleure précision des cas sera dans la gamme 5-10m. Dans les zones rurales, la précision peut se dégrader de manière significative, pouvant atteindre plusieurs kilomètres. Braze recommande de créer des géorepérages avec un rayon plus large dans les zones rurales.

### Comment les géofences affectent-elles la durée de vie de la batterie?

Notre solution de géorepérage utilise le service système de géorepérage natif sur iOS et Android et est optimisée pour échanger intelligemment la précision et la puissance assurer une meilleure autonomie de la batterie et une meilleure performance au fur et à mesure que le service sous-jacent s'améliore.

### Quand les géorepérages sont-ils actifs?

Les géorepérages fonctionnent même lorsque votre application est fermée, à toutes les heures de la journée.

### À quelle fréquence les géofences sont-elles actualisées pour les utilisateurs ?

Pour les utilisateurs actifs, le Braze SDK ne demandera des géorepérages qu'une fois par jour au démarrage de la session. Cela signifie que si des modifications sont apportées aux jeux de géorepérage après le démarrage de la session, vous devrez attendre 24 heures à partir de la première fois que les jeux sont tirés vers le bas pour recevoir le jeu mis à jour.

Pour les utilisateurs inactifs, si l'utilisateur est en tâche de fond activé, Braze enverra également une poussée silencieuse toutes les 24 heures pour tirer vers le bas les derniers emplacements de l'appareil.

Vous pouvez mettre à jour manuellement les ensembles de géorepérage pour chaque utilisateur à tout moment en cliquant sur **Re-sync Geofences** dans le coin inférieur de la page **Emplacements**.

{% alert note %}
Si les géorepérages ne sont pas chargés localement sur le périphérique, l'utilisateur ne peut pas déclencher le géorepérage même s'ils entrent dans la zone.
{% endalert %}

### Quelle est la différence entre les géorepérages et la segmentation sur le lieu le plus récent ?

Au Brésil, un géorepérage est un concept différent de la segmentation basée sur la localisation la plus récente. Les géofences ne sont utilisées que pour les déclencheurs, comme l'envoi d'un message lorsqu'un utilisateur entre ou quitte une zone spécifique. Les segments basés sur le filtre `Emplacement le plus récent` sont utilisés pour cibler une région spécifique de votre public, comme l'envoi d'un message aux utilisateurs situés à New York.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
