---
nav_title: Prédiction de l’attrition
article_title: Prédiction de l’attrition
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Prédiction de l’attrition"
guide_top_text: "L’attrition des clients, également connue sous le nom de rotation de la clientèle ou perte de clients, est l’un des indicateurs les plus importants à envisager pour les entreprises en croissance. Disposer des bons outils pour traiter l’attrition est essentiel pour minimiser les pertes et maximiser la rétention client. Pour obtenir l’avantage sur ces utilisateurs susceptibles d’abandonner, Braze propose la prédiction du taux d'attrition, offrant une approche proactive pour minimiser l’attrition future."
description: "Cette page d’accueil présente la prédiction du taux d’attrition : un outil qui vous permet de définir ce que signifie le taux d’attrition pour votre entreprise ainsi que les utilisateurs que vous souhaitez empêcher de se désabonner."

guide_featured_title: "Sujets"
guide_featured_list:
- name: Créer une prédiction d’attrition
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Analyses prédictives
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Écrire aux utilisateurs
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: Résolution des problèmes
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## Aperçu

![Un aperçu de l’attrition qui comprend une prédiction d’audience plus ancienne avec l’entraînement à partir de données d’historique. Ceci contribue à prédire le risque d’attrition futur en mesurant l’audience prédite actuelle ayant un score de risque d’attrition.][1]

> Avec la prédiction du taux d’attrition, vous pouvez définir ce qu’elle signifie pour votre entreprise ([définition de l’attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) et identifier les utilisateurs que vous souhaitez empêcher d’abandonner ([audience de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Lorsque vous créez une prédiction, Braze entraîne un modèle d'apprentissage automatique à l'aide d'[arbres de décision boostés par le gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour identifier les utilisateurs risquant de désabonner en apprenant à partir des modèles d'activité des utilisateurs passés qui ont désabonné et n'ont pas désabonné selon votre définition.

Une fois le modèle de prédiction créé, les utilisateurs de l'audience de prédiction se verront attribuer un [score de risque d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) compris entre 0 et 100, indiquant leur probabilité de désabonnement selon votre définition. Plus le score est élevé, plus il est probable que l’utilisateur abandonne. 

La mise à jour des scores de risque de l'audience de prédictions peut se faire à la [fréquence de votre choix.]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) De cette façon, vous pouvez contacter les utilisateurs qui risquent d’abandonner avant qu’ils ne le fassent réellement et l’empêcher de se produire. En utilisant jusqu'à trois prédictions actives, vous pouvez exploiter le taux d'attrition prédictif pour adapter des modèles individuels afin d'aider à prévenir le désabonnement dans des segments spécifiques de vos utilisateurs que vous considérez comme les plus précieux.

## Accéder à la prédiction du taux d'attrition

La page des **prédictions** est située dans la section **Analyse/analytique**. Pour y obtenir un accès complet, contactez votre gestionnaire de compte.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **prédictions** sous la rubrique **Engagement**.
{% endalert %}

Avant d’acheter cette fonction, vous disposez d’un mode aperçu. Il vous permettra de voir une démonstration de la prédiction du taux d’attrition avec des données synthétiques et de créer un modèle de prédiction d’attrition selon vos données utilisateur à un instant donné. Cet aperçu ne vous permettra pas de cibler des utilisateurs dans vos communications sur la base du risque d’attrition et ne se remettra pas à jour régulièrement après sa création.

Grâce à l'aperçu, vous pouvez également modifier et reconstruire votre prédiction ou l'archiver et en créer d'autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) attendue de différentes [définitions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
