---
nav_title: Achats prédictifs
article_title: Achats prédictifs
page_order: 6.4
layout: en vedette
alias: /achats prévisibles/
guide_top_header: "Achats prédictifs"
guide_top_text: "Savoir lequel de vos utilisateurs est susceptible de faire un achat est une idée cruciale pour les entreprises en pleine croissance. Sans elle, comment décidez-vous des campagnes à construire? Qui devrait recevoir des remises et des promotions? Où dépenser un budget limité ? Braze aide à répondre à ces questions avec des achats prévisionnels, un modèle d’apprentissage automatique qui permet aux équipes de marketing de comprendre facilement le comportement d’achat futur et de concentrer leurs ressources sur des campagnes de maximisation des revenus."
description: "Les achats prédictifs offrent aux marketeurs un outil puissant pour identifier et envoyer des messages en fonction de leur probabilité de faire un achat."
guide_featured_title: "Sujets"
guide_featured_list:
  - 
    name: Créer une prédiction d'achat
    link: /fr/docs/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/
    fa_icon: fas fa-cogs
  - 
    name: Analyses de prédiction
    link: /fr/docs/user_guide/predictive_suite/predictive_purchases/prediction_analytics/
    fa_icon: fas fa-chart-bar
  - 
    name: Utilisateurs de messagerie
    link: /fr/docs/user_guide/predictive_suite/predictive_purchases/messaging_users/
    fa_icon: fas fa-flèche-droite
---

## Aperçu

!\[aperçu des achats prévisionnels\]\[1\]

Les achats prédictifs offrent aux marketeurs un outil puissant pour identifier et envoyer des messages en fonction de leur probabilité de faire un achat. Lorsque vous créez une prévision d'achat, Braze forme un modèle d'apprentissage automatique à l'aide de [arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité d'achat précédente et prédire l'activité d'achat future.

Une fois qu'une prédiction est construite, les utilisateurs se voient assigner un [Achat Likelihood Score]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score) entre 0 et 100 indiquant à quel point ils sont susceptibles de faire un achat. Plus le score est élevé, plus un utilisateur est susceptible de faire un achat. Les utilisateurs sont également triés par catégories de Likelihood Bas, Moyennes et Hautes Achats.

La valeur réelle des achats prédictifs consiste à utiliser les résultats de prédiction pour créer un segment ou une campagne. Les marketeurs peuvent construire des campagnes ciblées directement sur la page __Prédiction__ pour obtenir des résultats immédiats qui stimulent les revenus ou enregistrer un segment pour une future campagne ou Canvas. Vous ne savez pas qui cibler en premier ? Lisez nos [considérations stratégiques]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy) pour les utilisateurs de messagerie en fonction de leur probabilité d'achat.

## Accéder aux achats prédictifs

La page __Prédictions__ est accessible à partir de la barre de navigation de gauche sur le tableau de bord de Braze. Pour un accès complet, contactez votre responsable de compte. Avant d'acheter cette fonctionnalité, elle est disponible en mode Aperçu. Cela vous permettra de voir une prédiction d'achat de démo avec des données synthétiques ainsi que de créer un modèle de prévision d'achat d'aperçu à la fois. Cette prédiction sera créée en fonction de vos données utilisateur réelles, mais cela ne vous permettra pas de cibler les utilisateurs pour la messagerie selon Achat Likelihood. Il ne sera pas mis à jour régulièrement après la création.

Avec l'aperçu, vous pouvez également modifier et reconstruire cette Prédiction ou l'archiver et en créer d'autres pour tester la [Qualité de Prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality) attendue de [publics différents]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#audience) et vous familiariser avec les analytiques.

<br><br>
[1]: {% image_buster /assets/img/purchasePrediction/purchasesOverview.png %}

