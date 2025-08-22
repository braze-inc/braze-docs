---
nav_title: Arbre décisionnel 
article_title: Arbre décisionnel 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Cet article de référence explique comment créer et utiliser des arbres décisionnels dans votre Canvas."
tool: Canvas

---

# Arbre décisionnel 

> Le composant de décision de séparation dans Canvas vous permet de fournir des expériences personnalisées, en temps réel à vos utilisateurs.

![Une étape décisionnelle nommée "Push enabled ?" pour les utilisateurs qui ne sont pas push enabled et les utilisateurs qui sont push enabled.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Ce composant peut être utilisé pour créer des branches Canvas selon qu’un utilisateur corresponde à la requête ou non.

## Créer un arbre décisionnel 

Pour créer un arbre décisionnel dans votre flux de travail, ajoutez une étape à votre Canvas. Ensuite, glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Fractionnement de la décision**.

### Définissez votre fractionnement

Comment souhaitez-vous fractionner vos utilisateurs ? Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) et des filtres pour tracer la ligne. En fait, vous créez une requête `true` ou `false` qui permettra d’évaluer vos utilisateurs puis de les diriger vers une étape ou une autre. Vous devez utiliser au moins un segment ou un filtre. Vous ne devez pas utiliser à la fois un segment et un filtre.

![Une étape de l'arbre décisionnel avec le filtre "Push Enabled is true" sélectionné.]({% image_buster /assets/img/define-split-2.png %}){: style="max-width:90%;"}

{% alert note %}
Par défaut, les segments et les filtres d'une étape de l'arbre décisionnel sont vérifiés juste après la réception d'une étape précédente, sauf si vous ajoutez un délai.
{% endalert %} 

## Utiliser votre séparation

L'utilisation d'un arbre décisionnel peut vous aider à distinguer les parcours de vos utilisateurs en fonction de leur segmentation ou de leurs attributs, voire du fait qu'ils utilisent certains canaux de communication pour recevoir vos messages !

Supposons que vous créiez un flux d’onboarding. Vous pourriez commencer par un e-mail de bienvenue lors de l’inscription. Puis deux jours plus tard, vous souhaitez envoyer un message de notification push mais uniquement aux utilisateurs ayant activé la notification push. Puis, tous les utilisateurs reçoivent un autre e-mail trois jours plus tard après l’inscription. Vous pourriez également utiliser votre décision de séparation pour envoyer un message in-app aux utilisateurs pour les inciter à activer la notification push s’ils ne l’ont pas fait.

S’il n’y a pas d’étape suivante dans le parcours, les utilisateurs arrivés à la fin de ce parcours quitteront le Canvas. 

![Une étape de l'arbre décisionnel intitulée "Push enabled ?" pour les utilisateurs qui ne sont pas équipés de la fonction Push et ceux qui le sont. Les utilisateurs qui ne disposent pas de la fonction "push" verront un délai de trois jours avant de recevoir un message par e-mail. Les utilisateurs qui utilisent la fonction "push" connaîtront un délai d'un jour, recevront une notification push suivie d'un délai de deux jours, puis recevront le même message e-mail que les utilisateurs qui n'utilisent pas la fonction "push".]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analyse

Reportez-vous au tableau suivant pour consulter les descriptions d'analyse pour cette étape :

| Indicateur | Description |
|---|---|
| _Saisie_ | Le nombre total de fois où l’étape a été saisie. Si votre canvas est rééligible et qu'un utilisateur entre deux fois dans une étape d'arbre décisionnel, deux entrées seront enregistrées. |
| _Oui_ | Le nombre d’entrées répondant aux critères indiqués et permettant d’accéder au parcours « oui ». |
| _Non_ | Le nombre d’entrées ne répondant pas aux critères indiqués et permettant d’accéder au parcours « non ». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

