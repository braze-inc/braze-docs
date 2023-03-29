---
nav_title: Logique de segmentation
article_title: Logique de segmentation 
page_order: 3

page_type: solution
description: "Cet article d’aide décrit les différences entre les opérateurs AND et OR (ET et OU) et la façon dont vous pouvez les utiliser pour construire des segments puissants."
tool: Segments
---

# Logique de segmentation 

Les opérateurs `AND` et `OR` permettent un filtrage puissant lors de la création d’un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 

## Utilisation de l’opérateur AND (ET)

Utilisez `AND` si vous êtes intéressé par l’intersection de deux groupes. C’est-à-dire ce qui est similaire entre les deux groupes. Si vous souhaitez inclure des clients avec deux valeurs ou plus pour un attribut particulier, vous devez utiliser l’opérateur `AND`. 

Prenons l’exemple d’utilisation d’un ciblage des clients de tous les pays, sauf le Canada et les États-Unis. L’instruction `Country is not United States AND Country is not Canada` inclura uniquement les clients qui ne sont pas des États-Unis et qui ne sont pas du Canada. Par conséquent, les clients des États-Unis et les clients canadiens seront exclus.

## Utilisation de l’opérateur OR (OU)

Utiliser `OR` si vous souhaitez cibler les utilisateurs qui répondent à au moins une condition dans un groupe de conditions. Si vous avez trois conditions reliées par `OR`, alors une, deux ou les trois conditions peuvent être vraies pour que l’instruction soit vraie.

Imaginez par exemple que vous souhaitiez envoyer un message à tous les utilisateurs qui ont la version 1.0 ou 1.1 de votre application. Pour cibler les utilisateurs qui se trouvent sur la version 1.0 et sur la version 1.1, vous pouvez utiliser les filtres `Is 1.0` et `Is 1.1` avec l’opérateur `OR` pour votre segment. Cela ciblera tous les utilisateurs qui se trouvent sur les versions 1.0 ou 1.1.

Dans cet exemple, imaginons une promotion valable pour les clients aux États-Unis et au Canada. Vous souhaitez vous assurer que seuls les clients qui habitent là où la promotion est valide reçoivent la promotion. Dans ce scénario, utilisez l’instruction suivante pour cibler votre campagne : `Country is United States OR Country is Canada`.

Avec l’opérateur `OR`, votre campagne ne sera accessible qu’aux clients dont le pays est le Canada ou dont le pays est les États-Unis.

### Éviter l’opérateur OR (OU)

Dans certaines circonstances, l’opérateur `OR` ne doit pas être utilisé. 

Par exemple, n’utilisez pas `OR` si vous avez une campagne valable dans tous les pays, sauf aux États-Unis et au Canada. Pour filtrer ce segment, vous pouvez essayer d’inverser la logique du scénario précédent. Cependant, cela génère un segment qui cible tous les clients : `Country is not United States OR Country is not Canada`.

L’instruction précédente cible tous les clients, car tous les clients répondent aux critères d’un ou de plusieurs filtres. Les clients canadiens répondent aux critères de `Country is not United States`. Les clients américains répondent aux critères de `Country is not Canada`.

Les critères de ciblage négatifs suivants ne doivent pas être utilisés avec l’opérateur `OR` lorsque deux filtres ou plus font référence au même attribut :

- `is not`
- `does not equal`
- `does not match regex`

Si `is not`, `does not equal` ou `does not match regex` sont utilisés avec l’opérateur `OR` deux fois ou plus dans une instruction, les clients ayant toutes les valeurs de l’attribut pertinent seront ciblés.

## Utiliser les deux opérateurs

Dans l’exemple suivant, nous utiliserons les deux opérateurs `AND` et `OR`. Ici, le public cible comprend les utilisateurs qui ont acheté des baskets Nike ou des baskets Adidas, et qui ont accepté de recevoir des notifications par e-mail.

![Créer un segment pour Amateurs de Sneakers dont la marque préférée est égale à Nike ou Adidas, et qui ont accepté de recevoir des e-mails][33]

Une autre façon de vous assurer que vous construisez la logique adéquate est de créer votre segment et de [prévisualiser les utilisateurs][35] qui sont dedans en fonction de vos filtres. Ainsi, vous pouvez vous assurer que leurs attributs, version d’application ou toute autre segmentation correspondent à ce que vous voyez.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 3 juin 2022_

[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
