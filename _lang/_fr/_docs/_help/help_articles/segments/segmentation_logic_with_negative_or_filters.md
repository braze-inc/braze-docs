---
nav_title: Logique de la segmentation avec filtres négatifs OU négatifs
article_title: Logique de la segmentation avec filtres négatifs OU négatifs
page_order: 4
page_type: Solution
description: "Cet article vous guide à travers les meilleures pratiques sur l'utilisation ou non de l'opérateur OR et sur la date d'utilisation de l'opérateur AN."
tool: Segments
---

# Logique de segmentation avec filtres négatifs OU

L'opérateur OU doit être utilisé avec soin, surtout lorsque l'on considère :
* [Quand appliquer l'opérateur OR](#using-or)
* [Lorsqu'il ne faut pas appliquer l'opérateur OR](#when-not-to-apply-the-or-operator)
* [Quand appliquer l'opérateur ET](#when-to-apply-the-and-operator)

## Quand appliquer l'opérateur OR {#using-or}

Utilisez l'opérateur `OU` pour créer une instruction qui évaluera à true si un utilisateur répond aux critères pour un ou plusieurs filtres dans la déclaration.

Par exemple, envisagez une promotion valable pour les clients des États-Unis et du Canada. Vous voulez vous assurer que seuls les clients dans les zones où la promotion est valide reçoivent la promotion. Dans ce scénario, utilisez la déclaration suivante pour cibler votre campagne:

`Le pays est les États-Unis OU le pays est le Canada`

!\[États-Unis OU Canada\]\[49\]{: style="max-width:80%"}

Avec l'opérateur `OU` , votre campagne ne sera envoyée qu'aux clients dont le pays est le Canada ou dont le pays est les États-Unis.

## Lorsqu'il ne faut pas appliquer l'opérateur OR

Dans certaines circonstances, l'opérateur `OU` ne doit pas être utilisé. Par exemple, n'utilisez pas `OU`si vous avez une campagne valide dans tous les pays, à l'exception des États-Unis et du Canada. Pour filtrer ce segment, vous pouvez essayer d'inverser la logique du scénario précédent. Cependant, cela mène à un segment qui cible tous les clients :

`Le pays n'est pas les États-Unis OU le pays n'est pas le Canada`

!\[Not United States OR Canada\]\[50\]{: style="max-width:80%"}

L'énoncé précédent vise tous les clients parce que tous les clients répondent aux critères d'un ou de plusieurs filtres. Les clients canadiens répondent aux critères de `Pays n'est pas aux États-Unis`. Les clients américains répondent aux critères de `Pays n'est pas le Canada`.

Les critères de ciblage négatif suivants ne doivent pas être utilisés avec l'opérateur `OU` lorsque deux ou plusieurs filtres font référence au même attribut :

- `n'est pas`
- `n'est pas égal à`
- `ne correspond pas à l'expression régulière`

Si `n'est pas`, `n'est pas égal`, ou `ne correspond pas à regex` sont utilisés avec l'opérateur `OU` deux fois ou plus dans une instruction, les clients avec toutes les valeurs pour l'attribut pertinent seront ciblés.

## Quand appliquer l'opérateur ET

Si vous souhaitez inclure des clients avec deux ou plusieurs valeurs pour un attribut particulier, vous devez utiliser l'opérateur `ET`. Revenons à l'exemple du cas d'utilisation : ciblons les clients de tous les pays, à l'exception du Canada et des États-Unis.

L'énoncé `Le pays n'est pas les États-Unis ET le pays n'est pas le Canada` inclura uniquement les clients qui ne sont pas des États-Unis et qui ne sont pas du Canada. Par conséquent, tant les clients des États-Unis que les clients du Canada seront exclus.

Vous avez encore besoin d'aide ? [Ouvrir un ticket de support]({{site.baseurl}}/support_contact/).

_Dernière mise à jour le 17 septembre 2021_
[49]: {% image_buster /assets/img_archive/us_canada.png %} [50]: {% image_buster /assets/img_archive/not_us_not_canada.png %}
