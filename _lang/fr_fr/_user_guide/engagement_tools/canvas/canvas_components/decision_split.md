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

> Le composant Decision Split de Canvas vous permet d'offrir des expériences personnalisées et en temps réel à vos utilisateurs.

!Une étape décisionnelle intitulée "Push enabled ?" pour les utilisateurs qui ne sont pas push enabled et les utilisateurs qui sont push enabled.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Ce composant peut être utilisé pour créer des branches de Canvas en fonction de la correspondance d'un utilisateur à une requête.

## Créer un arbre décisionnel 

Pour créer un arbre décisionnel dans votre flux de travail, ajoutez une étape à votre Canvas. Ensuite, glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Fractionnement de la décision**.

### Définissez votre répartition

Comment voulez-vous répartir vos utilisateurs ? Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) et des filtres pour tracer la ligne. Essentiellement, vous créez une requête `true` ou `false` qui évaluera vos utilisateurs et les entonnera ensuite vers une étape ou une autre. Vous devez utiliser au moins une segmentation ou un filtre. Il n'est pas nécessaire d'utiliser à la fois un segment et un filtre.

!Une étape de l'arbre décisionnel avec le filtre "Foreground Push Enabled is true" sélectionné.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Par défaut, les segments et les filtres d'une étape de l'arbre décisionnel sont vérifiés juste après la réception d'une étape précédente, sauf si vous ajoutez un délai.
{% endalert %} 

## Utilisez votre fractionnement

L'utilisation d'un arbre décisionnel peut vous aider à distinguer les parcours de vos utilisateurs en fonction de leur segmentation ou de leurs attributs, même s'ils utilisent certains canaux de communication pour recevoir vos messages !

Disons que vous créez un flux d'onboarding. Vous pouvez commencer par envoyer un e-mail de bienvenue lors de l'inscription. Puis, deux jours plus tard, vous souhaitez envoyer un message push, mais uniquement aux utilisateurs qui ont la fonction push activée. Ensuite, tous les utilisateurs reçoivent un autre e-mail trois jours après leur inscription. Vous pourriez également utiliser votre arbre décisionnel pour envoyer un message in-app aux utilisateurs qui n'ont pas activé push pour les encourager à le faire.

Si aucune étape ne suit l'un des chemins, les utilisateurs qui empruntent ce chemin quitteront le Canvas. 

!Une étape décisionnelle intitulée "Push enabled ?" pour les utilisateurs qui ne sont pas équipés de la fonction push et ceux qui le sont. Les utilisateurs qui ne disposent pas de la fonction "push" verront un délai de 3 jours avant de recevoir un message par e-mail. Les utilisateurs qui utilisent la fonction "push" connaîtront un délai d'un jour, recevront une notification push suivie d'un délai de deux jours, puis recevront le même message e-mail que les utilisateurs qui n'utilisent pas la fonction "push".]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analyse/analytique (si utilisé comme adjectif)

Reportez-vous au tableau suivant pour la description des analyses/analytiques pour cette étape :

| Indicateurs | Description |
|---|---|
| _Entré_ | Nombre total de fois où l'étape a été saisie. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape de l'arbre décisionnel, deux entrées seront enregistrées. |
| _Oui_ | Le nombre d'entrées qui répondent aux critères spécifiés et qui suivent le chemin "oui". |
| _Non_ | Le nombre d'entrées qui ne répondent pas aux critères spécifiés et qui ont été rejetées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

