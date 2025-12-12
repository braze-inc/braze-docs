---
nav_title: Vos rapports
article_title: Vos rapports
page_order: 7
layout: dev_guide
guide_top_header: "Vos rapports"
guide_top_text: "Vos données vous tiennent à cœur, c'est pourquoi nous vous proposons plusieurs options de reporting au sein de Braze (hors <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>). Si vous ne savez pas par où commencer, consultez l <a href='/docs/user_guide/analytics/reporting/#reports-overview'>'aperçu des rapports</a> pour savoir quels rapports et analyses vous pouvez utiliser pour répondre aux questions courantes en matière de stratégie marketing."

page_type: landing
description: "Cette page d'accueil contient des articles sur les options de rapports disponibles dans Braze (hors Currents), notamment les rapports de segmentation, les rapports d'engagement, le générateur de rapports, et bien plus encore."
tool: Reports
search_rank: 2
guide_featured_title: "Articles de section"
guide_featured_list:
  - name: Glossaire des indicateurs du rapport
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Données de segmentation
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: "Rapports d'engagement"
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: Générateur de rapports
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: Générateur de tableau de bord
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Configuration des rapports
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Analyse/analytique de la campagne (si utilisée comme adjective)
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Analytics (si utilisé comme adjectif)
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: Événements personnalisés
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "Rapport d'entonnoir"
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Rapport sur le contrôle global
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: Rapport de rétention
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: "Chiffre d'affaires"
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: "Chiffre d'affaires"
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Statistiques des segments
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Rapport du groupe de contrôle global
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# Aperçu des rapports

## Quelle variante a gagné ?

{% tabs local %}
{% tab Campaign Analytics %}
**Analyse/analytique de la campagne (si utilisée comme adjective)**

Utilisez l'[analyse/analytique des campagnes]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) pour obtenir des mises à jour en temps réel sur les résultats de haut niveau de chaque campagne et variante de cette campagne, ainsi que des détails au niveau des messages. Vous pouvez ajuster la plage de dates pour comprendre les performances de la campagne dans le temps et prévisualiser vos messages pour vous souvenir de ce que vous testiez.

{% endtab %}

{% tab Canvas Analytics %}
**Canvas Analytics (si utilisé comme adjectif)**

Utilisez [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour obtenir des statistiques de haut niveau sur votre Canvas afin de voir comment votre stratégie d'envoi de messages fonctionne. Ouvrez n'importe quel canvas en ligne/en production/instantané pour obtenir des statistiques clés sur les performances, telles que

- Nombre de messages envoyés dans le Canvas
- Nombre total de fois où les clients sont entrés dans le Canvas
- Combien de clients ont été convertis ?
- Chiffre d'affaires généré par le Canvas
- Estimation de l'audience totale

<br>

**Performance par variante**

[Analysez les variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) dans une ligne/en production/instantanée (Canvas) pour afficher les taux de conversion calculés automatiquement pour chaque événement de conversion. Vous pouvez également consulter les calculs d'augmentation et de confiance pour chaque variante et événement de conversion sous la forme d'un tableau facile à comparer.

Ce rapport vous permettra de répondre à d'autres questions :

- La confiance est-elle statistiquement significative ?
- Comment la variante 1 s'est-elle comportée par rapport à la variante 2 ?

{% endtab %}

{% tab Report Builder %}
**Générateur de rapports**

Utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) pour comparer les résultats de plusieurs campagnes ou Canvas en une seule vue et déterminer rapidement quelles stratégies d'engagement ont eu le plus d'impact sur vos indicateurs clés.

Consultez cette page pour :

- Créez un rapport sur les campagnes et les Canevas de la semaine ou du mois dernier, calculez les indicateurs critiques et partagez avec vos coéquipiers.
- Comparez les performances entre les variantes pour les tests multivariés et les Canevas.
- Déterminez quel canal de communication a obtenu le plus de conversion ou d'engagement pour une campagne ou un canvas spécifique.
- Suivre les tendances générales de performance d'un groupe de campagnes ou de Canevas (par exemple, tous les messages liés à une étiquette "newsletters").

Plus de questions auxquelles vous pouvez répondre grâce à cette fonctionnalité :

- Quelle a été la performance de la première version de mon e-mail de bienvenue par rapport à la seconde ?
- Quels ont été mes taux d'ouverture moyens en push ce mois-ci par rapport au mois dernier, pour une étiquette particulière ?
- Quelle lettre d'information mensuelle a obtenu le plus grand nombre de conversions ?

{% endtab %}
{% endtabs %}

## Quelle variante a eu le plus d'impact sur la rétention ?

{% tabs local %}
{% tab Retention Reports %}
**Rapports de rétention**

Utilisez les rapports de rétention pour les [campagnes]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) ou les [canevas]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) afin de mesurer la rétention des utilisateurs qui ont effectué un événement sélectionné dans une campagne spécifique.

Consultez ce rapport :

- Déterminez l'efficacité d'un message pour réengager les utilisateurs à long terme en analysant l'occurrence de différents événements jusqu'à un mois après la réception d'une campagne.
- Comparez l'occurrence de différents événements entre les variantes d'un [test A/B.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)

Ce rapport vous permettra de répondre à d'autres questions :

- Quelle variante a eu le plus d'impact sur la rétention ?
- Pendant combien de temps mes clients qui ont reçu cette campagne continuent-ils à utiliser mon appli par la suite ?
- Quel a été l'impact de cette campagne sur la rétention après un jour ? Après 30 jours ?

{% alert note %} Les rapports de rétention ne sont pas disponibles pour les campagnes déclenchées par SMS et API. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

Utilisez les rapports d'entonnoir pour les [campagnes]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) ou les [Canevas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) pour analyser les parcours de vos clients après avoir reçu une campagne. Vous pouvez choisir les événements natifs ou personnalisés à inclure dans chaque analyse de tunnel, puis plonger dans les performances de chaque variante par rapport à l'entonnoir de conversion sélectionné.

Consultez ce rapport :

- Comprenez à quel endroit du tunnel de conversion les utilisateurs ont décroché et identifiez les opportunités d'envoi de messages de réengagement.
- Affichez les conversions pour un événement qui n'était pas initialement inclus en tant qu'événement de conversion lors de l'implémentation de la campagne.
- Analysez l'entonnoir d'achat à l'aide d'une série d'actions (telles que "Quel pourcentage de clients a reçu un e-mail, a démarré une session, a ajouté un article à son panier, puis a acheté ?").

Ce rapport vous permettra de répondre à d'autres questions :

- À quel endroit du chemin de la conversion mes clients s'arrêtent-ils ?
- Comment puis-je améliorer mes stratégies de marketing ?

{% endtab %}
{% endtabs%}

## Quel est le degré d'engagement de mes utilisateurs ?

{% tabs local %}
{% tab Report Builder %}

Utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) pour comparer les résultats de plusieurs campagnes ou Canvas en une seule vue et déterminer rapidement quelles stratégies d'engagement ont eu le plus d'impact sur vos indicateurs clés.

Consultez cette page pour :

- Créez un rapport sur les campagnes et les Canevas de la semaine ou du mois dernier, calculez les indicateurs critiques et partagez avec vos coéquipiers.
- Déterminez quel canal de communication a obtenu le plus de conversion ou d'engagement pour une campagne ou un canvas spécifique.
- Suivre les tendances générales de performance d'un groupe de campagnes ou de Canevas (par exemple, tous les messages liés à une étiquette "newsletters").

Plus de questions auxquelles vous pouvez répondre grâce à cette fonctionnalité :

- Quelle a été la performance de la première version de mon e-mail de bienvenue par rapport à la seconde ?
- Quels ont été mes taux d'ouverture moyens en push ce mois-ci par rapport au mois dernier, pour une étiquette particulière ?
- Quelle lettre d'information mensuelle a obtenu le plus grand nombre de conversions ?

{% endtab %}
{% tab Overview Data %}
**Données d'aperçu**

Utilisez la page [Aperçu]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) pour obtenir un résumé de haut niveau des indicateurs clés concernant les performances de votre application et des informations sur la base d'utilisateurs de votre application.

Consultez cette page pour connaître ces statistiques :

- Utilisateurs à vie
- Sessions à vie
- Utilisateurs actifs mensuels par mois (MAU)
- Utilisateurs actifs quotidiens (UAP)
- Nouveaux utilisateurs
- Adhérence
- Sessions quotidiennes
- Session journalière par MAU

Plus de questions auxquelles vous pouvez répondre avec ce tableau de bord :

- Est-ce que je constate une amélioration de l'adhérence d'un mois sur l'autre ?
- Est-ce que je constate une croissance globale de mon application iOS ou Android ?
- Quel est le volume global de mes e-mails ce mois-ci ?

{% endtab %}
{% tab Engagement Reports %}
**Rapports d'engagement**

Utilisez les [rapports d'engagement]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) pour implémenter une exportation récurrente par e-mail des statistiques d'engagement pour les campagnes et les Canevas sélectionnés. Ce rapport est le plus personnalisable et le plus granulaire des rapports disponibles dans le tableau de bord.

Vous pouvez exporter les statistiques suivantes en fonction de votre canal de communication :

| canal| statistiques disponibles|
| ------| --------------|
| e-mail | Envois, ouvertures, ouvertures uniques, clics, clics uniques, clics d'ouverture, désabonnements, rebonds, livrés, spams signalés |
| Pousser  | Envois, ouvertures, ouvertures influencées, rebonds, clics directs |
| Poussée sur le web | Envois, ouvertures, rebonds, clics du corps |
| Message in-app | Impressions, clics, clics du premier bouton, clics du deuxième bouton |
| webhook  |  Envois, erreurs |
| SMS | Envois, Envois au transporteur, Réceptions/distributions confirmées, Échecs de livraison, Rejets |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ce rapport vous permettra de répondre à d'autres questions :

- Quel est l'impact de tous mes messages de reconquête ?
- Quel est le taux de réception/distribution global de mes campagnes d'e-mail ?
- Comment se sont déroulées toutes mes campagnes Braze en juin ? Pour 2021 à ce jour ?
- Quelles sont les tendances observées en matière de tests multivariés ?

{% endtab %}
{% endtabs %}

## Comment les comportements des utilisateurs diffèrent-ils selon les segments ?

{% tabs local %}
{% tab Segment Data %}
**Données de segmentation**

Si vous avez activé le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) pour un segment, ouvrez ce segment pour afficher les [données du segment]({{site.baseurl}}/viewing_and_understanding_segment_data/). Les données de segmentation permettent de suivre les sessions, les événements personnalisés et les chiffres d'affaires au fil du temps pour les utilisateurs concernés.

Consultez cette page pour connaître ces statistiques :

- Nombre total de :
  - Utilisateurs dans votre segmentation, et quel pourcentage de votre base totale d'utilisateurs ils représentent.
  - Les utilisateurs qui ont explicitement opté pour l'envoi d'e-mails.
  - Utilisateurs ayant opté explicitement pour les notifications push.
- Valeur vie client (LTV) moyenne pour les utilisateurs de ce segment
- Liste des outils d'engagement qui ont ciblé ce segmentation.
- Statistiques des segments

{% endtab %}
{% tab Segment Insights %}
**Statistiques des segments**

Les [informations sur les segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) vous permettent de comparer les segments entre eux afin de comprendre comment les indicateurs suivants peuvent avoir un impact sur des éléments tels que la durée du cycle de vie et la fréquence des sessions :

- Données démographiques
- Plates-formes
- Statut d'abonnement
- Préférences de catégorie
- Reçu de campagne

Ce rapport vous permettra de répondre à d'autres questions :

- Quelle a été la fréquence des sessions pour les utilisateurs qui ont reçu mon canvas d'onboarding par rapport à ceux du groupe de contrôle ?
- Quelle est la différence de durée du cycle de vie entre les utilisateurs ayant opté pour le push, les utilisateurs ayant opté pour l'e-mail et les utilisateurs ayant opté pour les deux ?

{% endtab %}
{% tab Custom Events %}
**Événements personnalisés**

Utilisez la page [Événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) pour surveiller la fréquence à laquelle un événement personnalisé s'est produit, ainsi que la dernière fois que chaque utilisateur l'a effectué à des fins de segmentation.

Consultez cette page pour :

- Contrôle de la fréquence des événements personnalisés
- Surveiller les événements personnalisés par segmentation
- Analysez l'impact des campagnes sur l'activité des événements personnalisés.
- Créer et contrôler les [formules d'indicateurs clés de performance]({{site.baseurl}}/user_guide/data/creating_a_formula/)
- Résolution des problèmes liés au suivi des événements personnalisés

{% endtab %}
{% endtabs %}

## Ma campagne a-t-elle donné lieu à un retour sur investissement ?

{% tabs local %}
{% tab Revenue Data %}
**Chiffre d'affaires**

Utilisez la page [Revenus]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) pour suivre les chiffres d'affaires et les achats sur des périodes spécifiques ou le total des revenus ou des achats de votre appli.

Consultez cette page pour connaître ces statistiques :

- Résultats de la formule des indicateurs clés de performance
- Nombre d'achats de produits
- Chiffre d'affaires des différents segments
- Chiffre d'affaires pour les différents produits
- Chiffre d'affaires par heure
- Chiffre d'affaires horaire pour les différents segments
- Chiffre d'affaires par utilisateur

{% endtab %}
{% tab Global Control Group Report %}
**Rapport du groupe de contrôle global**

Après avoir mis en place un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), utilisez le [rapport de contrôle global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) pour évaluer l'impact de votre marketing Braze dans son ensemble. Ce rapport vous permet de comparer les comportements des utilisateurs qui reçoivent des messages à ceux des utilisateurs qui n'en reçoivent pas, ce qui vous permet de mieux comprendre comment vos campagnes et vos Canevas contribuent à vos objectifs métier.

Consultez cette page pour :

- Mesurez facilement l'impact et l'augmentation incrémentale des campagnes et des Canevas sur les sessions et les événements personnalisés.
- randomiser et exclure automatiquement les membres du groupe de contrôle de la réception des messages.
- Exporter les membres du groupe de contrôle pour la suite de l'analyse.

Plus de questions auxquelles vous pouvez répondre par un rapport :

- Quel a été l'effet global de l'envoi de messages Braze sur le comportement des clients ?
- Quel est le ROI de Braze en tant que plateforme (pour le renouvellement ou les discussions avec les parties prenantes) ?

{% endtab %}
{% endtabs %}

## Quelles sont les prochaines campagnes à mener ?

{% tabs local %}
{% tab Funnel Report %}

Utilisez les rapports d'entonnoir pour les [campagnes]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) ou les [Canevas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) pour analyser les parcours de vos clients après avoir reçu une campagne. Vous pouvez choisir les événements natifs ou personnalisés à inclure dans chaque analyse de tunnel, puis plonger dans les performances de chaque variante par rapport à l'entonnoir de conversion sélectionné.

Consultez ce rapport :

- Comprenez à quel endroit du tunnel de conversion les utilisateurs ont décroché et identifiez les opportunités d'envoi de messages de réengagement.
- Affichez les conversions pour un événement qui n'était pas initialement inclus en tant qu'événement de conversion lors de l'implémentation de la campagne.
- Analysez l'entonnoir d'achat à l'aide d'une série d'actions (telles que "Quel pourcentage de clients a reçu un e-mail, a démarré une session, a ajouté un article à son panier, puis a acheté ?").

Ce rapport vous permettra de répondre à d'autres questions :

- À quel endroit du chemin de la conversion mes clients s'arrêtent-ils ?
- Comment puis-je améliorer mes stratégies de marketing ?

{% endtab %}
{% tab Predictive Churn %}
**Prédiction du taux d'attrition**

Le modèle [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) est le premier modèle de la [Predictive Suite de Braze]({{site.baseurl}}/user_guide/brazeai/). Utilisez Prediction du taux d'attrition pour définir et générer des prédictions, afin d'adopter une approche proactive visant à minimiser le taux d'attrition futur.

Étant donné que chaque entreprise définit différemment le désabonnement et la rétention, il vous suffit de saisir vos définitions dans Prediction du taux d'attrition, et Braze s'occupe du reste. Vous pouvez également créer des campagnes ou des canevas pour donner suite aux prédictions ou créer des segmentations en vue d'une analyse plus approfondie.

Plus de questions auxquelles vous pouvez répondre grâce à cette fonctionnalité :

- Combien de mes utilisateurs désabonnés risquent de désabonner ?
- Quels comportements ou attributs mes utilisateurs à risque ont-ils en commun ?

{% endtab %}
{% tab Report Builder %}
**Générateur de rapports**

Utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) pour comparer les résultats de plusieurs campagnes ou Canvas en une seule vue et déterminer rapidement quelles stratégies d'engagement ont eu le plus d'impact sur vos indicateurs clés.

Consultez cette page pour :

- Créez un rapport sur les campagnes et les Canevas de la semaine ou du mois dernier, calculez les indicateurs critiques et partagez avec vos coéquipiers.
- Comparez les performances entre les variantes pour les tests multivariés et les Canevas.
- Déterminez quel canal de communication a obtenu le plus de conversion ou d'engagement pour une campagne ou un canvas spécifique.
- Suivre les tendances générales de performance d'un groupe de campagnes ou de Canevas (par exemple, tous les messages liés à une étiquette "newsletters").

Plus de questions auxquelles vous pouvez répondre grâce à cette fonctionnalité :

- Quelle a été la performance de la première version de mon e-mail de bienvenue par rapport à la seconde ?
- Quels ont été mes taux d'ouverture moyens en push ce mois-ci par rapport au mois dernier, pour une étiquette particulière ?
- Quelle lettre d'information mensuelle a obtenu le plus grand nombre de conversions ?

{% endtab %}
{% endtabs %}
