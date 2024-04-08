---
nav_title: Prédiction du taux d'attrition
article_title: Prédiction du taux d'attrition
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Prédiction du taux d'attrition"
guide_top_text: "L’attrition des clients, également connue sous le nom de rotation de la clientèle ou perte de clients, est l’un des indicateurs les plus importants à envisager pour les entreprises en croissance. Disposer des bons outils pour traiter l’attrition est essentiel pour minimiser les pertes et maximiser la rétention client. Pour obtenir l’avantage sur ces utilisateurs susceptibles d’abandonner, Braze propose la prédiction du taux d'attrition, offrant une approche proactive pour minimiser l’attrition future."
description: "Cette page d’accueil présente la prédiction du taux d’attrition : un outil qui vous permet de définir ce que signifie le taux d’attrition pour votre entreprise ainsi que les utilisateurs que vous souhaitez empêcher de se désabonner."

guide_featured_title: "Sujets"
guide_featured_list:
- name: Créer une prédiction d’attrition
  link: /docs/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Analyses prédictives
  link: /docs/user_guide/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Écrire aux utilisateurs
  link: /docs/user_guide/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: Résolution des problèmes
  link: /docs/user_guide/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## Aperçu

![Un aperçu de l’attrition qui comprend une prédiction d’audience plus ancienne avec l’entraînement à partir de données d’historique. Ceci contribue à prédire le risque d’attrition futur en mesurant l’audience prédite actuelle ayant un score de risque d’attrition.][1]

> Avec la prédiction du taux d’attrition, vous pouvez définir ce qu’elle signifie pour votre entreprise ([définition de l’attrition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) ainsi que les utilisateurs que vous souhaitez empêcher d’abandonner ([prédiction de l’audience]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Lorsque vous créez une prédiction, Braze entraîne un modèle de machine learning en utilisant des [arbres de décision à gradient renforcé](https://en.wikipedia.org/wiki/Gradient_boosting) pour identifier les utilisateurs à risque d’attrition en l’entraînant à partir des modèles d’activité des utilisateurs passés qui ont et n’ont pas abandonné selon votre définition.

Une fois le modèle de prédiction créé, les utilisateurs situés dans la prédiction de l’audience recevront un [score de risque d’attrition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score) compris entre 0 et 100 indiquant dans quelle mesure ils sont susceptibles d’abandonner selon votre définition. Plus le score est élevé, plus il est probable que l’utilisateur abandonne. 

La mise à jour des scores de risque de la prédiction de l’audience peut être effectuée selon la [fréquence que vous choisissez]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). De cette façon, vous pouvez contacter les utilisateurs qui risquent d’abandonner avant qu’ils ne le fassent réellement et l’empêcher de se produire. En utilisant jusqu’à trois prédictions actives, vous pouvez tirer parti de la fonction de Prédiction du taux d'attrition pour adapter les modèles individuels afin d’éviter l’attrition au sein de certains segments spécifiques de vos utilisateurs que vous considérez comme étant les plus précieux.

## Accéder à la prédiction du taux d'attrition

La page **Predictions** est accessible depuis la barre de navigation de gauche sur le tableau de bord de Braze. Pour y obtenir un accès complet, contactez votre gestionnaire de compte Braze. 

Avant d’acheter cette fonction, vous disposez d’un mode aperçu. Il vous permettra de voir une démonstration de la prédiction du taux d’attrition avec des données synthétiques et de créer un modèle de prédiction d’attrition selon vos données à un instant donné. Cet aperçu ne vous permettra pas de cibler des utilisateurs dans vos communications sur la base du risque d’attrition et ne se remettra pas à jour régulièrement après sa création.

Avec l’aperçu, vous pouvez également modifier et reconstruire votre prédiction ou l’archiver et en créer d’autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) attendue de différentes [définitions]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
