---
nav_title: Événements prévisionnels
article_title: Événements prévisionnels
description: "Cet article traite des événements prédictifs (anciennement achats prédictifs), un outil qui donne aux marketeurs la possibilité d'identifier et d'envoyer des messages aux utilisateurs en fonction de leur probabilité d'effectuer un événement."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Événements prévisionnels

> Les événements prédictifs offrent aux marketeurs un outil puissant d'identification et d'envoi de messages aux utilisateurs en fonction de leur probabilité de réaliser un événement. Lorsque vous créez une prédiction d'événement, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par le gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité précédente et prédire l'activité future.

## À propos des événements prévisionnels

Une fois la prédiction créée, les utilisateurs se voient attribuer un [score de vraisemblance]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) compris entre 0 et 100, qui indique la probabilité qu'ils réalisent l'événement sélectionné. Plus le score est élevé, plus l'utilisateur est susceptible de réaliser cet événement. Les utilisateurs sont également classés par catégories de probabilité faible, moyenne et élevée.

La véritable valeur des événements prédictifs réside dans l'utilisation des résultats des prédictions pour créer un segment ou une campagne. Les marketeurs peuvent créer des campagnes ciblées directement sur la page **Prédictions** pour obtenir des prédictions immédiates en termes de chiffre d'affaires ou enregistrer un segment pour une future campagne ou un Canvas. Vous ne savez pas qui cibler en premier ? Lisez nos [considérations stratégiques]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) pour l'envoi de messages aux utilisateurs en fonction de leur score de probabilité.

![Graphique intitulé "How Predictive Events Works", montrant les données utilisateur entonnées dans le modèle de machine learning. Le libellé est le suivant : "Entraînez-vous avec des données historiques, comparez le comportement des utilisateurs qui ont réalisé l'événement au cours d'une certaine période avec ceux qui ne l'ont pas fait." À droite se trouvent les résultats du machine learning, où les utilisateurs sont classés du moins susceptible au plus susceptible de réaliser l'événement. L'étiquette indique "Prédire la probabilité d'événements futurs, attribuer un score de probabilité aux utilisateurs pour un ciblage précis et pratique".]({% image_buster /assets/img/how_predictive_events_works.png %})

## Accès aux prédictions

La page des **prédictions** est située dans la section **Analyse/analytique**. Pour y obtenir un accès complet, contactez votre gestionnaire de compte.

Avant d’acheter cette fonction, vous disposez d’un mode aperçu. Cela vous permettra de voir une prédiction de démonstration avec des données synthétiques ainsi que de créer un modèle de prédiction de prévisualisation à la fois. Cette prédiction sera créée sur la base de vos données utilisateur réelles, mais elle ne vous permettra pas de cibler les utilisateurs pour l'envoi de messages en fonction de leur score de probabilité. Elle ne sera pas non plus mise à jour régulièrement après la création.

Avec l'aperçu, vous pouvez également modifier et reconstruire cette prédiction ou l'archiver et en créer d'autres pour tester la [qualité des prédictions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) attendues par [différentes audiences]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) et vous familiariser avec les analyses adjectives.
