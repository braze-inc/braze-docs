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

Si vous n'activez pas le suivi analytique pour un segment, vous pouvez toujours accéder aux [statistiques en temps réel]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics) de ce segment et cibler ses utilisateurs avec des campagnes. La seule différence réside dans l'accès aux outils d'analyse spécifiques mentionnés sur cette page.

## Activation de l'analyse des segments

Dans la section **Informations relatives au segment** de la page d'un segment, activez le **suivi des analyses**.

![Basculer le suivi analytique d'un segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Le suivi peut être activé pour 25 segments maximum dans une application. Braze recommande de suivre les segments qui sont importants pour vous permettre d’analyser les effets de vos campagnes sur les sessions, les revenus et les achats.

## Visualisation des chiffres d'affaires et des achats dans le temps

Allez dans **Analyse/analytique** > **Rapport sur les recettes** pour consulter les données sur les [recettes et les achats au fil du temps pour ce segment]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/).

![Données sur les chiffres d'affaires par segment]({% image_buster /assets/img_archive/Revenue.png %})

Pour comparer visuellement les données de segment pour une période personnalisée, ajoutez ou supprimez des segments du graphique. Sélectionnez **Par segment** dans le menu déroulant **Répartition**, puis sélectionnez vos segments dans **Valeurs de répartition**.

Sélectionnez un nom de segment au-dessus du graphique pour activer ou désactiver la visibilité des indicateurs de ce segment.

![Chiffre d'affaires pour plusieurs segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessions au cours du temps

De même, vous pouvez trouver des données sur les [sessions dans le temps pour ce segment particulier]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data) sur la page d **'accueil**.

![Données de session par segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualiser les événements personnalisés dans le temps

Consultez les données sur les [événements personnalisés au fil du temps pour les segments]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics) en allant dans **Analytics** > **Custom Events Report (**si utilisé en tant qu'adjectif).

## Utilisation des modèles du générateur de requêtes

Lorsque le suivi analytique est activé, vous pouvez utiliser les modèles de rapports du générateur de requêtes pour décomposer les indicateurs de performance des campagnes, des Canvas, des variantes et des étapes par segment. Pour en savoir plus, consultez les [Données du segment]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

