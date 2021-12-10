---
nav_title: Église prédictive
article_title: Église prédictive
page_order: 6.4
layout: en vedette
alias: /fr_FR/fr_FR/
guide_top_header: "Église prédictive"
guide_top_text: "L'Église de la clientèle, également connue sous le nom de chiffre d'affaires de la clientèle ou de perte de la clientèle, est l'une des mesures les plus importantes à prendre en compte pour les entreprises en croissance. Il est essentiel de disposer des outils adéquats pour s’attaquer à la perte et maximiser la rétention de la clientèle. Pour faire un saut sur ces utilisateurs potentiellement mordants, Braze offre une Église prédictive qui offre une approche proactive pour minimiser la désunion future."
description: "Avec Église prédictive, vous pouvez définir ce que churn signifie pour la définition de votre entreprise ainsi que pour les utilisateurs que vous souhaitez empêcher de faire des audiences prévisionnelles."
guide_featured_title: "Sujets"
guide_featured_list:
  - 
    name: Créer une prédiction de la nature
    link: /fr/docs/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/
    fa_icon: fas fa-cogs
  - 
    name: Analyses de prédiction
    link: /fr/docs/user_guide/predictive_suite/predictive_churn/prediction_analytics/
    fa_icon: fas fa-chart-bar
  - 
    name: Utilisateurs de messagerie
    link: /fr/docs/user_guide/predictive_suite/predictive_churn/messaging_users/
    fa_icon: fas fa-flèche-droite
  - 
    name: Foire aux questions
    link: /fr/docs/user_guide/predictive_suite/predictive_churn/prediction_faq/
    fa_icon: fas fa-question
---

!\[Vue d'ensemble de Churn\]\[1\]

## Aperçu

Avec Église prédictive, vous pouvez définir ce que churn signifie pour votre entreprise ([Churn Definition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) ainsi que les utilisateurs que vous souhaitez empêcher de retourner ([Prediction Audience]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Lorsque vous créez une prédiction, Braze forme un modèle d'apprentissage automatique à l'aide de [arbres de décision rehaussés de gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour identifier les utilisateurs à risque de morsure en apprenant à partir des modèles d'activité des utilisateurs précédents qui ont fait et n'ont pas croulé selon votre définition.

Une fois que le modèle de prédiction est construit, les utilisateurs de l'Audience de Prédiction seront assignés à un [Score de Risque de Coeur]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 et 100 indiquant la probabilité qu'ils soient à Churn selon votre définition. Plus le score est élevé, plus un utilisateur est susceptible de comploter.

La mise à jour des scores de risque de l'Audience de Prédiction peut être faite avec une [fréquence que vous choisissez]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). De cette façon, vous pouvez contacter les utilisateurs qui risquent de cracher avant qu'ils ne le fassent réellement et éviter que cela ne se produise. Utiliser jusqu'à trois prédictions actives, vous pouvez utiliser Predictive Churn pour adapter des modèles individuels afin de prévenir la présence de véhicules dans certains segments de vos utilisateurs que vous jugez les plus précieux.

## Accéder à la église prédictive

La page Predictions est accessible à partir de la barre de navigation de gauche sur le tableau de bord de Braze. Pour un accès complet, contactez votre responsable de compte. Avant d'acheter cette fonctionnalité, elle est disponible en mode Aperçu. Cela vous permettra de voir une prédiction de la communauté de démonstration avec des données synthétiques ainsi que de créer un modèle de prédiction de la communauté à la fois. Cette prédiction sera créée en fonction de vos données utilisateur réelles, mais cela ne vous permettra pas de cibler les utilisateurs pour la messagerie selon Churn Risk. Il ne sera pas mis à jour régulièrement après la création.

Avec l'aperçu, vous pouvez également modifier et reconstruire cette Prédiction ou l'archiver et en créer d'autres pour tester la [Qualité de Prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) attendue de [définitions]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>
[1]: {% image_buster /assets/img/churn/churn_overview.png %}
