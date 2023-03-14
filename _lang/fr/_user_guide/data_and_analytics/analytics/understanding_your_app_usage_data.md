---
nav_title: Données d’aperçu
article_title: Comprendre vos données d’aperçu
page_order: 1
page_type: reference
description: "Cet article de référence décrit la page Aperçu et décrit les statistiques disponibles sur cette page."
tool: 
  - Rapports

---

# Comprendre vos données d’aperçu

## Aperçu

La page **Overview** du tableau de bord fournit des valeurs mobiles clés que vous pouvez suivre pour analyser la performance de votre appli et obtenir instantanément une compréhension de haut-niveau de votre base d’utilisateurs. Voici les définitions de ces statistiques, comment nous les calculons et pourquoi elles devraient être importantes pour vous.

![Capture d’écran du tableau de bord][1]

> Vous pouvez cliquer sur **Show Breakdown (Afficher la répartition)** pour chaque ligne des statistiques du tableau de bord pour afficher la valeur de chaque statistique par jour pour la période spécifiée dans la section **Display Data For (Afficher les données pour)**.

![Développer][2]

## Utilisateurs à vie

Lifetime Users est le nombre total d’utilisateurs créés dans ce groupe d’apps. Cela inclut tous les utilisateurs que nous avons enregistrés à l’aide de votre application, et ceux qui pourraient ne pas être associés à une application ou un site Web spécifique. Ce nombre est le pourcentage du nombre de vos utilisateurs à vie représentés par dans les utilisateurs actifs mensuels (MAU), ce qui est utile pour voir la rétention à long terme des utilisateurs.

Un faible ratio MAU/Utilisateurs à vie peut indiquer que vous devez diversifier vos canaux de communication ou faire plus d’efforts pour atteindre les utilisateurs inactifs. Découvrez notre « quick win » sur la [capture des utilisateurs inactifs][3] pour plus d’informations. En général, le rapport MAU/Lifetime diminue inévitablement au fil du temps en raison de l’attrition des utilisateurs, mais les outils Braze peuvent vous aider à minimiser cet effet en prolongeant l’engagement des utilisateurs.

## Sessions à vie

Il s’agit du nombre total de sessions que Braze a enregistrées depuis l’intégration. Pour faire bref, une session, c’est à chaque fois qu’un utilisateur utilise l’application. Pour une définition plus précise sur la manière dont les sessions sont définies par la plateforme, consultez ces articles techniques sur le suivi des sessions pour 
[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-tracking), [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/) ou [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/).

## Utilisateur actif par mois

Les utilisateurs actifs par mois (MAU) sont le nombre d’utilisateurs qui ont enregistré une session dans votre application au cours des 30 derniers jours. Les MAU sont calculés chaque soir pour une fenêtre glissante de 30 jours. Le pourcentage à côté du nombre de MAU vous permet de comparer votre nombre de MAU actuel par rapport à votre nombre de MAU enregistré il y a 31 jours. Les MAU donnent une bonne indication de la santé d’une application sur une période prolongée, car cette statistique lisse les incohérences liées à la différence d’utilisation de l’appli certains jours.

Notez que les utilisateurs anonymes sont également comptabilisés dans votre MAU. Pour les appareils mobiles, les utilisateurs anonymes dépendent de l’appareil. Pour les utilisateurs Web, les utilisateurs anonymes dépendent du cache de navigateur.

## Utilisateurs actifs quotidiens

Utilisateurs actifs quotidiens (DAU) affiche le nombre d’utilisateurs uniques qui ont au moins une session dans votre application dans une journée donnée. Le nombre d’utilisateurs actifs par jour peut être une statistique utile pour examiner la variabilité quotidienne de l’utilisation de votre application et adapter vos campagnes de communication pour optimiser leur efficacité. Par exemple, vous verrez peut-être une amélioration appréciable de l’utilisation de votre appli les weekends - c’est un signe que vous pourriez atteindre davantage d’utilisateurs avec des messages in-app envoyés le samedi et le dimanche plutôt qu’en semaine.

## Nouveaux utilisateurs

Les nouveaux utilisateurs vous indiquent combien d’utilisateurs qui n’avaient jamais lancé une session ont commencé à utiliser votre application. Ce nombre est un total de nouveaux utilisateurs sur la période donnée. Cette statistique peut être très utile pour suivre l’efficacité de vos efforts marketing.

>  Lorsque vous publiez votre application dans Braze, tous les utilisateurs seront de nouveaux utilisateurs puisque Braze n’a jamais enregistré de session pour eux auparavant.

## Adhérence

« L’adhérence » de votre appli est un ratio DAU/MAU un jour donné. L’adhérence mesure le pourcentage de votre MAU qui revient quotidiennement. Ainsi un ratio de 50 % indique qu’un utilisateur actif utilise l’application un jour sur deux en moyenne, ou qu’environ la moitié de vos utilisateurs reviennent quotidiennement. C’est un indicateur important du succès de votre appli. En effet, la plupart des utilisateurs n’arrêtent pas d’utiliser une appli parce qu’ils la détestent, mais plutôt parce qu’elle ne parvient pas à rentrer dans leur routine quotidienne. Vous pouvez donc utiliser l’adhérence pour mesurer le niveau d’engagement de vos utilisateurs. 

{% alert important %}
La valeur MAU est calculée chaque soir et ne sera pas mise à jour jusqu’au lendemain.
{% endalert %}

## Sessions quotidiennes

Les sessions quotidiennes sont le nombre de sessions enregistrées sur une journée donnée. L’analyse de cette valeur dans votre nombre d’utilisateurs actifs par jour peut vous indiquer combien de fois vos utilisateurs ouvrent l’application les jours où ils enregistrent au moins une session.

## Sessions quotidiennes par MAU

Les sessions quotidiennes par MAU sont le ratio Sessions Quotidiennes/MAU un jour donné. Cette statistique peut vous informer sur le nombre de sessions quotidiennes que vous pouvez attendre pour chaque MAU. Agrégées, ces données vous renseignent sur la fréquence relative de l’utilisation de votre application par vos utilisateurs. Par exemple, si vos Sessions Quotidiennes par MAU ont une moyenne de 0,5, vous pouvez alors vous attendre à ce que chaque MAU fasse une session tous les 2 jours environ.  

[1]: {% image_buster /assets/img_archive/Usage_Page.png %}
[2]: {% image_buster /assets/img_archive/Breakdown.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
