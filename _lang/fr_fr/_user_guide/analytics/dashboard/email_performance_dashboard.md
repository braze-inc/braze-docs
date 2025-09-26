---
nav_title: Tableau de bord des performances du canal
article_title: Tableau de bord des performances du canal
page_order: 2
page_type: reference
description: "Cet article de référence couvre le tableau de bord des performances du canal, qui vous permet d’afficher les indicateurs de canaux tout entiers pour vos campagnes et vos Canvas."
tool: 
  - Reports

---

# Tableau de bord des performances du canal

> Les tableaux de bord des performances des canaux affichent les indicateurs de performance agrégés pour un canal entier, à partir des campagnes et des Canevas. Ces tableaux de bord sont disponibles actuellement pour les e-mails et les SMS.

![Tableau de bord des performances des e-mails affichant l'engagement des canaux d'e-mail au cours des trente derniers jours.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

Vous pouvez consulter les tableaux de bord suivants :
- [Tableau de bord des performances e-mail](#email-performance-dashboard)
- [Tableau de bord des informations sur les e-mails](#email-insights-dashboard)
- [Tableau de bord des performances SMS](#sms-performance-dashboard)

## Tableau de bord des performances e-mail

Consultez votre tableau de bord des performances des e-mails en allant dans **Analyse/analytique** > **Performances des e-mails**, et en sélectionnant la plage de dates pour la période dont vous souhaitez consulter les données. Votre plage de dates peut remonter jusqu’à un an par le passé.

### Comment les indicateurs sont-ils calculés ?

![]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Les calculs des différents indicateurs du tableau de bord des performances des e-mails sont les mêmes que ceux effectués au niveau d'un message individuel (comme l'analyse de la campagne). Sur ce tableau de bord, les indicateurs sont agrégés pour toutes les campagnes et les Canvas dans la plage de dates que vous avez sélectionnée. Pour en savoir plus sur ces définitions, reportez-vous à la section [Indicateurs d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Chaque vignette affiche d’abord l’indicateur de pourcentage, puis le chiffre réel (à l’exception de *Envois*, qui montre le nombre d’envois effectués, suivi de la moyenne par jour). Par exemple, la tuile des clics uniques contient le *taux de clics uniques* de la période que vous avez sélectionnée et le décompte du nombre total de clics uniques de cette période. Chaque tuile indique également la [comparaison avec la période précédente](#comparison-to-last-period-change-in-totals-or-rates).

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Total | Nombre total d’envois par jour dans la plage de dates |
| Taux de livraison | Taux | (Nombre total de livraisons chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de désinscription | Taux | (Nombre total de désabonnements uniques pour chaque jour de la plage de dates) / (Nombre total de réception/distribution pour une plage de dates)<br><br>Ceci utilise les désinscriptions uniques, qui sont utilisées également dans les analyses de campagne, l’aperçu et le créateur de rapports. Ces désabonnements sont enregistrés dans toutes les sources (telles que le SDK, l'API REST, les importations CSV, les e-mails et les désabonnements aux listes). Les taux de désabonnement dans les analyses Campaign et Canvas sont des désabonnements qui se produisent à la suite d'un clic de désabonnement sur un e-mail délivré par Braze.  |
| Taux d’ouverture unique | Taux | (Nombre total d'ouvertures uniques pour chaque jour de la plage de dates) / (Nombre total de réception/distribution pour une plage de dates) |
| Taux d’autres ouvertures | Taux | (Nombre total d’autres ouvertures uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates)<br><br>Les autres ouvertures comprennent les e-mails qui n’ont pas été identifiés comme étant ouvert automatiquement, comme quand un utilisateur ouvre un e-mail. Cet indicateur n’est pas unique et est un sous–indicateur du nombre total d’ouvertures.  |
| Taux de clics unique | Taux | (Nombre total de clics uniques pour chaque jour de la plage de dates) / (Nombre total de réception/distribution pour une plage de dates) |
| Taux de « click to open » unique | Taux | (Nombre total de clics uniques pour chaque jour dans la plage de dates) / (Nombre total d’ouvertures uniques pour chaque jour dans la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Tableau de bord des informations sur les e-mails 

Le tableau de bord des informations sur les e-mails permet de savoir où et quand vos clients interagissent avec vos e-mails. Ces rapports peuvent fournir des données riches et granulaires sur la façon d'optimiser vos e-mails pour susciter un plus grand engagement. Le tableau de bord des informations sur les e-mails comprend jusqu'aux six derniers mois de données. Pour accéder au tableau de bord, allez dans **Analyse/analytique** > **Performance des e-mails** > Informations sur les e-mails **.**

### Engagement par appareil

Le rapport sur **l'engagement par appareil** fournit une ventilation des appareils utilisés par vos utilisateurs pour s'engager dans votre e-mail. Ces données permettent de contrôler l'engagement des e-mails sur les mobiles, les ordinateurs de bureau, les tablettes et d'autres types d'appareils. Ces données sont basées sur la chaîne de caractères de l'agent utilisateur transmise par les appareils de vos utilisateurs.

{% alert note %}
Si vous utilisez CloudFront comme réseau de diffusion de contenu, assurez-vous que l'agent utilisateur de vos utilisateurs est transmis à l'ESP. Sinon, chaque agent utilisateur sera "Amazon Cloudfront".
{% endalert %}

La catégorie "Autres" comprend toute chaîne de caractères d'utilisateurs qui ne peut être identifiée comme étant un ordinateur de bureau, un mobile ou une tablette. Par exemple, télévision, voiture, console de jeux vidéo, OTT (over-the-top ou streaming), et similaires. Il peut également s'agir de valeurs nulles ou vides.

Pour mieux comprendre ce qui se trouve dans la catégorie "Autres", vous pouvez extraire les agents utilisateurs à l'aide de l'une ou l'autre de ces options :

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) vous enverra la chaîne de caractères exacte de l'agent utilisateur qui a été récupérée sur les appareils de vos utilisateurs.
2. Tirez parti de notre [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder) pour utiliser le langage SQL ou de notre [générateur de requêtes pour l'intelligence artificielle]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) pour afficher les agents utilisateurs.

![Rapport sur l'engagement par appareil qui indique le nombre de clics pour les mobiles, les ordinateurs de bureau, les tablettes et autres. C'est sur les appareils mobiles que l'on enregistre le plus grand nombre de clics.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Pour l'ouverture des e-mails, Braze sépare Google Image Proxy, Apple Image Proxy et Yahoo Mail Proxy. Ces services mettent en cache et chargent toutes les images intégrées dans un e-mail avant qu'il ne soit envoyé au destinataire. Par conséquent, cela déclenche l'ouverture d'un e-mail à partir des serveurs du fournisseur de la boîte aux lettres plutôt qu'à partir du serveur du destinataire, ce qui peut entraîner une augmentation du nombre d'ouvertures d'e-mails. Ces services sont destinés à améliorer la confidentialité, la sécurité, les performances et l'efficacité lors du chargement des images. Ces données peuvent également contenir des ouvertures réelles de destinataires, car ces services proxy masquent l'agent utilisateur, et nous classons les données proxy en fonction de l'agent utilisateur.

![Rapport sur l'engagement par appareil qui indique le nombre de clics pour les mobiles, les ordinateurs de bureau, les tablettes, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy et autres. C'est sur les appareils mobiles que l'on trouve le plus grand nombre d'ouvertures.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Engagement par fournisseur de boîte aux lettres

Le rapport **Engagement par fournisseur de boîte aux lettres** affiche les principaux fournisseurs de boîtes aux lettres qui contribuent à vos clics ou ouvertures. Vous pouvez cliquer sur des fournisseurs de boîtes aux lettres de premier plan spécifiques afin d'obtenir des informations détaillées sur des domaines de réception spécifiques. Par exemple, si Microsoft figure dans ce rapport comme l'un de vos principaux indicateurs de fournisseurs de messagerie, vous pouvez consulter les détails de leurs domaines de réception tels que outlook.com, hotmail.com, live.com et d'autres encore.

![]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Heure de l’engagement

Le rapport sur le **moment de l'engagement** affiche des données sur le moment où les utilisateurs s'engagent dans vos e-mails. Cela peut aider à répondre à des questions telles que le jour de la semaine ou l'heure à laquelle l'engagement de vos clients est le plus élevé. Grâce à ces informations, vous pouvez expérimenter le meilleur jour ou la meilleure heure pour envoyer vos messages afin d'augmenter le taux d'engagement. Notez que ces heures sont basées sur le fuseau horaire de votre entreprise.

Le rapport d'engagement du **jour de la semaine** décompose les ouvertures ou les clics par jour de la semaine. 

![]({% image_buster /assets/img_archive/time_engagement.png %})

Le rapport sur l'engagement à l **'heure du jour** décompose les ouvertures ou les clics pour chaque heure d'une fenêtre temporelle de 24 heures.

![]({% image_buster /assets/img_archive/time_engagement_day.png %})

Pour plus d'informations sur l'analyse/analytique de vos e-mails, consultez la rubrique [Rapports sur les e-mails.]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)

## Tableau de bord des performances SMS

Pour utiliser votre tableau de bord des performances SMS, accédez à **Analyse/analytique** > **Performances SMS**, puis sélectionnez la plage de dates correspondant à la période dont vous souhaitez consulter les données. Votre plage de dates peut remonter jusqu’à un an par le passé.

### Comment les indicateurs sont-ils calculés ?

![]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Les calculs des différents indicateurs du tableau de bord des performances SMS sont les mêmes que ceux effectués au niveau d'un message individuel (comme l'analyse de la campagne). Sur ce tableau de bord, les indicateurs sont agrégés pour toutes les campagnes et les Canvas dans la plage de dates que vous avez sélectionnée. Pour en savoir plus sur ces définitions, consultez la section [Indicateurs des messages SMS]({{site.baseurl}}/sms_mms_rcs_reporting/).

Chaque vignette affiche d’abord l’indicateur de pourcentage, puis le chiffre réel (à l’exception de _Envois_, qui montre le nombre d’envois effectués, suivi de la moyenne par jour). Chaque tuile indique également la [comparaison avec la période précédente](#comparison-to-last-period-change-in-totals-or-rates).

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Total | Nombre total d’envois par jour dans la plage de dates |
| Taux de livraisons confirmées | Taux | (Nombre total de livraisons chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux d’échecs de livraison | Taux | (Nombre total d’échecs pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de rejets | Taux | (Nombre total de rejets pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de clics | Taux | (Nombre total de clics chaque jour dans la plage de dates) / (Nombre total de livraisons effectuées chaque jour dans la plage de dates) |
| Abonnements totaux | Taux | Nombre total de messages d’abonnement entrants par jour dans la plage de dates |
| Désabonnements totaux | Taux | Nombre total de messages de désabonnement entrants par jour dans la plage de dates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres de tableau de bord

Vous pouvez filtrer les données sur votre tableau de bord en utilisant les options de filtre suivantes :

- **Étiquette :** Choisissez une étiquette. Une fois cette option appliquée, votre tableau de bord affichera des indicateurs uniquement pour l'étiquette sélectionnée.
- **Canvas :** Choisissez jusqu'à 10 toiles. Une fois appliqué, votre tableau de bord affichera les indicateurs pour les seules toiles sélectionnées. Si vous sélectionnez en premier un filtre de balise, les options de vos filtres Canvas ne comprendront alors que les Canvas disposant de la balise sélectionnée.
- **Campagne :** Choisissez jusqu'à 10 campagnes. Une fois appliqué, votre tableau de bord affichera les indicateurs pour les seules campagnes que vous avez sélectionnées. Si vous sélectionnez en premier un filtre de balise, les options de vos filtres de campagnes ne comprendront alors que les campagnes disposant de la balise sélectionnée.

![Options de filtrage sur le tableau de bord de la performance des chaînes où vous pouvez sélectionner une étiquette et une liste de toiles à filtrer.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparaison des périodes

Le tableau de bord de performance de canal compare automatiquement la période sélectionnée dans la plage de dates à la période précédente d’un même nombre de jours. Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates dans le tableau de bord, la comparaison avec la dernière période comparera les indicateurs des sept derniers jours par rapport aux sept jours précédents. Si vous sélectionnez une plage de dates personnalisée, par exemple du 10 mai au 15 mai, soit six jours de données, le tableau de bord comparera les indicateurs de ces jours aux indicateurs du 4 mai au 9 mai.

La comparaison est le pourcentage de variation entre la période actuelle et la dernière période, calculé en prenant la différence entre les deux périodes et en divisant cette dernière par la métrique de la dernière période.

### Visualisation des changements dans les effectifs totaux et les taux

Vous pouvez basculer entre **Afficher les changements de totaux**, qui compare les totaux (par exemple le nombre d'e-mails livrés) entre les deux périodes, et **Afficher les changements de taux**, qui compare les taux (par exemple le taux de livraison).

![Boutons radio permettant de basculer entre l'affichage de la variation des totaux ou de la variation des taux pour le tableau de bord des performances des chaînes.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Foire aux questions

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ?

Quelques scénarios peuvent entraîner des valeurs vides pour un indicateur :

- Braze a enregistré des zéros pour cet indicateur particulier dans la plage de dates sélectionnée.
- Vous n’avez envoyé aucun message au cours de la période sélectionnée.
- Il y a eu des indicateurs concernant des ouvertures, clics ou désinscriptions pendant la période sélectionnée, mais il n’y a pas eu d’envois ou de livraisons. Dans ce cas, Braze ne calculera pas une mesure de taux.

Pour voir plus d’indicateurs, essayez d’étendre la plage de dates.

### Pourquoi mon tableau de bord d’e-mail affiche-t-il plus d’Autres Ouvertures que d’Ouvertures Uniques ?

Pour l'indicateur des _ouvertures uniques_, Braze dédupliquera toutes les ouvertures répétées enregistrées par un utilisateur donné (qu'il s'agisse d'_ouvertures de machines_ ou d'_autres ouvertures_) de sorte qu'une seule _ouverture unique_ soit incrémentée en cas d'ouvertures multiples par un utilisateur. Pour les _autres ouvertures_, Braze ne procède pas à la déduplication.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

