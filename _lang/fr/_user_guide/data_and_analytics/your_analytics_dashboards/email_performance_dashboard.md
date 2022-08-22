---
nav_title: Tableau de bord des performances E-mail 
article_title: Tableau de bord des performances E-mail
page_order: 2
page_type: reference
description: "Cet article de référence couvre le tableau de bord des performances E-mail, qui vous permet d’afficher les indicateurs de performance du canal E-mail pour toutes vos campagnes et tous vos Canvas."
tool: 
  - Rapports

---

# Tableau de bord des performances E-mail

Le tableau de bord des performances d’E-mail vous permet d’afficher les mesures de performance globales pour l’ensemble de votre canal d’E-mail, à partir des campagnes et des Canvas. 

Pour utiliser votre tableau de bord des performances E-mail, allez sur **Overview** > **Performances E-mail **, et sélectionnez la plage de dates pour laquelle vous souhaitez afficher les données. Votre plage de dates peut remonter jusqu’à un an par le passé.

![Tableau de bord des performances E-mail affichant l’engagement des sept derniers jours sur ce canal de communication.][1]

## Calculs des métriques

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Les calculs des différentes métriques sur le tableau de bord des performances E-mail sont les mêmes que ceux qui sont affichés pour l’analyse des campagnes (c.-à-d. au niveau des messages individuels). Sur ce tableau de bord, les mesures sont agrégées pour toutes les campagnes et les Canvas dans la plage de dates que vous avez sélectionnée. Pour en savoir plus sur ces définitions, consultez [Métriques E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Chaque vignette affiche le pourcentage d’abord, puis le chiffre réel (à l’exception des  _Envois_, qui montre le nombre d’envois effectués suivi de la moyenne par jour). Par exemple, la vignette Clics Uniques montre le  _pourcentage de clics uniques_  pour la période sélectionnée et le nombre total de clics uniques pour cette période. Chaque vignette montre également une comparaison[ avec la dernière période](#comparison-to-last-period).

| Métrique | Type | Calcul |
| --- | --- | ---- |
| Envois | Total | Nombre total d’envois par jour dans la plage de dates |
| Taux de livraison | Taux | (Nombre total de livraisons chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de bounce | Taux | (Nombre total de bounce pour chaque jour dans la plage de dates) / (Nombre total d’envois effectués chaque jour dans la plage de dates) |
| Taux de désinscription | Taux | (Nombre total de désinscriptions uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates)<br> <br> Basé sur les désabonnements uniques, qui sont également utilisés dans Campaign Analytics, Overview et Créateur de rapports. |
| Taux d’ouverture unique | Taux | (Nombre total d’ouvertures uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates) |
| Taux d’autres ouvertures | Taux | (Nombre total de toutes les autres ouvertures dans la plage de dates) / (Nombre total de livraisons pour la plage de dates)<br> <br> Les autres ouvertures incluent les e-mails qui n’ont pas été identifiés comme étant ouverts sur machine, par exemple lorsqu’un utilisateur ouvre un e-mail. Cette métrique n’est pas unique et est une sous-métrique du nombre total d’ouvertures.  |
| Taux de clics unique | Taux | (Nombre total de clics uniques pour chaque jour dans la plage de dates) / (Nombre total de livraisons pour la plage de dates) |
| Taux de « click to open » unique | Taux | (Nombre total de clics uniques pour chaque jour dans la plage de dates) / (Nombre total d’ouvertures uniques pour chaque jour dans la plage de dates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Comparaison avec la dernière période

Le tableau de bord d’E-mail compare automatiquement la période sélectionnée dans la plage de dates à la période précédente (même nombre de jours). Par exemple, si vous choisissez « 7 derniers jours » comme plage de dates dans le tableau de bord, la comparaison avec la dernière période comparera les métriques des sept derniers jours par rapport aux sept jours précédents. Si vous sélectionnez une plage de dates personnalisée, par exemple du 10 mai au 15 mai, soit six jours de données, le tableau de bord comparera les métriques de ces jours aux métriques du 4 mai au 9 mai.

La comparaison est le pourcentage de variation entre la période actuelle et la dernière période, calculé en prenant la différence entre les deux périodes et en divisant cette dernière par la métrique de la dernière période.

## Questions fréquemment posées

### Pourquoi mon tableau de bord affiche-t-il des valeurs vides ?

Quelques scénarios peuvent entraîner des valeurs vides pour une métrique :

- Braze a enregistré des zéros pour cette métrique particulière dans la plage de dates sélectionnée.
- Vous n’avez envoyé aucun e-mail au cours de la période sélectionnée.
- Il y a eu des ouvertures, clics ou désinscriptions pendant la période sélectionnée, mais il n’y a pas eu d’envois ou de livraisons. Dans ce cas, Braze ne calculera pas une mesure de taux.

Pour voir plus de métriques, essayez d’étendre la plage de dates.

### Pourquoi mon tableau de bord affiche-t-il plus d’Autres Ouvertures que d’Ouvertures Uniques ?

Pour la métrique  _Ouverture unique_ , Braze dédupliquera les données d’ouvertures enregistrées par un utilisateur (que ce soient des  _Ouverture sur machine_  ou des  _Autres ouvertures_), pour qu’une seule  _Ouverture unique_  soit comptabilisée si l’utilisateur ouvre plusieurs fois. Pour les  _Autres ouvertures_, Braze ne déduplique pas.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you’ve selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you’ve selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the emails were sent.

#### If a metric displays “--”

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven’t set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}
[2]: {% image_buster /assets/img_archive/email_performance_dashboard_2.png %}
