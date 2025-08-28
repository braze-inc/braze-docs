---
nav_title: Exporter les données sur les revenus et les revenus totaux
article_title: Exporter les données sur les revenus et les revenus totaux
page_order: 4
page_type: reference
description: "Cet article de référence couvre la manière d’exporter les données et les statistiques sur les revenus."
tool: 
  - Reports

---

# Exporter les données sur les revenus et les revenus totaux

> Cette page couvre la page [Rapport sur les revenus]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) du tableau de bord, où vous pouvez consulter des données sur les revenus sur des périodes spécifiques, les revenus d'un produit spécifique et les revenus totaux de votre appli.

Le **rapport sur les revenus** est disponible sous **Analyse**.

{% alert tip %}
Vous cherchez plus de moyens d’obtenir des données sur les revenus ? Essayez d'ajouter le comportement d'achat (ainsi que l'achat d'un produit) aux campagnes ou aux Canvas en tant qu'[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).
{% endalert %}

Pour exporter vos chiffres d'affaires, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> dans le graphique des **performances au fil du temps** et sélectionnez l'option d'exportation de votre choix.

## Graphique des performances dans le temps

Les données suivantes peuvent être visualisées dans le graphique des **performances au fil du temps**:

- Formules de KPI
- Achats
    - (Facultatif) Achats par produit
- Revenue
    - (Optionnel) Chiffre d'affaires par segment
    - (Facultatif) Chiffre d'affaires par produit
- Revenus horaires
    - (Optionnel) Chiffre d'affaires par heure par segmentation
- Chiffre d’affaires par utilisateur

![Chiffre d'affaires]({% image_buster /assets/img_archive/Export_revenue_graph.png %})

## Total des revenus

Vous pouvez consulter les chiffres/analytiques des affaires au cas par cas sur les pages [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) ou [Canvas Analytics.]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)  

{% multi_lang_include metrics.md metric='Total Revenue' %}

{% alert tip %}
Les chiffres d'affaires ne peuvent pas être exportés via l'API. Pour obtenir de l'aide avec les exportations CSV, reportez-vous à la [résolution des problèmes d'exportation.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)
{% endalert %}

{% comment %}

## Revenus directs

Vous pouvez afficher les indicateurs de revenus supplémentaires suivants en générant un rapport de comparaison de campagnes à l'aide du [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) :

- [Total des revenus directs]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue)
- [Total des achats directs]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases)
- [Achats directs uniques]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases)
- [Revenu par destinataire]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient)

Ces indicateurs sont basés sur l'attribution au dernier clic, ce qui signifie que les chiffres d'affaires seront attribués à une campagne si cette campagne :

1. Est la dernière campagne sur laquelle l'utilisateur a cliqué avant l'achat.
    <br>**ET**<br>
2. a été cliqué par l'utilisateur moins de 3 jours avant l'achat

{% endcomment %}




