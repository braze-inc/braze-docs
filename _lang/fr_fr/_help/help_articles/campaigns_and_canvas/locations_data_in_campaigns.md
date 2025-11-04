---
nav_title: Vérification des données de localisation
article_title: Vérification des données de localisation
page_order: 1
page_type: solution
description: "Cet article d’aide décrit des vérifications rapides qui peuvent vous aider si aucun utilisateur n’a des données de localisation."
tool: Location
---

# Vérification des données de localisation

Par défaut, le SDK Braze capture la localisation la plus récente d’un utilisateur. Cela signifie généralement que « l’emplacement récent » est l’endroit à partir duquel votre utilisateur a récemment utilisé votre application. Si vous envoyez des données de localisation Braze en arrière-plan, vous aurez peut-être des données plus granulaires.

Si aucun utilisateur n'a de lieux disponibles, deux vérifications rapides peuvent vous aider à confirmer la collecte des données et le transfert de la date.

## Collecte de données

Confirmez que votre application recueille les données de localisation :

- Pour iOS, cela signifie que les utilisateurs choisissent de partager leurs données de localisation via une invite à un moment donné du parcours utilisateur. 
- Pour Android, assurez-vous que votre application demande des autorisations de localisation fine ou grossière lors de l’installation.

Pour voir si les données de localisation de l'utilisateur sont envoyées à Braze, utilisez le filtre **Location Available**. Ce filtre vous permet de voir le pourcentage d’utilisateurs avec un « emplacement le plus récent ».

![]({% image_buster /assets/img_archive/trouble7.png %})

## Transfert de données

Confirmez auprès de vos développeurs que les données de localisation sont bien transmises à Braze. Normalement, la transmission des données de localisation est gérée automatiquement par le SDK après que l'utilisateur a donné les autorisations, mais vos développeurs ont peut-être désactivé le suivi de localisation dans Braze. Vous trouverez plus d’informations sur le suivi des données de localisation pour :
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 16 novembre 2022_

