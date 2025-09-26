---
nav_title: "Tableau de bord de l'accueil"
article_title: "Tableau de bord de l'accueil (Aperçu précédent)"
page_order: 1
page_type: reference
description: "Cet article de référence décrit votre tableau de bord Accueil et fournit des définitions pour les statistiques disponibles sur cette page."
tool: 
  - Reports

---

# Tableau de bord de l'accueil

> La page **Accueil** du tableau de bord fournit des indicateurs clés qui vous permettent de suivre et de comprendre les performances de votre appli ou de votre site web, et vous donne un aperçu de haut niveau de votre base d'utilisateurs.

La page d **'accueil** comporte deux sections principales :
- [Reprendre là où vous vous êtes arrêté](#pick-up-where-you-left-off)
- [Aperçu des performances](#peformance-overview)

![Tableau de bord de Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Reprendre là où vous vous êtes arrêté

Vous pouvez reprendre là où vous vous étiez arrêté dans le tableau de bord de Braze, avec un accès direct aux fichiers que vous avez récemment modifiés ou créés. Cette section apparaît en haut de la page d **'accueil** du tableau de bord de Braze.

Vous pouvez revenir sur des campagnes, des canvas et des segments récemment modifiés ou créés. Chaque carte est associée à des tags qui indiquent le type de contenu (campagne, Canvas, segment) et le statut (actif, brouillon, archivé, arrêté).

![Un projet de canvas, un segment actif et un projet de campagne dans la section "Reprenez là où vous vous êtes arrêté".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Aperçu des performances

Par défaut, la section **Aperçu des performances** affiche les données des 30 derniers jours pour toutes les apps et tous les sites. Vos indicateurs sont tous calculés sur la base de la plage de dates sélectionnée.

![Champs de date et d'application sur le tableau de bord de l'accueil.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Les pourcentages sont calculés sur la base de la plage de dates actuelle par rapport à la plage de dates précédente, à l'exception des *Utilisateurs actifs mensuels* (MAU), qui utilisent le dernier jour de la période précédente au lieu d'une plage. 

Par exemple, si vous définissez votre plage de dates sur les **7 derniers jours** et que votre *nombre d'utilisateurs actifs quotidiens* affiche un pourcentage d'augmentation de 1,8 %, cela signifie que vous avez eu 1,8 % d'utilisateurs actifs quotidiens en plus cette semaine par rapport à la semaine dernière.

![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Afficher la répartition

Sélectionnez **Afficher la décomposition** pour chaque ligne des statistiques de l'aperçu des performances afin d'afficher la valeur de chaque statistique par jour pour la plage de dates spécifiée.

![Développez]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## Statistiques disponibles

Vous trouverez ci-dessous les définitions des statistiques dont vous disposez, la manière dont nous les calculons et les raisons pour lesquelles elles sont importantes pour vous.

### Utilisateurs

*Utilisateurs* est le nombre total d'utilisateurs créés dans cet espace de travail. Il s'agit de tous les utilisateurs que nous avons enregistrés et qui utilisent votre application ou votre site web à un moment donné, ainsi que ceux qui ne sont pas associés à une application ou à un site web spécifique. Ce chiffre correspond au pourcentage de vos utilisateurs actifs *mensuels* (MAU), ce qui est utile pour évaluer la fidélisation des utilisateurs sur une longue période.

Un faible ratio MAU/utilisateur peut indiquer que vous devez diversifier vos canaux de communication ou redoubler d'efforts pour atteindre les utilisateurs en fin de carrière. Pour plus d'informations, reportez-vous à notre solution rapide pour [capturer les utilisateurs qui perdent leur emploi]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users). En général, le ratio MAU/durée de vie diminuera inévitablement au fil du temps en raison du désabonnement des utilisateurs, mais les outils d'engagement de Braze peuvent vous aider à minimiser cet effet en maintenant les utilisateurs engagés plus longtemps.

### Sessions à vie

Le nombre *de sessions à vie* est le nombre total de sessions enregistrées par Braze depuis son intégration. En termes simples, une session correspond à chaque fois qu'un utilisateur utilise l'application ou visite votre site web. Pour une définition plus précise de la manière dont les sessions sont définies par plate-forme, consultez la page correspondante du site web de l'UE.
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), ou les articles des développeurs sur le suivi des sessions [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Utilisateur actif par mois

Les *utilisateurs actifs mensuels* (MAU) correspondent au nombre d'utilisateurs ayant enregistré une session dans votre appli ou votre site au cours des 30 derniers jours. Les MAU sont calculés chaque soir pour une fenêtre glissante de 30 jours. Le MAU vous permet de bien comprendre l'état de santé d'une appli ou d'un site sur une longue période, car il lisse les incohérences entre les jours où l'intensité d'utilisation varie.

Le pourcentage figurant à côté du nombre de MAU indique l'évolution des MAU pour cette période par rapport à la période précédente.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
Les utilisateurs anonymes sont également pris en compte dans votre MAU. Pour les appareils mobiles, les utilisateurs anonymes dépendent de l’appareil. Pour les utilisateurs Web, les utilisateurs anonymes dépendent du cache du navigateur.
{% endalert %}

### Utilisateurs actifs quotidiens

Les *utilisateurs actifs quotidiens* (DAU) affichent le nombre d'utilisateurs uniques qui enregistrent au moins une session dans votre appli ou votre site un jour donné. Le DAU peut être une statistique utile pour examiner la variabilité quotidienne de l'utilisation de votre appli ou de votre site et adapter vos campagnes d'envoi de messages pour qu'elles soient aussi efficaces que possible. Par exemple, l'utilisation de votre application peut connaître un pic appréciable le week-end - cela vous informerait que vous pourriez atteindre plus d'utilisateurs avec des messages in-app ces jours-là par rapport aux jours de la semaine.

### Nouveaux utilisateurs

*Nouveaux utilisateurs* vous indique combien d'utilisateurs n'ayant jamais enregistré de session ont commencé à utiliser votre application ou votre site. Ce nombre est un total de nouveaux utilisateurs sur la période donnée. Cette statistique peut être très utile pour suivre l’efficacité de vos efforts marketing.

{% alert note %}
Lors de l'intégration initiale de Braze, tous les utilisateurs auront l'air de nouveaux utilisateurs car Braze n'a jamais enregistré de session pour eux auparavant.
{% endalert %}

### Adhérence

La valeur d' *adhérence* est un rapport entre le nombre d'utilisateurs quotidiens et le nombre de MAU pour une période donnée. Par essence, l'adhérence mesure le pourcentage de vos utilisateurs actifs mensuels qui reviennent quotidiennement.

Par exemple, si la plage de dates est définie sur 30 jours, un ratio de 50 % indique qu'en moyenne un utilisateur actif utilise l'appli ou le site web pendant 15 jours sur 30 ou qu'environ la moitié de vos utilisateurs actifs reviennent quotidiennement. L'adhérence est un indicateur de succès important, car la plupart des utilisateurs n'abandonnent pas une application parce qu'ils la détestent, mais plutôt parce qu'elle ne fait pas partie de leur routine quotidienne. Par conséquent, vous pouvez utiliser l'adhérence comme indicateur pour mesurer le degré d'engagement de vos utilisateurs.

Le pourcentage figurant à côté du taux d'adhérence indique l'évolution de l'adhérence pour cette période par rapport à la période précédente.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Les délais pour "dernière période" et "cette période" sont déterminés par la plage de dates que vous sélectionnez.

{% alert important %}
La valeur MAU est calculée chaque nuit et n'est mise à jour que le lendemain.
{% endalert %}

### Sessions quotidiennes

*Sessions quotidiennes* est le nombre de sessions enregistrées un jour donné. La comparaison de cette valeur avec votre décompte d'utilisateurs quotidiens peut vous informer du nombre de fois où vos utilisateurs ouvrent l'appli ou visitent votre site web les jours où ils enregistrent au moins une session.

### Sessions quotidiennes par MAU

Le nombre de *sessions quotidiennes par UAM* est le rapport entre le *nombre de sessions quotidiennes* et le nombre d'UAM pour un jour donné. Cette statistique vous indique le nombre de sessions par jour que vous pouvez espérer enregistrer par MAU. Une fois regroupés et calculés, ces chiffres peuvent vous donner une idée de la fréquence relative à laquelle vos utilisateurs utilisent votre application ou votre site. En d'autres termes, si le *nombre de sessions quotidiennes par MAU* est en moyenne de 0,5, vous pouvez vous attendre à ce que chaque utilisateur actif par mois enregistre une session tous les 2 jours environ.  

