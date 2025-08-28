---
nav_title: Logique de segmentation
article_title: Logique de segmentation 
page_order: 3

page_type: solution
description: "Cet article d’aide décrit les différences entre les opérateurs AND et OR (ET et OU) et la façon dont vous pouvez les utiliser pour créer des segments puissants."
tool: Segments
---

# Logique de segmentation 

Les opérateurs `AND` et `OR` permettent un filtrage puissant lors de la [création d'un segment.]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) À l'aide de ces opérateurs, vous pouvez cibler vos utilisateurs en fonction de leurs actions ou de leurs comportements lors de l'étape **Audience ciblée** de la création de vos campagnes ou Canevas.

## Comprendre les opérateurs AND (ET) et OR (OU)

Les opérateurs `AND` et `OR` fonctionnent de différentes manières. Vous pouvez utiliser chaque opérateur en fonction de ce que vous souhaitez accomplir lors de la segmentation de votre audience. 

### Quand utiliser l’opérateur AND (ET)

En général, utilisez `AND` si vous êtes intéressé par l'intersection de deux valeurs ou plus pour un attribut particulier.

Prenons l’exemple du ciblage des utilisateurs de tous les pays, sauf le Canada et les États-Unis dans une campagne. Dans ce cas, l’utilisation de l’opérateur `AND` peut aider à filtrer ces utilisateurs. L’instruction `Country is not United States AND Country is not Canada` inclura uniquement les utilisateurs qui ne sont pas des États-Unis et qui ne sont pas du Canada. Ainsi, en utilisant cette logique, les utilisateurs du Canada et des États-Unis seront exclus.

### Quand utiliser l’opérateur OR (OU)

Utilisez `OR` si votre but est de cibler les utilisateurs qui répondent à au moins une condition dans un ensemble de conditions. Si vous avez trois conditions reliées par `OR`, alors une, deux ou les trois conditions peuvent être vraies pour que l’instruction proprement dite soit vraie.

Imaginez par exemple que vous souhaitiez envoyer un message à tous les utilisateurs qui ont la version 1.0 ou 1.1 de votre application. Pour cibler les utilisateurs qui se trouvent sur la version 1.0 et sur la version 1.1, vous pouvez utiliser les filtres `Is 1.0` et `Is 1.1` avec l’opérateur `OR` pour votre segment. Cela ciblera tous les utilisateurs qui se trouvent sur les versions 1.0 ou 1.1.

Dans cet exemple, imaginons une promotion valable pour les utilisateurs aux États-Unis et au Canada. Vous souhaitez vous assurer que seuls les utilisateurs qui habitent là où la promotion est valide reçoivent la promotion. Dans ce scénario, utilisez l’instruction suivante pour cibler votre campagne : `Country is United States OR Country is Canada`. Avec l'opérateur `OR`, votre campagne ne s'adressera qu'aux utilisateurs dont le pays est le Canada ou les États-Unis.

#### Quand éviter l’opérateur OR

Il peut y avoir des situations de ciblage de l’utilisateur où l’utilisation de l’opérateur `OR` doit être évitée. L’opérateur `OR` crée une instruction qui évalue si un utilisateur répond aux critères d’un ou plusieurs filtres d’une instruction. Par exemple, si vous souhaitez créer un segment d’utilisateurs qui appartiennent au segment « gastronomes » mais qui n’appartiennent pas soit au segment « non gastronomes » soit au segment « amateurs de bonbons », l’opérateur `OR` peut alors fonctionner.

![]({% image_buster /assets/img_archive/or_operator_segment.png %})

Cependant, si votre objectif est de segmenter les utilisateurs qui appartiennent au segment « gastronomes » et qui ne sont dans aucun des segments « non gastronomes » et « amateurs de bonbons », utilisez l’opérateur `AND`. De cette manière, les utilisateurs qui reçoivent la campagne ou le canvas appartiennent au segment visé ("foodies") et non aux autres segments ("non-foodies" et "candy-lovers") en même temps. 

Les critères de ciblage négatifs suivants ne doivent pas être utilisés avec l’opérateur `OR` lorsque deux filtres ou plus font référence au même attribut :

- `is not`
- `does not equal`
- `does not match regex`

Si `is not`, `does not equal` ou `does not match regex` sont utilisés avec l’opérateur `OR` deux fois ou plus dans une instruction, les utilisateurs ayant toutes les valeurs de l’attribut pertinent seront ciblés.

### Utiliser les deux opérateurs

Dans l’exemple suivant, nous utiliserons les deux opérateurs `AND` et `OR`. Ici, l'audience cible comprend les utilisateurs qui ont acheté des baskets Nike ou des baskets Adidas, et qui ont accepté de recevoir des notifications par e-mail.

![Créer un segment pour les acheteurs de chaussures de sport lorsque la marque préférée de l'utilisateur est Nike ou Adidas et qu'il a choisi d'être abonné à l'e-mail]({% image_buster /assets/img_archive/NikeSneakers.png %}).

Une autre façon de vous assurer que vous créez la bonne logique est de créer votre segment et de [prévisualiser les utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) qui y tombent en fonction de vos filtres. Ainsi, vous pouvez vous assurer que leurs attributs, version d’application ou toute autre segmentation correspondent à ce que vous voyez.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 3 juin 2022_

