---
nav_title: FAQ
article_title: FAQ sur les localisations et géorepérages
page_order: 4
page_type: FAQ
description: "Cet article de référence aborde certaines questions fréquemment posées concernant le suivi de la localisation et les géorepérages."
tool: Location

---

# Foire aux questions

> Cette page fournit des réponses aux questions fréquemment posées sur les emplacements/localisations et les géorepérages.

## Suivi de localisation

### Quand Braze recueille-t-il des données de localisation ?

Braze enregistre uniquement les données de localisation lorsque l’application est ouverte en avant-plan. Par conséquent, notre filtre `Most Recent Location` cible les utilisateurs en fonction du dernier endroit où ils ont ouvert l’application (également appelé début de session).

Gardez les nuances suivantes à l’esprit :

- Si le suivi de la géolocalisation est désactivé, le filtre `Most Recent Location` affichera le dernier emplacement enregistré.
- Si un utilisateur a déjà eu un emplacement enregistré sur son profil, il sera éligible pour le filtre `Location Available`, même s’il a désactivé le suivi de la géolocalisation depuis que l’emplacement a été enregistré.

### Quelle est la différence entre le filtre Most Recent Device Locale (Dernière localisation de l’appareil) et Most Recent Location (Dernière localisation) ?

La `Most Recent Device Locale` provient des paramètres de l’appareil de l’utilisateur. Par exemple, pour les utilisateurs d'iPhone, elle apparaît dans leur appareil sous **Réglages** > **Général** > **Langue et région.** Ce filtre est utilisé pour collecter des informations sur la langue et la mise en forme régionale, telles que les dates et adresses, et est indépendant du filtre `Most Recent Location`.

La `Most Recent Location` correspond aux dernières données GPS connues du dispositif. Elle est mise à jour au début de la session et est stockée dans le profil de l'utilisateur.

### Si un utilisateur désactive le suivi de la géolocalisation, leurs anciennes données de géolocalisation seront-elles supprimées de Braze ?

Non ! Si un utilisateur a déjà eu un emplacement enregistré sur son profil, ces données ne seront pas automatiquement supprimées même si cet utilisateur désactive le suivi de la géolocalisation ultérieurement.

## Géorepérages

### Quelle est la différence entre les géorepérages et le suivi de la localisation ?

Dans Braze, un géorepérage est un concept différent du suivi de la localisation. Les géorepérages sont utilisés comme déclencheurs de certaines actions. Un géorepérage est une frontière virtuelle établie autour d'un emplacement géographique. Lorsqu'un utilisateur entre ou sort de cette frontière, il peut déclencher une action spécifique, comme l'envoi d'un message.

La géolocalisation est utilisée pour collecter et stocker les données d'emplacement/localisation les plus récentes d'un utilisateur. Ces données peuvent être utilisées pour segmenter les utilisateurs en fonction du filtre `Most Recent Location`. Par exemple, vous pouvez utiliser le filtre `Most Recent Location` pour cibler une région spécifique de votre audience, par exemple en envoyant un message aux utilisateurs situés à New York.

### Quel est le niveau de précision des géorepérages de Braze ?

Les géorepérages de Braze utilisent une combinaison de tous les outils de géolocalisation disponibles sur un appareil pour trianguler l’emplacement de l’utilisateur. Ces outils incluent, entre autres, le WI-FI, le GPS et les antennes-relais.

La précision type est de 20 à 50 m et le plus haut degré de précision est compris entre 5 et 10 m. Dans les zones rurales, la précision peut se dégrader considérablement, potentiellement sur plusieurs kilomètres. Braze recommande de créer des géorepérages avec des rayons plus importants pour les zones rurales.

Pour plus d'informations sur la précision des géorepérages, reportez-vous à la documentation [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) et [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Comment les géorepérages affectent-elles la durée de vie de la batterie ?

Notre solution de géorepérage utilise le service de système de géorepérage natif d’iOS et Android et est réglée pour équilibrer de manière intelligente la précision et la performance, garantissant ainsi une durée de vie optimale de la batterie ainsi que des améliorations de performances lorsque le service sous-jacent est amélioré.

### Quand les géorepérages sont-elles actives ?

Les géorepérages de Braze fonctionnent à toute heure de la journée, même lorsque votre application est fermée. Ils deviennent actifs dès qu'ils sont définis et téléchargés dans le tableau de bord de Braze. Cependant, les géorepérages ne peuvent pas fonctionner si l'utilisateur a désactivé le suivi de la localisation.

Pour que les géorepérages fonctionnent, les utilisateurs doivent avoir activé les services d'emplacement/localisation sur leur appareil et avoir autorisé votre appli à accéder à leur emplacement. Si un utilisateur a désactivé le suivi de la localisation, votre appli ne pourra pas détecter quand il entre ou sort d'un géorepérage.

### Les données de géorepérage sont-elles stockées dans les profils utilisateurs ?

Non, Braze ne stocke pas de données de géorepérage dans les profils utilisateurs. Les géorepérages font l’objet d’une surveillance par les services de localisation d'Apple et de Google, et Braze n'est averti que lorsqu'un utilisateur déclenche un géorepérage. À ce stade, nous traitons toutes les campagnes de déclenchement associées.

### Puis-je définir un géorepérage au sein d’un géorepérage ?

En tant que bonne pratique, évitez d’utiliser des géorepérages imbriquées, car cela pourrait entraîner des problèmes de déclenchement des notifications.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
