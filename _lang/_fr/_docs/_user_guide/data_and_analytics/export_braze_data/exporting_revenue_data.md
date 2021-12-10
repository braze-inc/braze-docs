---
nav_title: Exporter les revenus & Total des revenus
article_title: Exporter les revenus & Total des revenus
page_order: 4
page_type: Référence
description: "Cet article de référence couvre les données sur les revenus et les statistiques."
tool:
  - Rapports
---

# Données des revenus

Sur la page **Revenus** du tableau de bord, vous pouvez afficher des données sur les revenus ou les achats sur des périodes spécifiques de temps, pour un produit spécifique, ou pour le chiffre d'affaires ou les achats totaux de votre application.

{% alert tip %}
Vous recherchez plus de moyens pour obtenir des données sur les revenus ? Essayez d'ajouter un comportement d'achat (ainsi que l'achat d'un produit) aux campagnes ou aux Canvases en tant que [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/).
{% endalert %}

## Graphique de statistiques détaillées

Les données suivantes peuvent être consultées via le graphique **Statistiques Détaillées**:

- Achats par date
    - (Facultatif) Achats pour différents produits
- Revenu par date
    - (Optionnel) Revenus pour différents segments
    - (Optionnel) Revenus pour différents produits
- Revenus par Heure
    - (Facultatif) Revenus par heure pour différents segments
- Revenus par utilisateur

!\[Graphique des revenus\]\[9\]

## Revenus totaux

Vous pouvez consulter les statistiques de revenus au cas par cas sur les pages [Analyses de campagne]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/campaign_analytics/) ou [Analytiques de toile]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/). La statistique des revenus totaux est générée par les bénéficiaires de la campagne qui ont effectué un achat au cours de la période de conversion primaire de la campagne.

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, reportez-vous à [la fonction de dépannage d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Revenus directs

Vous pouvez consulter les métriques de revenus supplémentaires suivantes en générant un rapport de comparaison de campagne en utilisant le [Constructeur de rapport][1]:

- [Revenus directs totaux][2]
- [Achats directs totaux][3]
- [Achats directs uniques][4]
- [Revenus par Destinataire][5]

Ces mesures sont basées sur l'attribut du dernier clic, ce qui signifie que pour que les revenus soient attribués à une campagne, cette campagne doit:

1. Soyez la dernière campagne que l'utilisateur a cliqué avant d'acheter <br>**ET**<br>
2. Être cliqué par l'utilisateur moins de 3 jours avant l'achat

{% endcomment %}
[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient
