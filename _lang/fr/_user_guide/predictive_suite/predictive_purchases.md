---
nav_title: Achats prédictifs
article_title: Achats prédictifs
page_order: 6.4
layout: dev_guide
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "Achats prédictifs"
guide_top_text: "Savoir lequel de vos utilisateurs est susceptible de réaliser un achat est une connaissance cruciale pour les entreprises en croissance. Sans cela, comment décidez-vous quelles campagnes construire ? Qui devrait recevoir des remises et des promotions ? Où dépenser un budget limité ? Braze aide à répondre à ces questions grâce aux Achats prédictifs, un modèle de machine learning qui permet aux équipes marketing de comprendre le comportement d’achat futur et de concentrer leurs ressources sur les campagnes maximisant les revenus."
description: "Cet article présente les achats prédictifs : un outil qui permet aux marketeurs d’identifier et de communiquer avec des utilisateurs en fonction de leur probabilité de réaliser un achat. "

guide_featured_title: "Sujets"
guide_featured_list:
- name: Créer une prédiction d’achat
  link: /docs/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Analyses prédictives
  link: /docs/user_guide/predictive_suite/predictive_purchases/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Écrire aux utilisateurs
  link: /docs/user_guide/predictive_suite/predictive_purchases/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## Aperçu

![Graphique intitulé « Comment fonctionnent les achats prédictifs ». Sur la gauche, les données utilisateur sont acheminées dans le modèle de machine learning. L’étiquette indique « Entrainez avec des données historiques, comparez les comportements avant achat lors des achats précédents avec ceux des achats potentiels ». Sur la droite, on peut voir les résultats du machine learning dans lesquels les utilisateurs sont classés des moins susceptibles aux plus susceptibles d’acheter. L’étiquette indique « Prédisez la probabilité des futurs achats, attribuez un score de probabilité d’achat aux utilisateurs pour un ciblage précis et pratique ».][1]

> Les achats prédictifs donnent aux marketeurs un outil puissant pour identifier et communiquer avec les utilisateurs en fonction de leur probabilité de réaliser un achat.  Lorsque vous créez une prédiction d’achat, Braze entraîne un modèle de machine learning en utilisant des [arbres de décision à gradient renforcé](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l’activité d’achat précédente et prévoir la future. 

Une fois que la prédiction est construite, les utilisateurs se voient attribuer un [Score de probabilité d’achat]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score) entre 0 et 100 indiquant la probabilité qu’ils effectuent un achat. Plus ce score est élevé, plus il est probable que l’utilisateur achète. Les utilisateurs sont également triés par catégories de probabilité d’achat faible, moyenne et élevée. 

La valeur réelle des achats prédictifs réside dans l’utilisation des résultats de prédiction pour créer un segment ou une campagne. Les marketeurs peuvent élaborer des campagnes ciblées directement sur la page **Predictions** pour obtenir des résultats immédiats d’augmentation des revenus ou enregistrer un segment pour une future campagne ou Canvas. Vous ne savez pas qui cibler en premier ? Consultez nos [considérations stratégiques]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy) pour écrire aux utilisateurs en fonction de leur probabilité d’achat.

## Accéder aux achats prédictifs

La page **Predictions** est accessible depuis la barre de navigation de gauche sur le tableau de bord de Braze. Pour y obtenir un accès complet, contactez votre gestionnaire de compte. Avant d’acheter cette fonction, vous disposez d’un mode Aperçu. Il vous permettra de voir une démonstration de la prédiction d’achat avec des données synthétiques et de créer un modèle de prédiction d’achat à un moment donné. Cette prédiction sera créée en fonction de vos données utilisateur réelles, mais elle ne vous permettra pas de cibler les utilisateurs pour la messagerie sur la base de la probabilité d’achat. Elle ne sera pas non plus mise à jour régulièrement après la création.

Avec l’aperçu, vous pouvez également modifier et reconstruire cette prédiction ou l’archiver et en créer d’autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality) attendue de [différentes audiences]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#audience) et vous familiariser avec les analytiques.

<br><br>

[1]: {% image_buster /assets/img/purchasePrediction/purchasesOverview.png %}

