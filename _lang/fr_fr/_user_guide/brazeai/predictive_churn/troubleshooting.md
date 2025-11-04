---
nav_title: Résolution des problèmes
article_title: "Résolution prédiction du taux d'attrition des problèmes"
description: "Cet article de référence couvre certaines étapes de résolution des problèmes et considérations à garder à l'esprit lors de l'utilisation du taux d'attrition prédictif."
page_order: 3

---

# Résolution des problèmes

> Le prédiction du taux d'attrition (et tout modèle de machine learning) ne vaut que ce que valent les données dont dispose le modèle. Elle est également très dépendante de l'existence de certains volumes de données. 

## Erreurs potentielles

### Pas assez de données pour la formation 

Ce message d'erreur apparaît lorsque votre définition du désabonnement est trop restrictive et renvoie trop peu d'utilisateurs désabonnés. 

Pour y remédier, vous devrez modifier le nombre de jours et/ou les actions qui définissent le désabonnement afin de capturer davantage d'utilisateurs. Veillez à utiliser correctement les filtres `AND/OR` afin de ne pas créer de définitions trop restrictives. 

{% alert important %}
Bien que la fonction Prediction du taux d'attrition soit activée au niveau de l'entreprise, certains espaces de travail peuvent ne pas compter suffisamment d'utilisateurs pour créer des prédictions. En règle générale, vous avez besoin de 300 000 utilisateurs actifs par mois dans un seul espace de travail.
{% endalert %}

### Problèmes liés à la prédiction de la taille de l'audience

Lorsque vous créez votre audience de prédictions pour affiner le type d'utilisation sur lequel vous souhaitez que votre modèle soit entraîné, vous pouvez rencontrer ce message vous informant que votre audience de prédictions compte trop peu d'utilisateurs : 

"Il n'y a pas assez de désabonnés dans le passé pour créer des prédictions fiables".

Les données de prédictions montrent 31 désabonnés passés (conforme aux exigences) et 0 non-désabonnés passés (inférieur au minimum). Un message d'avertissement indique qu'il n'y a pas assez de désabonnés pour créer la prédiction.]({% image_buster /assets/img/churn/audience_size_error.png %})

Si la définition de votre audience de prédictions est trop stricte, vous risquez de ne pas disposer d'un vivier suffisamment important d'utilisateurs historiques et actifs. Pour y remédier, vous devrez soit modifier le nombre de jours et le type d'attributs utilisés dans cette définition, soit changer les actions qui définissent le désabonnement, soit les deux. 

Si votre audience prédictive continue à poser problème même après avoir modifié vos définitions, il se peut que vous ayez trop peu d'utilisateurs pour supporter cette fonctionnalité optionnelle. Nous vous suggérons plutôt d'essayer de créer une prédiction sans les couches et les filtres supplémentaires. 

### La taille de l'audience de prédiction est trop importante

La définition d'une audience de prédictions ne peut pas dépasser 100 millions d'utilisateurs. Si un message vous indique que votre audience est trop importante, nous vous recommandons d'ajouter des couches à votre audience ou de modifier la fenêtre de temps sur laquelle elle est basée.

### La qualité des prédictions est médiocre

\![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Si votre modèle a une [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) de 40 % ou plus, vous êtes en bonne place ! Mais si la qualité de vos prédictions tombe à 39 % ou moins, il se peut que vous deviez modifier vos définitions du taux de désabonnement et de l'audience de prédiction pour qu'elles soient plus spécifiques ou qu'elles aient des fenêtres temporelles différentes. 

Si vous n'êtes pas en mesure de respecter à la fois l'exigence relative à la taille de l'audience lors de l'élaboration de vos définitions de prédictions et d'obtenir une qualité de prédiction supérieure à 40 %, cela signifie probablement que les données envoyées à Braze ne sont pas idéales pour ce cas d'utilisation, qu'il n'y a pas suffisamment d'utilisateurs pour créer un modèle ou que le cycle de vie de votre produit est plus long que ce que notre fenêtre de rétroaction de 60 jours permet actuellement de prendre en charge. 

## Considérations sur les données

Voici les questions que vous devez vous poser lorsque vous mettez en place le système Prediction du taux d'attrition. Les modèles de machine learning ne valent que ce que valent les données qui les entraînent, c'est pourquoi avoir de bonnes pratiques d'hygiène des données et comprendre ce qui entre dans le modèle fera une grande différence.

- Quelles sont les actions à forte valeur ajoutée qui conduisent à la rétention et à la fidélisation ?
- Avez-vous mis en place des événements personnalisés qui renvoient à ces actions spécifiques ? Le système Predictive Churn fonctionne avec des événements personnalisés et non avec des attributs personnalisés.
- Pensez-vous à des fenêtres de temps à l'intérieur desquelles vous définirez le désabonnement ? Vous pouvez définir le désabonnement comme quelque chose qui se produit dans un délai maximum de 60 jours.
- Avez-vous pris en compte les périodes de l'année qui donnent lieu à des comportements atypiques de la part des utilisateurs, telles que les vacances ? L'évolution rapide du comportement des consommateurs aura un impact sur vos prédictions. 

