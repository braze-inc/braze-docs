---
nav_title: Décision de séparation 
article_title: Décision de séparation 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Cet article de référence aborde la création et la mise en œuvre des étapes de décision de séparation dans votre Canvas."
tool: Canvas

---

# Décision de séparation 

Le composant de décision de séparation dans Canvas vous permet de fournir des expériences personnalisées, en temps réel à vos utilisateurs. Ce composant peut être utilisé pour créer des branches Canvas selon qu’un utilisateur corresponde à la requête ou non.
![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Créer une décision de séparation 

Pour créer une décision de séparation dans votre flux de travail, commencez par ajouter une étape à votre Canvas. Pour Canvas Flow, glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **Decision Split (Décision de séparation)**. Pour l’éditeur Canvas d’origine, utilisez le menu déroulant en haut de la nouvelle étape complète dans votre flux de travail et sélectionnez **Decision Split (Décision de séparation)**.

### Définissez votre fractionnement

Comment souhaitez-vous fractionner vos utilisateurs ? Vous pouvez utiliser des [segments][5] et des filtres pour tirer le trait. En fait, vous créez une requête `true` ou `false` qui permettra d’évaluer vos utilisateurs puis de les diriger vers une étape ou une autre. Vous devez utiliser au moins un segment ou un filtre. Vous ne devez pas utiliser à la fois un segment et un filtre.

![][2]{: style="max-width:90%;"}

{% alert note %} 
Par défaut, les filtres et les segments pour une décision de séparation sont contrôlés dès la réception d’une étape précédente, sauf si vous ajoutez un délai. 
{% endalert %} 

## Utiliser votre séparation

L’utilisation de la décision de séparation vous permet de distinguer des parcours pour vos utilisateurs, en fonction de leur segment ou de leurs attributs, même s’ils utilisent des canaux de communication spécifiques pour recevoir vos messages !

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
| Saisie | Le nombre total de fois où l’étape a été saisie. Si votre Canvas est rééligible et qu’un utilisateur entre deux fois dans un composant de décision de séparation, deux entrées sont enregistrées. |
| Oui | Le nombre d’entrées répondant aux critères indiqués et permettant d’accéder au parcours « oui ». |
| Non | Le nombre d’entrées ne répondant pas aux critères indiqués et permettant d’accéder au parcours « non ». |
{: .reset-td-br-1 .reset-td-br-2}

![][4]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[4]: {% image_buster /assets/img/decision-step-analytics-4.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/
