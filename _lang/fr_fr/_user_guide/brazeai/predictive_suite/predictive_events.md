---
nav_title: Événements prévisionnels
article_title: Événements prévisionnels
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "Événements prévisionnels"
guide_top_text: "Savoir lequel de vos utilisateurs est susceptible de réaliser un événement spécifique, comme un achat, est une information cruciale pour les entreprises en pleine croissance. Sans cela, comment décidez-vous quelles campagnes créer ? Qui devrait recevoir des remises et des promotions ? Où dépenser un budget limité ? Braze aide à répondre à ces questions avec Predictive Events (anciennement Predictive Purchases), un modèle de machine learning qui permet aux équipes marketing de comprendre facilement les comportements futurs et de concentrer leurs ressources sur l'engagement et les campagnes maximisant le chiffre d'affaires."
description: "Cet article traite des événements prédictifs (anciennement achats prédictifs), un outil qui donne aux marketeurs la possibilité d'identifier et d'envoyer des messages aux utilisateurs en fonction de leur probabilité d'effectuer un événement."

guide_featured_title: "Sujets"
guide_featured_list:
- name: "Création d'une prédiction"
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Analyses prédictives
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Écrire aux utilisateurs
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## Aperçu

![Graphique intitulé "How Predictive Events Works", montrant les données utilisateur entonnées dans le modèle de machine learning. Le libellé est le suivant : "Entraînez-vous avec des données historiques, comparez le comportement des utilisateurs qui ont réalisé l'événement au cours d'une certaine période avec ceux qui ne l'ont pas fait." À droite se trouvent les résultats du machine learning, où les utilisateurs sont classés du moins susceptible au plus susceptible de réaliser l'événement. Le libellé est le suivant : "Prédire la probabilité d'événements futurs, attribuer un score de probabilité aux utilisateurs pour un ciblage précis et pratique."][1]

> Les événements prédictifs offrent aux marketeurs un outil puissant d'identification et d'envoi de messages aux utilisateurs en fonction de leur probabilité de réaliser un événement. Lorsque vous créez une prédiction d'événement, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par le gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité précédente et prédire l'activité future.

Une fois la prédiction créée, les utilisateurs se voient attribuer un [score de vraisemblance]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) compris entre 0 et 100, qui indique la probabilité qu'ils réalisent l'événement que vous avez choisi. Plus le score est élevé, plus l'utilisateur est susceptible de réaliser cet événement. Les utilisateurs sont également classés par catégories de probabilité faible, moyenne et élevée.

La véritable valeur des événements prédictifs réside dans l'utilisation des résultats des prédictions pour créer un segment ou une campagne. Les marketeurs peuvent créer des campagnes ciblées directement sur la page **Prédictions** pour obtenir des prédictions immédiates en termes de chiffre d'affaires ou enregistrer un segment pour une future campagne ou un Canvas. Vous ne savez pas qui cibler en premier ? Lisez nos [considérations stratégiques]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) pour l'envoi de messages aux utilisateurs en fonction de leur score de probabilité.

## Accéder aux événements prévisionnels

La page des **prédictions** est située dans la section **Analyse/analytique**. Pour y obtenir un accès complet, contactez votre gestionnaire de compte.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **prédictions** sous la rubrique **Engagement**.
{% endalert %}

Avant d’acheter cette fonction, vous disposez d’un mode aperçu. Cela vous permettra de voir une prédiction de démonstration avec des données synthétiques ainsi que de créer un modèle de prédiction de prévisualisation à la fois. Cette prédiction sera créée sur la base de vos données utilisateur réelles, mais elle ne vous permettra pas de cibler les utilisateurs pour l'envoi de messages en fonction de leur score de probabilité. Elle ne sera pas non plus mise à jour régulièrement après la création.

Avec l'aperçu, vous pouvez également modifier et reconstruire cette prédiction ou l'archiver et en créer d'autres pour tester la [qualité des prédictions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) attendues par [différentes audiences]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) et vous familiariser avec les analyses adjectives.

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

