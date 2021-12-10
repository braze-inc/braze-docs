---
nav_title: Conversions de campagne ou de canvas basses
article_title: Conversions de campagne ou de canvas basses
page_order: 4
page_type: Solution
description: "Cet article d'aide vous guide à travers des campagnes de dépannage ou des Canvases avec des taux de conversion inférieurs à ceux prévus."
tool:
  - Toile
  - Campagnes
---

# Conversion de campagne ou de Canvas basse

Vos conversions (lorsque votre utilisateur effectue une action dans le cadre de votre message que vous avez défini lors de la création de votre campagne) peuvent ne pas être aussi élevées que vous vous y attendez par rapport aux campagnes précédentes ou à vos attentes. Les conversions sont une entreprise délicate, mais elles dépendent de quelques fonctions simples sur notre plateforme : le suivi des événements et les délais de conversion.

Pour résoudre rapidement les problèmes, nous vous recommandons :

* [Vérifier le suivi des événements](#ensure-the-event-is-tracking)
* [Vérifier la date limite](#verify-the-deadline-to-convert)


## S'assurer que l'événement est en cours de suivi

Lorsqu'une campagne déclenche un début de session ou un événement personnalisé, vous voulez vous assurer que cet événement ou la session se produit assez souvent pour déclencher le message. Vérifiez ces données sur les pages [Aperçu][1] (pour les données de session) ou [Événements personnalisés][2]:

!\[Statistiques personnalisées des compteurs d'événements\]\[43\]

## Vérifiez la date limite de conversion

Pour chaque événement de conversion que vous sélectionnez par campagne, vous avez fixé la [date limite][44]. Cela signifie que vous définissez une limite de temps dans laquelle une conversion doit avoir lieu pour qu'elle puisse être prise en compte dans chaque campagne.

Vérifiez que vous avez vérifié les informations sur [le calcul des conversions][45] afin de comprendre les métriques de votre campagne.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 6 mai 2021_
[43]: {% image_buster /assets/img_archive/trouble5.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule