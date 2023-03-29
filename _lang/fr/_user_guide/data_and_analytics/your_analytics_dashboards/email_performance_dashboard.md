---
nav_title: Tableau de bord des performances du canal
article_title: Tableau de bord des performances du canal
page_order: 2
page_type: reference
description: "Cet article de référence couvre le tableau de bord des performances du canal, qui vous permet d’afficher les indicateurs de canaux tout entiers pour vos campagnes et vos Canvas."
tool: 
  - Reports

---

# Tableaux de bord des performances du canal

Les tableaux de bord des performances du canal vous permettent d’afficher les indicateurs de performance globales pour un canal tout entier, à partir des campagnes et des Canvas. Ces tableaux de bord sont disponibles actuellement pour les e-mails et les SMS.

![Tableau de bord des performances e-mail affichant l’engagement des trente derniers jours sur ce canal de communication.][1]

## Tableau de bord des performances e-mail

Pour utiliser votre tableau de bord des performances e-mail, allez sur **Overview** > **Email Performance (Performances e-mail)** et sélectionnez la plage de dates pour laquelle vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu’à un an par le passé.

### Calculs des indicateurs

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Les calculs des différents indicateurs sur le tableau de bord des performances e-mail sont les mêmes que ceux qui sont affichés au niveau du message individuel (c.-à-d., analytiques des campagnes). Sur ce tableau de bord, les mesures sont agrégées pour toutes les campagnes et les Canvas dans la plage de dates que vous avez sélectionnée. Pour en savoir plus sur ces définitions, consultez [Indicateurs E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Chaque vignette affiche l’indicateur de pourcentage d’abord, puis le chiffre réel (à l’exception des _Envois_, qui montre le nombre d’envois effectués suivi de la moyenne par jour). Par exemple, la vignette Clics Uniques montre le _pourcentage de clics uniques_ pour la période sélectionnée et le nombre total de clics uniques pour cette période. Chaque vignette montre également une [comparaison avec la dernière période](#comparison-to-last-period).

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Total | Nombre total d’envois par jour dans la plage de dates |
| Taux de livraison | Taux | (Nombre total de livraisons chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de rebond | Taux | (Nombre total de rebonds pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de désinscription | Taux | (Nombre total de désinscriptions uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates)<br><br>Ceci utilise les désinscriptions uniques, qui sont utilisées également dans les analytiques de campagne, l’aperçu et le créateur de rapports. |
| Taux d’ouverture unique | Taux | (Nombre total d’ouvertures uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates) |
| Taux d’autres ouvertures | Taux | (Nombre total d’autres ouvertures uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates)<br><br>Les autres ouvertures comprennent les e-mails qui n’ont pas été identifiés comme étant ouvert automatiquement, comme quand un utilisateur ouvre un e-mail. Cet indicateur n’est pas unique et est un sous–indicateur du nombre total d’ouvertures.  |
| Taux de clics unique | Taux | (Nombre total de clics uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates) |
| Taux de « click to open » unique | Taux | (Nombre total de clics uniques pour chaque jour dans la plage de dates) / (Nombre total d’ouvertures uniques pour chaque jour dans la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Tableau de bord des performances SMS

Pour utiliser votre tableau de bord des performances SMS, allez sur **Overview** > **Performances SMS** et sélectionnez la plage de dates pour laquelle vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu’à un an par le passé. 

### Calculs des indicateurs

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Les calculs des différents indicateurs sur le tableau de bord des performances SMS sont les mêmes que ceux qui sont affichés au niveau du message individuel (c.-à-d., analytiques des campagnes). Sur ce tableau de bord, les mesures sont agrégées pour toutes les campagnes et les Canvas dans la plage de dates que vous avez sélectionnée. Pour en savoir plus sur ces définitions, consultez la section [Indicateurs SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/).

Chaque vignette affiche l’indicateur de pourcentage d’abord, puis le chiffre réel (à l’exception des _Envois_, qui montre le nombre d’envois effectués suivi de la moyenne par jour). Chaque vignette montre également une [comparaison avec la dernière période](#comparison-to-last-period).

| Indicateur | Type | Calcul |
| --- | --- | ---- |
| Envois | Total | Nombre total d’envois par jour dans la plage de dates |
| Taux de livraisons confirmées | Taux | (Nombre total de livraisons chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux d’échecs de livraison | Taux | (Nombre total d’échecs pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de rejets | Taux | (Nombre total de rejets pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de clics | Taux | (Nombre total de clics chaque jour dans la plage de dates) / (Nombre total de livraisons effectuées chaque jour dans la plage de dates) |
| Abonnements totaux | Taux | Nombre total de messages d’abonnement entrants par jour dans la plage de dates |
| Désabonnements totaux | Taux | Nombre total de messages de désabonnement entrants par jour dans la plage de dates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres de tableau de bord

Vous pouvez filtrer les données sur votre tableau de bord en utilisant les options de filtre suivantes :

- **Balise :** Choisissez une balise. Une fois qu’elle est appliquée, votre tableau de bord affichera des indicateurs pour votre seule balise sélectionnée.
- **Canvas :** Choisissez jusqu’à 10 Canvas. Une fois appliqués, votre tableau de bord affichera des indicateurs pour vos seuls Canvas sélectionnés. Si vous sélectionnez en premier un filtre de balise, les options de vos filtres Canvas ne comprendront alors que les Canvas disposant de la balise sélectionnée.
- **Campagne :** Choisissez jusqu’à 10 campagnes. Une fois appliquées, votre tableau de bord affichera des indicateurs pour vos seules campagnes sélectionnées. Si vous sélectionnez en premier un filtre de balise, les options de vos filtres de campagnes ne comprendront alors que les campagnes disposant de la balise sélectionnée.

![Options de filtre sur le tableau de bord de performance de canal où vous pouvez sélectionner une balise et une liste de Canvas par lesquels vous pouvez filtrer.][3]

## Comparaison avec la dernière période : Changement dans les totaux ou les taux

Le tableau de bord de performance de canal compare automatiquement la période sélectionnée dans la plage de dates à la période précédente d’un même nombre de jours. Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates dans le tableau de bord, la comparaison avec la dernière période comparera les indicateurs des sept derniers jours par rapport aux sept jours précédents. Si vous sélectionnez une plage de dates personnalisée, par exemple du 10 mai au 15 mai, soit six jours de données, le tableau de bord comparera les indicateurs de ces jours aux indicateurs du 4 mai au 9 mai.

La comparaison est le pourcentage de variation entre la période actuelle et la dernière période, calculé en prenant la différence entre les deux périodes et en divisant cette dernière par la métrique de la dernière période.

Vous pouvez basculer entre **Afficher les changements de totaux**, qui compare les décomptes totaux (c.-à-d., le nombre d’e-mails livrés) entre deux périodes, et **Afficher les changements de taux**, qui compare les taux (c.-à-d., le taux de livraison).

![Boutons d’option pour basculer entre le fait d’afficher les changements sur les totaux ou les taux dans le tableau de bord de performance de canal.][4]

## Foire aux questions

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ?

Quelques scénarios peuvent entraîner des valeurs vides pour un indicateur :

- Braze a enregistré des zéros pour cet indicateur particulier dans la plage de dates sélectionnée.
- Vous n’avez envoyé aucun message au cours de la période sélectionnée.
- Il y a eu des indicateurs concernant des ouvertures, clics ou désinscriptions pendant la période sélectionnée, mais il n’y a pas eu d’envois ou de livraisons. Dans ce cas, Braze ne calculera pas une mesure de taux.

Pour voir plus d’indicateurs, essayez d’étendre la plage de dates.

### Pourquoi mon tableau de bord d’e-mail affiche-t-il plus d’Autres Ouvertures que d’Ouvertures Uniques ?

Pour l’indicateur _Ouverture unique_, Braze dédupliquera les données d’ouvertures enregistrées par un utilisateur (que ce soient des _Ouverture sur machine_ ou des _Autres ouvertures_), pour qu’une seule _Ouverture unique_ soit comptabilisée si l’utilisateur ouvre plusieurs fois. Pour les _Autres ouvertures_, Braze ne déduplique pas.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you’ve selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you’ve selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the messages were sent.

#### If a metric displays “--”

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven’t set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}
[2]: {% image_buster /assets/img_archive/email_performance_dashboard_2.png %}
[3]: {% image_buster /assets/img_archive/dashboard_filters.png %}
[4]: {% image_buster /assets/img_archive/email_performance_dashboard_3.png %}
