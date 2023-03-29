---
nav_title: Générateur de requêtes
article_title: Générateur de requêtes
page_order: 100
page_type: reference
description: "Cet article de référence décrit comment créer des rapports à l’aide des données Braze depuis Snowflake dans le générateur de requêtes."
tool: Rapports
---

# Générateur de requêtes

Avec le générateur de requêtes, vous pouvez générer des rapports en utilisant les données Braze dans Snowflake. Le générateur de requêtes est livré avec des [modèles de requête](#query-templates) SQL préconstruits pour commencer. Actuellement, seules les requêtes modélisées sont autorisées, la prise en charge des requêtes SQL personnalisées suivra.

{% alert important %}
Le générateur de requêtes est en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Exécution des rapports dans le générateur de requêtes

Pour exécuter un rapport :

1. Rendez-vous sur **Query Builder (Générateur de requêtes)**, sous **Data (Données)**.
2. Sélectionnez le rapport que vous souhaitez exécuter.
3. Cliquez sur **Run Report (Exécuter le rapport)**.
4. Pour télécharger votre rapport au format CSV, cliquez sur **Export (Exporter)**.

![Générateur de requêtes affichant les résultats de la requête modélisée « Engagement de canal et chiffre d’affaires au cours des 30 derniers jours ».]({% image_buster /assets/img_archive/query_builder.png %})

Les résultats de chaque rapport peuvent être générés une fois par jour. Si vous exécutez le même rapport plus d’une fois pour un jour civil, vous verrez les mêmes résultats dans les deux rapports.

### Temporisation du rapport

Les rapports qui prennent plus de 6 minutes à s’exécuter vont expirer. S’il s’agit de la première requête que vous exécutez depuis un certain temps, elle peut être plus longue à traiter et, par conséquent, le risque de temporisation est plus important. Si cela se produit, essayez d’exécuter le rapport à nouveau.

Si un rapport temporise ou rencontre des erreurs, même après avoir essayé à nouveau, veuillez contacter l’assistance.

## Modèles de requêtes

Toutes les données de surface des modèles proviennent des 30 derniers jours.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 25%;
}
table th:nth-child(3) {
    width: 20%;
}
table th:nth-child(4) {
    width: 45%;
}
table td {
    word-break: break-word;
}
</style>


| Nom de la requête | Description | Indicateurs | Aperçu |
| --- | --- | --- | --- |
| Engagement du canal et chiffre d’affaires | Pour chaque canal, vous verrez tous ses indicateurs d’engagement (ouverture, clics, etc.), le chiffre d’affaires, le nombre de transactions et le prix moyen. | {::nomarkdown} <ul> <li> <b>Nombre de transactions :</b> nombre d’événements d’achat </li> <li> <b>Prix moyen :</b> chiffre d’affaires divisé par les transactions </li> </ul> {:/} | ![]({% image_buster /assets/img_archive/query_builder_q1.png %}) |
| Rebonds d’e-mail par domaine | Nombre de rebonds par domaine d’e-mail | | ![]({% image_buster /assets/img_archive/query_builder_q2.png %}) |
| Performance e-mail par pays | Pour chaque pays, vous verrez les indicateurs suivants : envoi, taux d’ouverture indirecte et directe. Le pays est le pays de l’utilisateur au moment de l’envoi de la notification push. | | ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Abonnements et désinscriptions du groupe d’abonnement par e-mail | Pour chaque semaine, vous verrez le nombre d’abonnements et de désinscriptions uniques des groupes d’abonnement par e-mail. | | ![]({% image_buster /assets/img_archive/query_builder_q4.png %}) |
| URL de l’e-mail cliqué | Ce rapport indique le nombre de clics sur chaque lien dans un e-mail. Pour exécuter ce rapport, vous devez spécifier l’identifiant API pour une campagne ou un Canvas. Vous pouvez trouver l’identifiant API d’une campagne au bas de la page des détails de cette campagne et vous pouvez trouver l’identifiant API Canvas sous **Analyze Variants (Analyser les variantes)**. <br><br>Pour chaque lien personnalisé, vous verrez un décompte des clics. Votre téléchargement CSV inclut les ID utilisateur de tous les utilisateurs qui ont cliqué, le lien sur lequel ils ont cliqué et un horodatage de ce clic. | **URL personnalisées :** Les URL qui sont vidées de balises Liquid | ![]({% image_buster /assets/img_archive/query_builder_q5.png %}) |
| Chiffre d’affaires par pays | Ce rapport fournit le chiffre d’affaires par pays pour une campagne/Canvas spécifique. Pour exécuter ce rapport, vous devez spécifier l’identifiant API pour une campagne ou un Canvas. Vous pouvez trouver l’identifiant API d’une campagne au bas de la page des détails de cette campagne et vous pouvez trouver l’identifiant API Canvas sous **Analyze Variants (Analyser les variantes)**.<br><br>Pour chaque pays, vous verrez le montant du chiffre d’affaires généré, le nombre de commandes, le nombre de retours, le chiffre d’affaires net et le chiffre d’affaires brut. | {::nomarkdown} <ul> <li> <b>Nombre de commandes :</b> nombre d’événements d’achat </li> <li> <b>Nombre de retours :</b> nombre d’événements d’achat avec des valeurs de chiffre d’affaires négatives </li> <li> <b>Chiffre d’affaires net :</b> chiffre d’affaires de tout ce qui ne constitue pas de retours </li> <li> <b>Chiffre d’affaires brut :</b> chiffre d’affaires qui inclut la valeur des retours </li> </ul> {:/} | ![]({% image_buster /assets/img_archive/query_builder_q6.png %}) |
| Performances des notifications push par pays | Pour chaque pays, vous verrez les indicateurs suivants : livraisons, taux d’ouverture et taux de clics. Le pays est le pays de l’utilisateur au moment de l’envoi de l’e-mail. | | ![]({% image_buster /assets/img_archive/query_builder_q7.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}