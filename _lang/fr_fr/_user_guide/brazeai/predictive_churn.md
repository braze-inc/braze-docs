---
nav_title: "Prédiction du taux d'attrition"
article_title: "Prédiction du taux d'attrition"
description: "Cette page d'atterrissage présente Predictive Churn, un outil qui vous permet de définir ce que le désabonnement signifie pour votre entreprise ainsi que les utilisateurs que vous aimeriez empêcher de désabonner."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Prédiction du taux d'attrition

> Avec Prediction du taux d'attrition, vous pouvez définir ce que le taux d'attrition signifie pour votre entreprise et identifier les utilisateurs que vous souhaitez conserver. Lorsque vous créez une prédiction, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour reconnaître les utilisateurs à risque en analysant les prédictions de leur comportement passé, qu'il s'agisse d'utilisateurs ayant désabonné ou non.

{% alert tip %}
Pour plus d'informations, voir [Définition du désabonnement]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) et [audience des prédictions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## À propos de la prédiction du taux d'attrition

Une fois le modèle de prédiction créé, les utilisateurs [désabonnés]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) de l'audience de prédiction se verront attribuer un [score de risque d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) compris entre 0 et 100, indiquant leur probabilité de désabonner selon votre définition. Plus le score est élevé, plus l'utilisateur est susceptible de se désabonner. 

La mise à jour des scores de risque de l'audience de prédictions peut se faire à la [fréquence de votre choix.]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) Vous pouvez ainsi contacter les utilisateurs désabonnés avant qu'ils ne le soient et éviter que cela ne se produise. En utilisant jusqu'à trois prédictions actives, vous pouvez exploiter le taux d'attrition prédictif pour adapter des modèles individuels afin d'aider à prévenir le désabonnement dans des segments spécifiques de vos utilisateurs que vous considérez comme les plus précieux.

!Un aperçu du désabonnement, qui comprend une audience de prédictions passées avec un entraînement à l'aide de données historiques. Cela permet de prédire le risque de désabonnement futur en mesurant l'audience prédite aujourd'hui à l'aide d'un score de risque de désabonnement.]({% image_buster /assets/img/churn/churn_overview.png %})

## Accéder au taux prédictionnel de désabonnement

La page des **prédictions** est située dans la section **Analyse/analytique**. Pour un accès complet, contactez votre gestionnaire de compte.

Avant d'être achetée, cette fonctionnalité est disponible en mode aperçu. Cela vous permettra de voir une démo de prédiction de désabonnement avec des données synthétiques et de créer un modèle de prédiction de désabonnement basé sur vos données utilisateur à la fois. Cet aperçu ne vous permettra pas de cibler les utilisateurs désabonnés pour l'envoi de messages en fonction du risque de désabonnement et ne sera pas régulièrement mis à jour après la création.

Grâce à l'aperçu, vous pouvez également modifier et reconstruire votre prédiction ou l'archiver et en créer d'autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) attendue de différentes [définitions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
