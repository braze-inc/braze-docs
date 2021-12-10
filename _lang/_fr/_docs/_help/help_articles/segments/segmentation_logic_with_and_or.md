---
nav_title: Logique de la segmentation avec Et/Or
article_title: Logique de la segmentation avec Et/Or
page_order: 3
page_type: Solution
description: "Cet article vous guide à travers la différence entre les opérateurs ET et OU et comment vous pouvez les utiliser pour construire des segments puissants."
tool: Segments
---

# Logique de segmentation avec ET/OU

Les opérateurs `ET` et `OU` permettent un filtrage très puissant. Il y a 2 scénarios que vous pouvez appliquer :
* [Utiliser AND ou OR](#using-and-or-or)
* [Utiliser les deux](#using-both)

## Utiliser AND ou OR

### ET

Utilisez `ET` si vous êtes intéressé par l'intersection de deux groupes. C'est ce qui est similaire entre les deux groupes. Par exemple, comparons deux animaux. Ce que les chiens `ET` chats ont en commun est la fourrure, ce sont des mammifères et sont des animaux humains :

!\[Définition du diagramme de Venn\]\[30\]

### OU

Utilisez **ou** si vous voulez cibler les utilisateurs qui remplissent au moins une condition dans un groupe de conditions. Si vous avez trois conditions liées entre elles par `OU`, alors une, deux, ou toutes les conditions pourraient être vraies pour que la déclaration soit vraie.

Par exemple, imaginez que vous voulez envoyer un message à tous vos utilisateurs __sauf__ ces utilisateurs sur la version `1.` ou `1.1` de votre application. Vous voulez cibler le chevauchement des utilisateurs qui ne sont pas sur la version `1.` et non sur la version `1.1.1.` Vous pouvez créer ce segment d'une des deux façons :


* Vous pouvez utiliser deux filtres « n'est pas `1.0`» OU « n'est pas `1.1`». En utilisant ce filtre `OU` , vous ciblez tous les utilisateurs qui n'ont pas ces versions.

* L'alternative peut être une route plus longue. Vous devrez ajouter un filtre pour chaque version de votre application en utilisant l'instruction OU, en s'assurant d'exclure les versions de l'application `1.` et `1.1`.


# Utiliser les deux

Enfin, regardez l'exemple ci-dessous où nous utilisons à la fois les `ET` et `OU`. Le public ciblé ici sont les utilisateurs qui ont acheté Nike Sneakers `OU` Adidas sneakers `ET` sont choisis pour recevoir des notifications par courriel.

!\[Exemple de Shoppers Sneaker\]\[33\]

!\[Exemple de Diagramme de Venn\]\[34\]

Une autre façon de vous assurer que vous construisez la bonne logique est de créer votre segment et de [prévisualiser les utilisateurs][35] qui y tombent en fonction de vos filtres. De cette façon, vous pouvez vous assurer que leurs attributs, la version de l'application, ou toute autre segmentation correspondent à ce que vous voyez.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 23 septembre 2021_
[30]: {% image_buster /assets/img_archive/trouble10.png %} [33]: {% image_buster /assets/img_archive/NikeSneakers.png %} [34]: {% image_buster /assets/img_archive/VennDiagram.png %}

[35]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
