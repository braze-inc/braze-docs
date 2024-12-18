---
nav_title: Modèles de requête
article_title: Modèles de générateurs de requêtes
page_order: 0
page_type: reference
toc_headers: h2
description: "Cet article de référence répertorie les types de rapports que vous pouvez créer en utilisant les données Braze de Snowflake dans le générateur de rapports."
tool: Reports
---

# Modèles de générateur de requêtes

> Accédez aux modèles du [générateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) en sélectionnant **Modèle de requête** lors de la création d'un rapport. Tous les modèles contiennent des données allant jusqu'aux 60 derniers jours, mais vous pouvez modifier directement cette valeur et d'autres dans l'éditeur.<br><br>Pour connaître les définitions des indicateurs susceptibles d'apparaître dans vos rapports Query Builder, reportez-vous au [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) et filtrez en fonction du canal concerné.

## Modèles de chaînes

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nom de la requête | Description | 
| --- | --- | 
| Engagement du canal et chiffre d’affaires | Ce rapport présente, pour chaque canal, tous les indicateurs d'engagement (tels que les ouvertures et les clics), le chiffre d'affaires, le nombre de transactions et le prix moyen. {::nomarkdown} <ul> <li> <i>Nombre de transactions :</i> Nombre d'événements d'achat </li> <li> <i>Prix moyen :</i> Chiffre d'affaires divisé par le nombre de transactions </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Achats et revenus par segment | Ce rapport présente les indicateurs relatifs aux messages envoyés pour un segment spécifique. <br><br> Les indicateurs d'achat sont uniques tout au long de la période de référence pour les rapports. Un utilisateur peut générer un achat maximum. Le chiffre d'affaires tient compte de tous les achats effectués au cours de la période considérée pour les rapports. |
| Achats et revenus par segment, pour les différentes variantes ou étapes | Ce rapport présente les indicateurs relatifs aux variantes ou aux étapes canvas des messages envoyés à chaque segment. <br><br> Les indicateurs d'achat sont uniques tout au long de la période de référence pour les rapports. Un utilisateur peut générer un achat maximum. Le chiffre d'affaires tient compte de tous les achats effectués au cours de la période considérée pour les rapports. |
| Messages les plus et les moins performants pour les achats | Ce rapport présente les indicateurs d'achat pour les campagnes, canvas ou étapes de canvas les plus ou les moins performants. Chaque ligne correspond à une campagne, un canvas ou une étape du canvas. Vous devez indiquer si vous souhaitez afficher les meilleurs ou les moins bons résultats, ainsi que les indicateurs spécifiques pour lesquels vous souhaitez effectuer cette analyse ( *achats uniques à la réception*, *chiffre d'affaires à la réception*, *destinataires uniques*, par exemple). <br><br> Les lignes des rapports sur les meilleurs résultats seront classées de la meilleure à la pire, tandis que les lignes des rapports sur les moins bons résultats seront classées de la pire à la meilleure. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modèles de campagne

| Nom de la requête | Description | 
| --- | --- | 
| Revenus générés par la campagne par pays | Ce rapport indique les chiffres d'affaires par pays pour une campagne spécifique. Pour exécuter ce rapport, vous devez spécifier l'identifiant API d'une campagne. Vous trouverez l'identifiant API d'une campagne au bas de la page de détails de cette campagne. <br><br> Ce rapport indique, pour chaque pays, le montant des revenus générés, le nombre de commandes, le nombre de retours, le chiffre d'affaires net et le chiffre d'affaires brut.<br><br> {::nomarkdown} <ul> <li> <i>Commandes :</i> Nombre d'événements d'achat </li> <li><i> Retours :</i> Nombre d'événements d'achat avec des chiffres d'affaires négatifs </li> <li><i> Chiffre d'affaires net :</i> Chiffre d’affaires de tout ce qui ne constitue pas de retours </li> <li><i> Chiffre d'affaires brut :</i> Chiffre d'affaires incluant la valeur des retours </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modèles de canvas

| Nom de la requête | Description | 
| --- | --- | 
| Revenus du canvas par pays | Ce rapport indique le chiffre d'affaires par pays pour une toile spécifique. Pour exécuter ce rapport, vous devez spécifier l'identifiant API d'un canvas. Vous trouverez l'identifiant API du canvas sous **Analyser variantes**. <br><br> Ce rapport indique, pour chaque pays, le montant des revenus générés, le nombre de commandes, le nombre de retours, le chiffre d'affaires net et le chiffre d'affaires brut.<br><br> {::nomarkdown} <ul> <li> <i>Commandes :</i> Nombre d'événements d'achat </li> <li><i> Retours :</i> Nombre d'événements d'achat avec des chiffres d'affaires négatifs </li> <li><i> Chiffre d'affaires net :</i> Chiffre d’affaires de tout ce qui ne constitue pas de retours </li> <li><i> Chiffre d'affaires brut :</i> Chiffre d'affaires incluant la valeur des retours </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modèles d'e-mail

| Nom de la requête | Description | 
| --- | --- | 
| Rebonds d’e-mail par domaine | Nombre de rebonds par domaine d'e-mail, décomposé en nombre total de rebonds, échecs d’envoi définitifs et échecs provisoires d’envoi. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Indicateurs de distribution des e-mails par jour | Ce rapport présente les indicateurs relatifs aux messages envoyés chaque jour, tels que le nombre d'e-mails envoyés, livrés, ayant fait l'objet d'un échec provisoire d'envoi et d'un échec définitif d'envoi. <br><br> Tous les indicateurs sont uniques tout au long de la période couverte par le rapport. Par exemple, si un e-mail de bienvenue a fait l'objet d'un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre et n'a jamais été livré : {::nomarkdown} <ul><li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 21 novembre augmente d'une unité.</li><li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 22 novembre ne change pas. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
|  Indicateurs d’engagement envers les e-mails par segment | Ce rapport présente les indicateurs des messages envoyés à chaque segment, tels que le nombre d'e-mails envoyés, livrés, ayant fait l'objet d'un échec provisoire ou d'un échec définitif. <br><br> Tous les indicateurs sont uniques tout au long de la période couverte par le rapport. Par exemple, si un e-mail de bienvenue a fait l'objet d'un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre et n'a jamais été livré : {::nomarkdown} <ul><li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 21 novembre augmente d'une unité. </li><li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 22 novembre ne change pas.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Indicateurs d'engagement par e-mail pour les variantes ou les étapes, par segmentation. | Ce rapport présente les indicateurs relatifs aux variantes ou aux étapes canvas des messages envoyés à chaque segment. Ces indicateurs comprennent le nombre d'e-mails envoyés, livrés, ayant fait l'objet d'un échec provisoire ou d'un échec définitif. <br><br> Tous les indicateurs sont uniques tout au long de la période couverte par le rapport. Par exemple, si un e-mail de bienvenue a fait l'objet d'un échec provisoire d'envoi une fois le 21 novembre, deux fois le 22 novembre et n'a jamais été livré : {::nomarkdown} <ul><li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 21 novembre augmente d'une unité. </li> <li> L’indicateur d’<i>échecs provisoires d'envoi</i> pour le 22 novembre ne change pas.</li></ul> {:/} |
| Performance e-mail par pays | Ce rapport présente les indicateurs suivants pour chaque pays : envois, taux d'ouverture indirect et taux d'ouverture direct. Le pays est le pays de l’utilisateur au moment de l’envoi de la notification push. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Journaux des modifications des abonnements aux e-mails | Ce rapport montre les indicateurs qui ont été enregistrés à propos du changement d'abonnement de chaque utilisateur, tels que son adresse e-mail, son statut d'abonnement, l'heure à laquelle son statut a été modifié et le Canvas ou la campagne associé(e). |
| Abonnements et désinscriptions du groupe d’abonnement par e-mail | Ce rapport indique, pour chaque semaine, le nombre d'abonnements et de désabonnements uniques d'utilisateurs pour les groupes d’abonnement aux e-mails. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URL de l’e-mail cliqué | Ce rapport indique le nombre de clics sur chaque lien dans un e-mail. Pour exécuter ce rapport, vous devez spécifier l’identifiant API pour une campagne ou un Canvas. Vous trouverez l'identifiant API d'une campagne au bas de la page des détails de cette campagne et l'identifiant API de Canvas sous **Analyser les variantes.** <br><br> Ce rapport montre les liens dépersonnalisés et le nombre de clics pour chaque lien. Votre téléchargement CSV inclut les ID utilisateur de tous les utilisateurs qui ont cliqué, le lien sur lequel ils ont cliqué et un horodatage de ce clic. <br><br> *URL dépersonnalisés :* URL dépourvus d'étiquettes Liquid. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Envoi de messages du haut vers le bas pour l’engagement par e-mail | Ce rapport présente les indicateurs d'engagement par e-mail pour les campagnes, Canvas ou étapes Canvas du haut ou du bas de l'échelle. Vous devez indiquer si vous souhaitez afficher les meilleurs ou les moins bons résultats, ainsi que les indicateurs spécifiques pour lesquels vous souhaitez effectuer cette analyse (tels que les *envois*, les *échecs provisoires d'envoi* et les *ouvertures uniques*). <br><br> Les lignes des rapports sur les meilleurs résultats seront classées de la meilleure à la pire, tandis que les lignes des rapports sur les moins bons résultats seront classées de la pire à la meilleure. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 }

## Modèles mobiles

| Nom de la requête | Description | 
| --- | --- | 
| Opérateurs des appareils | Le nombre d'utilisateurs par opérateur d'appareil, comme Verizon et T-Mobile. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modèles d’appareil  | Le nombre d'utilisateurs par modèle d'appareil, comme l'iPhone 15 Pro et le Pixel 7. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Systèmes d’exploitation des appareils | Le nombre d'utilisateurs par système d'exploitation, par exemple 17.4 et Android 14. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Résolutions de l’écran des appareils | Le nombre d'utilisateurs par résolution d'écran de l'appareil, par exemple 1179x2556 et 750x1334. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Codes d’erreur SMS | Ce rapport indique le type d'erreur et le nombre d'erreurs pour chaque code d'erreur SMS. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| SMS Fournir des erreurs par utilisateur | Ce rapport indique les codes d'erreur SMS pour un utilisateur spécifique. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modèles de notifications push

| Nom de la requête | Description | 
| --- | --- | 
| Performances des notifications push par pays | Ce rapport présente les indicateurs suivants pour chaque pays : réception/distribution, taux d'ouverture et taux de clics. Le pays est le pays de l’utilisateur au moment de l’envoi de l’e-mail. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Répartition des segments

| Nom de la requête | Description |
| -- | -- |
| Indicateurs d’engagement envers les e-mails par segment | Ce rapport présente les indicateurs de performance des e-mails ventilés par segment au niveau de la campagne ou du canvas. |
| Achats et revenus par segment | Ce rapport présente les indicateurs d'achats et d'affaires ventilés par segment pour une campagne ou un canvas spécifique. |
| Envoi de messages du haut vers le bas pour l’engagement par e-mail | Ce rapport indique les campagnes, les Canvas ou les étapes du Canvas les plus performants ou les moins performants pour un indicateur d'engagement par e-mail spécifié.|
| Messages les plus et les moins performants pour les achats | Ce rapport indique les campagnes, les Canvas ou les étapes du Canvas les plus ou les moins performants pour un indicateur d'achat ou de chiffre d'affaires spécifié. |
| Performance des notifications push par segment | Ce rapport présente les indicateurs de poussée ventilés par segmentation.|
{: .reset-td-br-1 .reset-td-br-2 }