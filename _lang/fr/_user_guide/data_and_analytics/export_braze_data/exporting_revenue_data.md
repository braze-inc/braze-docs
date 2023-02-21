---
nav_title: Exporter les données sur les revenus et les revenus totaux
article_title: Exporter les données sur les revenus et les revenus totaux
page_order: 4
page_type: reference
description: "Cet article de référence couvre les données et statistiques sur les revenus."
tool: 
  - Rapports

---

# Données sur les revenus

Sur la page **Revenue** (Revenus) du tableau de bord, vous pouvez afficher les données sur les revenus pour des périodes spécifiques, pour un produit spécifique, ou voir le chiffre d’affaires total pour votre application.

{% alert tip %}
Vous cherchez plus de moyens d’obtenir des données sur les revenus ? Essayez d’ajouter un comportement d’achat (en même temps que l’achat du produit) en tant qu’[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) de vos campagnes ou Canvas.
{% endalert %}

## Graphique détaillé des statistiques

Les données suivantes sont accessibles via le graphique **Statistiques détaillées** :

- Achats par date
    - (Facultatif) Achats pour différents produits
- Chiffre d’affaires par date
    - (Facultatif) Chiffre d’affaires pour différents segments
    - (Facultatif) Chiffre d’affaires pour différents produits
- Chiffre d’affaires par heure
    - (Facultatif) Chiffre d’affaires horaire pour différents segments
- Revenu par utilisateur

![Graphique des revenus][9]

## Total des revenus :

Vous pouvez afficher les statistiques du chiffre d’affaires au cas par cas sur les pages [Campaign Analytics (Analyses de campagne)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/campaign_analytics/) ou [Canvas Analytics (Analyses de Canvas)]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/). La statistique du chiffre d’affaires total est générée par les destinataires de la campagne ayant effectué un achat au cours de la période de conversion principale de la campagne.

{% alert tip %}
Pour obtenir de l’aide sur les exportations de CSV et l’API, consultez notre article [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Revenus directs

Vous pouvez afficher les indicateurs de chiffre d’affaires supplémentaires suivants en générant un rapport de comparaison de campagne en utilisant le [Créateur de rapports][1] :

- [Total des revenus directs][2]
- [Total des achats directs][3]
- [Achats directs uniques][4]
- [Revenu par destinataire][5]

Ces métriques sont basées sur l’attribution au dernier clic, ce qui signifie que pour que les revenus soient attribués à une campagne, cette campagne doit :

1. Être la dernière campagne que l’utilisateur a cliqué avant l’achat
    <br>**ET**<br>
2. Avoir été cliquée par l’utilisateur moins de 3 jours avant l’achat.

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
