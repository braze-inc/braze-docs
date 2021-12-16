---
nav_title: Dépannage
article_title: Dépannage de la région prédictive
description: "Cet article de référence couvre certaines étapes de dépannage et les considérations à garder à l'esprit lors de l'utilisation de la Église prédictive."
page_order: 3
---

# Dépannage de la région prédictive

> Église prédictive (et tout modèle d'apprentissage automatique) n'est pas aussi bonne que les données disponibles pour le modèle. il est aussi très dépendant d'avoir certains volumes de données avec lesquels travailler. Cela signifie que les utilisateurs peuvent rencontrer des messages d'erreur, ou une faible qualité de prédiction, car ils apprennent à connaître cette nouvelle fonctionnalité.

## Erreurs potentielles

### Pas assez de données pour former

Ce message d’erreur apparaît lorsque votre définition de churn est trop limitée et renvoie trop peu d’utilisateurs.

Pour résoudre ce problème, vous devrez changer le nombre de jours et/ou d'actions qui définissent churn pour capturer plus d'utilisateurs. Assurez-vous que vous utilisez correctement les filtres `ET/OU` afin de ne pas créer de définitions trop restrictives.

{% alert important %}
Bien que Predictive Churn soit activé au niveau de l'entreprise, certains groupes d'applications peuvent ne pas avoir assez d'utilisateurs pour construire des prédictions. Généralement, vous avez besoin de 300 000 utilisateurs actifs mensuels dans un seul groupe d'applications.
{% endalert %}

### Problèmes avec la taille de l'audience de prédiction
!\[Predicition Size\]\[3\]{: style="float:right;max-width:60%;margin-left:15px;margin-bottom:15px;margin-top:15px;"}

Lors de la création de votre audience de prédiction pour affiner le type d'utilisation auquel vous voulez que votre modèle soit formé, vous pourriez rencontrer ce message vous informant que votre audience prédiction a trop peu d'utilisateurs.

Si votre définition d'audience de prédiction est trop stricte, il se peut que vous n'ayez pas suffisamment d'utilisateurs historiques et actifs pour travailler.

Pour résoudre ceci, vous devrez soit modifier le nombre de jours et le type d'attributs utilisés dans cette définition et/ou changer les actions qui définissent churn.

Si votre Audience de Prédiction reste un problème même après avoir modifié vos définitions, vous pouvez avoir trop peu d'utilisateurs pour prendre en charge cette fonctionnalité optionnelle. Nous vous suggérons d'essayer de construire une prédiction sans les couches et les filtres supplémentaires.

### La taille de l'audience de prédiction est trop grande

Une définition d'audience de prédiction ne peut excéder 100 millions d'utilisateurs. Si vous voyez un message disant que votre audience est trop grande, alors nous vous recommandons d'ajouter plus de calques à votre auditoire et/ou de changer la fenêtre de l'heure sur laquelle il se base.

### La prédiction a une mauvaise qualité
!\[Predicition Quality\]\[1\]{: style="float:right;max-width:40%;margin-left:15px;"} Si votre modèle a une qualité de prédiction de 40% et plus, vous êtes dans un endroit génial! Mais si votre qualité de prédiction tombe à 39% et ci-dessous, vous devrez peut-être modifier votre Église, et les définitions de l'audience de prédiction pour être plus spécifiques ou avoir des fenêtres de temps différentes.

Si vous n'êtes pas en mesure de répondre aux deux exigences de taille d'audience tout en construisant vos définitions de prédiction et en atteignant une qualité de prédiction supérieure à 40%, cela signifie probablement que les données envoyées à Braze ne sont pas idéales pour ce cas d'utilisation, qu'il n'y a pas assez d'utilisateurs avec lesquels construire un modèle avec, ou que le cycle de vie de votre produit est plus long que le support de notre fenêtre de retour actuelle de 30 jours.

## clarifications du chronométrage

Vous pouvez regarder jusqu'à 14 jours en arrière en fonction de votre prédiction. Votre définition de "churn" et votre fenêtre de temps pour n'importe quel achat de dernière fois/dernière application utilisée/dernier événement personnalisé dans la définition de l'audience de prédiction ne peut pas ajouter jusqu'à plus de 30 jours.

Par exemple, si vous définissez churn comme ne débutant pas de session dans les dix derniers jours, alors votre Audience de Prédiction peut être basée sur 20 jours de données.

## Considérations de données

Vous trouverez ci-dessous quelques questions à vous poser lorsque vous aurez mis en place l’Église prédictive. Les modèles d'apprentissage automatique sont aussi bons que les données qui les forment, donc avoir de bonnes pratiques d'hygiène des données et comprendre ce qui entre dans le modèle fera une grande différence.

- Quelles actions de grande valeur mènent à la rétention et à la loyauté?
- Avez-vous configuré des événements personnalisés qui correspondent à ces actions spécifiques ? Predictive Churn fonctionne avec des événements personnalisés par opposition aux attributs personnalisés.
- Pensez-vous dans des fenêtres de temps à l'intérieur desquelles vous définissez l'église? Vous pouvez définir churn comme quelque chose qui se passe en 14 jours.
- Avez-vous pensé à des périodes de l'année qui conduisent à des comportements atypiques des utilisateurs - comme des vacances. Des changements rapides dans le comportement des consommateurs influenceront vos prédictions.
[1]: {% image_buster /assets/img/churn/churn3.png %} [3]: {% image_buster /assets/img/churn/audience_size_error.png %}