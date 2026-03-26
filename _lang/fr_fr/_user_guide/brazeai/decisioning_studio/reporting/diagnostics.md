---
nav_title: Diagnostics
article_title: Rapport de diagnostics
page_order: 3
description: "Découvrez comment utiliser le rapport de diagnostics pour surveiller la santé des données sortantes et entrantes dans BrazeAI Decisioning Studio."
---

# Rapport de diagnostics

> Le rapport de diagnostics contient deux types de rapports différents : **Sortant** et **Entrant**.

{% tabs local %}
{% tab outbound %}
Le rapport de diagnostics sortant affiche le volume quotidien de recommandations générées et activées pour l'ensemble de vos audiences. Utilisez-le pour repérer les problèmes de distribution, suivre les pics ou les baisses d'activations et confirmer que les messages atteignent bien les groupes ciblés.

![Rapport de diagnostics sortant affichant un graphique linéaire qui suit le volume quotidien de recommandations générées et activées pour différents groupes d'audience. Le graphique présente deux lignes intitulées Generated et Activated, avec l'axe des ordonnées représentant le nombre de recommandations et l'axe des abscisses les dates. Une légende identifie chaque ligne par couleur. L'interface comprend des filtres déroulants pour la plage de dates et la sélection d'audience au-dessus du graphique.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Le rapport de diagnostics entrant surveille la santé de vos flux de données vers BrazeAI<sup>TM</sup>. Il suit des détails tels que le nombre de fichiers, leur taille et le volume de lignes pour chaque ressource, vous permettant de confirmer que les données arrivent comme prévu et de résoudre les problèmes avant qu'ils n'affectent vos agents ou campagnes.

Vous pouvez utiliser le menu déroulant pour sélectionner différents indicateurs de graphique, comme la taille moyenne des fichiers ou le nombre de fichiers.

![Rapport de diagnostics entrant affichant un graphique linéaire qui suit le nombre quotidien de fichiers et la taille moyenne des fichiers pour les ressources de données livrées à BrazeAI<sup>TM</sup>. Le graphique présente deux lignes intitulées File count et Average file size MBs, avec l'axe des ordonnées représentant les valeurs et l'axe des abscisses les dates. Au-dessus du graphique se trouvent des filtres déroulants pour la plage de dates et la sélection de ressource de données.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Consultez le tableau suivant pour plus de détails sur chaque indicateur du rapport entrant :

| Champ | Description |
|-------|-------------|
| Data asset | Le nom du jeu de données ou du fichier livré. |
| Date | La date à laquelle les données ont été reçues. |
| Last delivery time | L'heure la plus récente à laquelle les données ont été livrées. |
| File count | Le nombre total de fichiers reçus. |
| Max file size (MBs) | La taille du plus gros fichier reçu, en mégaoctets. |
| Average file size (MBs) | La taille moyenne de tous les fichiers reçus, en mégaoctets. |
| File row count | Le nombre total de lignes contenues dans les fichiers livrés. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}