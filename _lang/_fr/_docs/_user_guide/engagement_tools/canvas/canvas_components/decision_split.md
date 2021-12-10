---
nav_title: Étape de séparation de décision
article_title: Étape de séparation de décision
alias: /fraction_de_décision/
page_order: 2
page_type: Référence
description: "Cet article de référence couvre la façon de créer et de mettre en œuvre des étapes de séparation de décision dans votre Canvas."
tool: Toile
---

# Étape de séparation de décision

Les étapes séparées de décision dans Canvas vous permettent de livrer des expériences personnalisées et en temps réel à vos utilisateurs. Les étapes de séparation de décision peuvent être utilisées pour créer des branches de Canvas en fonction du fait qu'un utilisateur correspond à une requête. !\[Decision Split Step\]\[1\]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Créer une étape de séparation de décision

Pour créer une étape de séparation de décision, ajoutez une étape à votre Canvas. Ensuite, utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner **Étape de séparation de la décision**.

### Définissez votre séparation

Comment voulez-vous diviser vos utilisateurs ? Vous pouvez utiliser Segments et Filtres pour tracer la ligne. Essentiellement, vous créez une requête `true` ou `false` qui évaluera vos utilisateurs puis les entonnoira à une étape ou une autre. Vous devez utiliser au moins un segment ou un filtre. Vous n'avez pas besoin d'utiliser à la fois un segment et un filtre.

!\[Define Split\]\[2\]{: style="max-width:80%;"}

{% alert note %}
Par défaut, les filtres et les segments pour les **étapes de séparation de décision** sont vérifiés juste après avoir reçu une étape précédente, à moins que vous n'ajoutiez un délai.
{% endalert %}

## Utiliser les étapes séparées

Utiliser l'étape de séparation de décision peut vous aider à distinguer les chemins pour vos utilisateurs en fonction de leur segment ou de leurs attributs, même s'ils utilisent certains canaux de messagerie pour recevoir vos messages!

Disons que vous êtes en train de créer un flux d’intégration. Vous pourriez commencer par un e-mail de bienvenue lors de votre inscription. Ensuite, deux jours plus tard, vous voulez envoyer un message push, mais seulement aux utilisateurs qui sont activés. Après cela, tous les utilisateurs reçoivent un autre e-mail trois jours après leur inscription. Vous pouvez également utiliser votre décision divisée pour envoyer un message dans l'application aux utilisateurs qui n'ont pas d'autorisation push pour les encourager à activer push.

!\[Use Split in Onboarding\]\[3\]{: style="max-width:60%;"}

S'il n'y a pas d'étape suivant l'un des chemins, les utilisateurs qui descendent sur ce chemin quitteront le Canvas.

{% alert important %}
Une séparation de décision ne peut pas avoir des étapes complètes de fraternité. En d'autres termes, vous ne pouvez pas créer une étape complète qui branche dans une étape de filtre et une étape complète. Cette restriction existe car s'il y avait une branche avec une étape de filtre et une étape complète, il ne serait pas clair quels utilisateurs de la branche descendraient.
<br>
Une étape de filtre ne peut se connecter qu'à une étape suivante.
{% endalert %}

## Analyses

| métrique | Libellé                                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entré    | Le nombre total de fois que l'étape a été saisie. Si votre Canevas a rééligibilité et qu'un utilisateur entre deux fois une étape de séparation de décision, deux entrées seront enregistrées. |
| Oui      | Le nombre d'entrées qui remplissent les critères spécifiés et qui se sont déroulées dans le chemin "oui".                                                                                      |
| Non      | Le nombre d'entrées qui ne remplissaient pas les critères spécifiés et qui se sont déroulées dans le chemin « non ».                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

!\[Analyses de l'étape de la décision\]\[4\]{: style="max-width:80%;"}
[1]: {% image_buster /assets/img/decision-split-1.png %} [2]: {% image_buster /assets/img/define-split-2. ng %} [3]: {% image_buster /assets/img/use-split-onboarding-3.png %} [4]: {% image_buster /assets/img/decision-step-analytics-4.png %}
