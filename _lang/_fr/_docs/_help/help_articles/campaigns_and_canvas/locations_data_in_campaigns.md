---
nav_title: Vérification des données de localisation
article_title: Vérification des données de localisation
page_order: 1
page_type: Solution
description: "Cet article d'aide vous guide à travers des vérifications rapides qui peuvent vous aider si aucun utilisateur n'a de lieux disponibles."
tool: Localisation
---

# Vérification des données de localisation

Braze capture par défaut l'emplacement le plus récent d'un utilisateur via son SDK. Cela signifie généralement que la « localisation récente » est l'endroit où votre utilisateur a utilisé votre application la plus récente. Si vous envoyez des données de localisation en arrière-plan de Braze, vous pouvez avoir plus de données granulaires disponibles.

Si aucun utilisateur n'a d'emplacement disponible, il y a deux vérifications rapides qui peuvent vous aider :

* [Confirmer la collecte de données](#confirm-data-collection)
* [Confirmer le transfert de données](#confirm-data-transfer)

## Confirmer la collecte de données

Confirmez que votre application collecte les données de localisation :

- Pour iOS, cela signifie que les utilisateurs choisissent de partager leurs données de localisation via une invite à un moment donné du voyage de l'utilisateur.
- Pour Android, confirmez que votre application demande des autorisations de localisation correctes ou grossières lors de l'installation.

Afin de voir si les données de localisation de l'utilisateur sont envoyées à Braze, utilisez le filtre « emplacement disponible». Ce filtre vous permettra de voir le pourcentage d'utilisateurs pour lesquels vous avez un « emplacement le plus récent ».

!\[trouble7\]\[25\]

## Confirmer le transfert de données

Confirmez que vos développeurs passent des données de localisation à Braze. Normalement, le passage des données d'emplacement est géré automatiquement par le SDK une fois que l'utilisateur donne les autorisations, mais il est possible que vos développeurs aient désactivé le suivi de la localisation en Brésil. Plus d'informations sur le suivi de la localisation peuvent être trouvées pour:
- [Android][26]
- [iOS][27]
- [Web][28]

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 27 mars 2019_
[25]: {% image_buster /assets/img_archive/trouble7.png %}

[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
