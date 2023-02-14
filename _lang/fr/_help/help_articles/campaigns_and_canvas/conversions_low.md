---
nav_title: Faibles conversions dans une campagne ou un Canvas
article_title: Faibles conversions dans une campagne ou un Canvas
page_order: 4

page_type: solution
description: "Cet article d’aide décrit comment résoudre les problèmes de taux de conversion inférieurs aux prévisions dans vos campagnes ou vos Canvas."
tool:
- Canvas
- Campagnes
---

# Faibles conversions dans une campagne ou un Canvas

Les conversions se produisent lorsque votre utilisateur effectue une action dans le message que vous avez définie lors de la création de votre campagne.

Vos conversions peuvent ne pas être aussi élevées que prévu comparées aux campagnes précédentes ou à vos attentes. Les conversions sont une activité difficile, mais elles dépendent de quelques fonctions simples dans notre plateforme : le suivi des événements et les échéances de conversion.

Pour résoudre rapidement le problème, nous vous recommandons de vérifier les délais de suivi des événements et de la conversion.

## Suivi des événements

Lorsqu’une campagne déclenche un événement de début de session ou un événement personnalisé, vous voulez vous assurer que cet événement ou session est assez fréquent pour déclencher le message. Vérifiez ces données sur les pages [Overview][1] (pour les données de session) ou [Custom Events][2] (Événements personnalisés) :

![La page Événements personnalisés avec les statistiques du nombre d’Événements personnalisés.][43]

## Échéances de conversion

Pour chaque événement de conversion que vous sélectionnez par campagne, vous définissez une [échéance][44]. Cela signifie que vous définissez une limite de temps avant laquelle une conversion doit se produire pour être comptabilisée dans chaque campagne respective.

Vérifiez que vous avez examiné les informations de [calcul des conversions][45] afin de comprendre les indicateurs de votre campagne. Pour les conversions d’utilisateurs dans Canvas, reportez-vous à la [FAQ Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas). 

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 6 mai 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[43]: {% image_buster /assets/img_archive/trouble5.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule