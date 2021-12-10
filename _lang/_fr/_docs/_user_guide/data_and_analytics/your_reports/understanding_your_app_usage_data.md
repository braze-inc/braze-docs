---
nav_title: Vue d'ensemble des données
article_title: Comprendre vos données d'aperçu
page_order: 1
page_type: Référence
description: "Cet article de référence décrit la page d'aperçu et fournit des définitions des statistiques disponibles sur cette page."
tool:
  - Rapports
---

# Comprendre vos données d'aperçu

## Aperçu

La page **aperçu** sur le tableau de bord vous fournit des indicateurs mobiles clés pour suivre et comprendre les performances de votre application et vous donne un coup d'œil à la base d'utilisateurs de votre application. Voici les définitions de ces statistiques, comment nous les calculons et pourquoi elles devraient être importantes pour vous.

!\[Capture d'écran du tableau de bord\]\[1\]

> Vous pouvez cliquer sur **Afficher la ventilation** située sur le côté droit de toutes les lignes des statistiques du tableau de bord pour afficher la valeur de chaque statistique par jour pour la période spécifiée dans la section **Afficher les données pour**.

!\[Expand\]\[2\]

## Utilisateurs à vie

Les utilisateurs à vie représentent le nombre total d'utilisateurs que nous avons enregistrés en utilisant votre application à tout moment. Au-dessous de ce nombre est le pourcentage de combien d'utilisateurs sont représentés en tant qu'utilisateurs actifs mensuels (MAU) qui est utile pour voir la rétention des utilisateurs sur une longue période.

Un faible ratio d'utilisateur MAU/à vie peut indiquer que vous avez besoin de diversifier vos canaux de messagerie ou d'augmenter vos efforts pour atteindre les utilisateurs en difficulté. Voyez notre victoire rapide sur [la capture des utilisateurs de lapsing][3] pour plus d'informations. En général, le ratio MAU / durée de vie diminuera inévitablement avec le temps en raison de la présence de l'utilisateur, mais les outils de Braze peuvent vous aider à minimiser cet effet en maintenant les utilisateurs engagés plus longtemps.

## Sessions à vie

C'est le nombre total de sessions que Braze a enregistrées depuis l'intégration. Bref, une session est à chaque fois qu'un utilisateur utilise l'application. Pour une définition plus précise de la manière dont les sessions sont définies par plate-forme, veuillez visiter le [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-tracking), [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/), ou [articles sur le suivi de session Windows Universal]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/tracking_sessions/).

## Utilisateurs actifs mensuels

Les utilisateurs actifs mensuels (MAU) est le nombre d'utilisateurs qui ont enregistré une session dans votre application au cours des 30 derniers jours. Le MAU est calculé tous les soirs avec une fenêtre roulante de 30 jours. Le pourcentage à côté du nombre de MAU vous donnera une comparaison entre le nombre de MAU d'aujourd'hui et le nombre de MAU enregistré il y a 31 jours. MAU vous donne une bonne compréhension de la santé d'une application sur une longue période de temps en éliminant les incohérences entre les jours d'intensité d'utilisation variable.

Notez que les utilisateurs anonymes seront également pris en compte dans votre MAU. Pour les appareils mobiles, les utilisateurs anonymes sont dépendants de l’appareil. Pour les utilisateurs du web, les utilisateurs anonymes dépendent du cache du navigateur.

## Utilisateurs actifs quotidiens

Les utilisateurs actifs quotidiens (DAU) affichent le nombre d'utilisateurs uniques qui enregistrent au moins une session dans votre application un jour donné. DAU peut être une statistique utile pour examiner la variabilité quotidienne de l'utilisation de votre application et personnaliser vos campagnes de messagerie pour être aussi efficace que possible. Par exemple, L'utilisation de votre application peut voir un pic appréciable le week-end - cela vous informerait que vous pourriez joindre plus d'utilisateurs avec des messages dans l'application ces jours-ci plutôt que les jours de semaine.

## Nouveaux utilisateurs

Les nouveaux utilisateurs vous indiquent combien d'utilisateurs qui n'ont jamais enregistré de session ont commencé à utiliser votre application. Ce nombre est un total de nouveaux utilisateurs au cours de la période donnée. Cette statistique peut être très utile pour suivre l'efficacité de vos efforts publicitaires.

> Lorsque vous publiez initialement votre application avec Braze, tous les utilisateurs ressembleront à de nouveaux utilisateurs puisque Braze n'a jamais enregistré de session pour eux auparavant.

## Adhésif

La valeur de « coloration » de votre application est un rapport entre un dau d'une journée donnée et un mau. par essence, la colle mesure le pourcentage de votre mau qui reviennent sur une base quotidienne. par exemple, un ratio de 50% indique qu'en moyenne, un utilisateur actif utilise l'application pendant 15 jours sur 30 jours, ou qu'environ la moitié de vos utilisateurs actifs reviennent sur une base quotidienne. la colle est une mesure importante pour la réussite de l'application parce que la plupart des utilisateurs ne quittent pas une application parce qu'ils la détestent activement, mais plutôt parce que cela ne fait pas partie de leur routine quotidienne. vous pouvez donc utiliser la coloration comme un proxy pour mesurer à quel point vous vous engagez à engager vos utilisateurs.

{% alert important %}
La valeur MAU est calculée par nuit et ne sera pas mise à jour avant le lendemain.
{% endalert %}

## Sessions quotidiennes

Les sessions quotidiennes sont le nombre de sessions enregistrées sur un jour donné. Comparer cette valeur à votre nombre de DAU peut vous informer du nombre de fois que vos utilisateurs ouvrent l'application les jours où ils enregistrent au moins une session.

## Sessions quotidiennes par MAU

Les sessions quotidiennes par MAU sont le rapport entre les sessions quotidiennes et MAU sur une journée donnée. Ce que cette statistique peut vous dire, c'est combien de sessions par jour vous pouvez vous attendre à avoir enregistré par MAU. Sur l'agrégat, cela peut vous donner une idée de la fréquence relative de l'utilisation de votre application par vos utilisateurs. Autrement dit, si vos sessions quotidiennes par MAU étaient en moyenne 0. , alors vous pouvez vous attendre à ce que chaque MAU enregistre une session tous les 2 jours.
[1]: {% image_buster /assets/img_archive/Usage_Page.png %} [2]: {% image_buster /assets/img_archive/Breakdown.png %}

[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
