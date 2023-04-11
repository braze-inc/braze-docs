---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de la prédiction du taux d'attrition
description: "Le présent article de référence couvre certaines étapes de résolution des problèmes et les considérations à garder à l’esprit lors de l’utilisation de la prédiction du taux d'attrition."
page_order: 3

---

# Résolution des problèmes de la prédiction du taux d'attrition

> La prédiction du taux d'attrition (et n’importe quel modèle de machine learning) est aussi juste que les données disponibles pour le modèle. Elle dépend également fortement du volume de données disponibles. Cela signifie que certains utilisateurs peuvent rencontrer des messages d’erreur ou une qualité de prédiction faible lorsqu’ils apprennent à connaître cette nouvelle fonctionnalité. 

## Erreurs potentielles

### Pas assez de données pour l’entraînement 

Ce message d’erreur s’affiche lorsque votre définition d’attrition est trop limitée et renvoie trop peu d’utilisateurs ayant abandonné. 

Pour le résoudre, vous devrez modifier le nombre de jours ou les actions qui définissent l’attrition pour capturer plus d’utilisateurs. Assurez-vous d’utiliser les filtres `AND/OR` correctement pour ne pas créer de définitions trop restrictives. 

{% alert important %}
Bien que la fonction de prédiction du taux d'attrition soit activée au niveau de la société, certains groupes d’apps peuvent ne pas avoir assez d’utilisateurs pour établir des prédictions. Généralement, vous avez besoin de 300 000 utilisateurs actifs mensuels dans un seul groupe d’apps.
{% endalert %}

### Problèmes avec la taille de l’audience de prédiction

![][3]{: style="float:right;max-width:60%;margin-left:15px;margin-bottom:15px;margin-top:15px;"}

Lorsque vous créez votre audience de prédiction pour affiner le type d’utilisation contre lequel vous souhaitez que votre modèle soit entraîné, vous pouvez rencontrer ce message vous informant que votre audience de prédiction n’a pas assez d’utilisateurs : 

« Nombre insuffisant de personnes désabonnées par le passé disponibles dans l’audience de prédiction sélectionnée au cours des 7 derniers jours pour établir la prédiction de manière fiable. »"

Si la définition de votre audience de prédiction est trop stricte, il se peut que vous ne disposiez pas d’un nombre suffisant d’utilisateurs historiques et actifs avec lequel travailler. Pour le résoudre, vous devrez soit modifier le nombre de jours et le type d’attributs utilisés dans cette définition, soit changer les actions qui définissent l’attrition. 

Si votre audience de prédiction continue à être un problème et ce même après avoir modifié vos définitions, il se peut que vous ayez trop peu d’utilisateurs pour prendre en charge cette fonctionnalité facultative. Nous suggérons d’essayer de créer à la place une prédiction sans les couches et filtres supplémentaires. 

### La taille de l’audience de prédiction est trop grande

Une audience de prédiction ne peut pas dépasser 100 millions d’utilisateurs. Si vous voyez un message indiquant que votre audience est trop grande, nous vous recommandons d’ajouter plus de couches à votre audience ou de modifier la fenêtre temporelle sur laquelle elle est basée.

### La prédiction a une qualité médiocre

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}
Si votre modèle a une [qualité de prédiction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) de 40 % ou plus, vous vous en sortez très bien ! Mais si votre qualité de prédiction chute à 39 % ou moins, vous devrez peut-être modifier vos définitions d’attrition et d’audience de prédiction pour être plus spécifiques ou avoir des fenêtres horaires différentes. 

Si vous ne parvenez pas à répondre à la fois aux exigences de taille d’audience en construisant vos définitions de prédiction et à obtenir une qualité de prédiction supérieure à 40 %, cela signifie probablement que les données envoyées à Braze ne sont pas idéales pour ce cas d’utilisation, qu’il n’y a pas assez d’utilisateurs avec lesquels construire un modèle, ou que le cycle de vie de votre produit est plus long que ce que supporte notre fenêtre actuelle de 30 jours. 

## Considérations relatives aux données

Voici quelques questions à vous poser lorsque vous configurez la prédiction du taux d'attrition. Les modèles de machine learning sont aussi juste que les données pour les entraîner. Avoir de bonnes pratiques en matière d’hygiène des données et comprendre ce qui joue sur le modèle fera une grande différence.

- Quelles actions de grande valeur mènent à la rétention et à la fidélité ?
- Avez-vous mis en place des événements personnalisés qui correspondent à ces actions spécifiques ? La prédiction du taux d'attrition fonctionne avec des événements personnalisés plutôt que des attributs personnalisés.
- Pensez-vous en termes de fenêtres temporelles pour lesquelles vous définirez l’attrition ? Vous pouvez définir l’attrition comme quelque chose qui se produit en 14 jours maximum.
- Avez-vous envisagé des moments de l’année qui conduisent à des comportements d’utilisateur atypiques, comme des vacances ? Des changements rapides dans le comportement des consommateurs auront un impact sur vos prédictions. 

[1]: {% image_buster /assets/img/churn/churn3.png %}
[3]: {% image_buster /assets/img/churn/audience_size_error.png %}