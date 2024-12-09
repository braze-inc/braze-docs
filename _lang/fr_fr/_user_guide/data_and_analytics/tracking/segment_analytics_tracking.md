---
nav_title: Suivi analytique des segments
article_title: Suivi analytique des segments
page_order: 8
page_type: reference
description: "Cet article de référence couvre le suivi de l'analyse/analytique des segments et explique comment afficher les chiffres d'affaires et les achats au fil du temps, les sessions au fil du temps et les événements personnalisés au fil du temps."
tool: 
  - Segments
  - Reports
---

# Suivi analytique des segments

> Lorsque le suivi analytique est activé pour un segment, vous pouvez afficher les sessions, les événements personnalisés et le chiffre d'affaires au fil du temps pour ce segment.

Si vous n'activez pas le suivi analytique pour un segment, vous pouvez toujours accéder aux [statistiques en temps réel][11] de ce segment et cibler ses utilisateurs avec des campagnes. La seule différence réside dans l'accès aux outils d'analyse spécifiques mentionnés sur cette page.

## Activation de l'analyse des segments

Dans la section **Informations relatives au segment** de la page d'un segment, activez le **suivi des analyses**.

![Basculer le suivi des analyses sur un segment][16]

Le suivi peut être activé pour 25 segments maximum dans une application. Braze recommande de suivre les segments qui sont importants pour vous permettre d’analyser les effets de vos campagnes sur les sessions, les revenus et les achats.

## Visualisation des chiffres d'affaires et des achats dans le temps

Allez dans **Analyse/analytique** > **Rapport sur les recettes** pour consulter les données sur les [recettes et les achats au fil du temps pour ce segment][14].

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **chiffres d'affaires** sous **Données**.
{% endalert %}

![Données de revenus par segment][17]

Pour comparer visuellement les données de segment pour une période personnalisée, ajoutez ou supprimez des segments du graphique. Sélectionnez **Par segment** dans le menu déroulant **Répartition**, puis sélectionnez vos segments dans **Valeurs de répartition**.

Sélectionnez un nom de segment au-dessus du graphique pour activer ou désactiver la visibilité des indicateurs de ce segment.

![Chiffre d'affaires pour plusieurs segments][21]

## Sessions au cours du temps

De même, vous pouvez trouver des données sur les [sessions dans le temps pour ce segment particulier][13] sur la page d **'accueil**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), il s'agit de votre page d'**aperçu.**
{% endalert %}

![Données de session par segment][18]

## Visualiser les événements personnalisés dans le temps

Consultez les données sur les [événements personnalisés au fil du temps pour les segments][20] en allant dans **Analytics** > **Custom Events Report.**

## Utilisation des modèles du générateur de requêtes

Lorsque le suivi analytique est activé, vous pouvez utiliser les modèles de rapports du générateur de requêtes pour décomposer les indicateurs de performance des campagnes, des Canvas, des variantes et des étapes par segment. Pour en savoir plus, consultez les [Données du segment]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}
