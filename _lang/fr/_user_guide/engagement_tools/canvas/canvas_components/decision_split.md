---
nav_title: Étape de fractionnement des décisions
article_title: Étape de fractionnement des décisions
alias: /decision_split/
page_order: 2
page_type: reference
description: "Cet article de référence aborde la création et la mise en œuvre des étapes de fractionnement de décision dans votre Canvas."
tool: Canvas

---

# Étape de fractionnement des décisions

Les étapes de fractionnement des décisions dans Canvas vous permettent de fournir des expériences personnalisées, en temps réel à vos utilisateurs. Les étapes de fractionnement des décisions peuvent être utilisées pour créer des branches Canvas selon qu’un utilisateur réponde à la requête.
![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Créer une étape de fractionnement des décisions

Pour créer une étape de fractionnement des décisions, ajoutez une étape à votre Canvas. Puis utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner **Étape de fractionnement des décisions**.

### Définissez votre fractionnement

Comment souhaitez-vous fractionner vos utilisateurs ? Vous pouvez utiliser des [segments][5] et des filtres pour tirer le trait. En fait, vous créez une requête `true` ou `false` qui permettra d’évaluer vos utilisateurs puis de les diriger vers une étape ou une autre. Vous devez utiliser au moins un segment ou un filtre. Vous ne devez pas utiliser à la fois un segment et un filtre.

![Définir un fractionnement][2]{: style="max-width:80%;"}

{% alert note %} 
Par défaut, les filtres et les segments pour des **Étapes de fractionnement des décisions** sont contrôlés dès la réception d’une étape précédente, sauf si vous ajoutez un délai. 
{% endalert %} 

## Utiliser des étapes de fractionnement

L’utilisation de l’étape de fractionnement des décisions vous permet de distinguer des parcours pour vos utilisateurs, en fonction de leur segment ou de leurs attributs, même s’ils utilisent des canaux de messagerie spécifiques pour recevoir vos messages !

Supposons que vous créiez un flux d’onboarding. Vous pourriez commencer par un e-mail de bienvenue lors de l’inscription. Puis deux jours plus tard, vous souhaitez envoyer un message de notification push mais uniquement aux utilisateurs ayant activé la notification push. Puis, tous les utilisateurs reçoivent un autre e-mail trois jours plus tard après l’inscription. Vous pourriez également utiliser votre décision de fractionnement pour envoyer un message In-App aux utilisateurs pour les inciter à activer la notification push s’ils ne l’ont pas fait.

![][3]{: style="max-width:60%;"}

S’il n’y a pas d’étape suivante dans le parcours, les utilisateurs arrivés à la fin de ce parcours quitteront le Canvas. 

{% alert important %}
Une décision de séparation ne peut pas inclure des étapes parentes au sein d’une étape complète. En bref, vous ne pouvez pas créer une étape complète qui se subdivise en une étape de filtre et une étape complète. Cette restriction se justifie par le fait que s’il existait une branche avec une étape de filtre et une étape complète, la branche à laquelle les utilisateurs doivent accéder ne serait pas indiquée avec précision.
<br>
Une étape de filtre peut être reliée uniquement à une étape suivante.
{% endalert %}

## Analytique

Reportez-vous au tableau suivant pour consulter les descriptions analytiques pour cette étape :

| Métrique | Description |
|---|---|
| Saisie | Le nombre total de fois où l’étape a été saisie. Si votre Canvas est rééligible et qu’un utilisateur saisit deux fois une étape de fractionnement des décisions, les deux entrées seront enregistrées. |
| Oui | Le nombre d’entrées répondant aux critères indiqués et permettant d’accéder au parcours « oui ». |
| Non | Le nombre d’entrées ne répondant pas aux critères indiqués et permettant d’accéder au parcours « non ». |
{: .reset-td-br-1 .reset-td-br-2}

![][4]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[4]: {% image_buster /assets/img/decision-step-analytics-4.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/