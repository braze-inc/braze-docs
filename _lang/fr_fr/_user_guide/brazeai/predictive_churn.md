---
nav_title: Prédiction de l’attrition
article_title: Prédiction du taux d’attrition
description: "Cette page d'atterrissage présente Predictive Churn, un outil de la Predictive Suite de Braze qui vous permet de définir ce que le désabonnement signifie pour votre entreprise ainsi que les utilisateurs que vous aimeriez empêcher de désabonner."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Prédiction du taux d’attrition

> Avec Predictive Churn, un outil de la Predictive Suite de Braze, vous pouvez définir ce que le désabonnement signifie pour votre entreprise et identifier les utilisateurs que vous souhaitez conserver. Lorsque vous créez une prédiction, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour reconnaître les utilisateurs à risque en analysant les prédictions de leur comportement passé, qu'il s'agisse d'utilisateurs ayant désabonné ou non.

{% alert tip %}
Pour plus d'informations, voir [Définition du désabonnement]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) et [audience des prédictions]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## À propos de la prédiction du taux d'attrition

Une fois le modèle de prédiction créé, les utilisateurs désabonnés de l'audience de prédiction se verront attribuer un [score de risque d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) compris entre 0 et 100, indiquant leur probabilité de désabonner selon votre définition. Plus le score est élevé, plus il est probable que l’utilisateur abandonne. 

La mise à jour des scores de risque de l'audience de prédictions peut se faire à la [fréquence de votre choix.]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction) Vous pouvez ainsi contacter les utilisateurs désabonnés avant qu'ils ne se désabonnent et éviter que cela ne se produise. En utilisant jusqu'à trois prédictions actives, vous pouvez exploiter le taux d'attrition prédictif pour adapter des modèles individuels afin d'aider à prévenir le désabonnement dans des segments spécifiques de vos utilisateurs que vous considérez comme les plus précieux.

![Un aperçu de l’attrition qui comprend une prédiction d’audience plus ancienne avec l’entraînement à partir de données d’historique. Ceci contribue à prédire le risque d’attrition futur en mesurant l’audience prédite actuelle ayant un score de risque d’attrition.]({% image_buster /assets/img/churn/churn_overview.png %})

## Accéder au taux prédictionnel de désabonnement

La page des **prédictions** est située dans la section **Analyse/analytique**. Pour y obtenir un accès complet, contactez votre gestionnaire de compte.

Avant d’acheter cette fonction, vous disposez d’un mode aperçu. Il vous permettra de voir une démonstration de la prédiction du taux d’attrition avec des données synthétiques et de créer un modèle de prédiction d’attrition selon vos données utilisateur à un instant donné. Cet aperçu ne vous permettra pas de cibler des utilisateurs dans vos communications sur la base du risque d’attrition et ne se remettra pas à jour régulièrement après sa création.

Grâce à l'aperçu, vous pouvez également modifier et reconstruire votre prédiction ou l'archiver et en créer d'autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) attendue de différentes [définitions]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
