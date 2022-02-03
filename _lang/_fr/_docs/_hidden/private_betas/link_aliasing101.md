---
nav_title: Aliasing du lien 101
permalink: /lien_aliasing_101
description: "Cet article décrit à quoi s'attendre lorsque le lien Aliasing est activé, comme les impacts sur votre flux de travail et à quoi ressembleront vos liens."
hidden: vrai
---

# Aliasing du lien 101

## Qu'est-ce que l'alias de lien ?

Link Aliasing est une nouvelle fonctionnalité qui permet aux marketeurs de créer des noms identifiables générés par les utilisateurs pour identifier les liens envoyés dans les messages électroniques en provenance de Brésil. Ces noms générés par les utilisateurs sont ensuite disponibles pour le repositionnement de segmentation et le déclenchement basé sur l'action et dans l'affichage de rapports d'informations de clic.

## À quoi s'attendre

{%raw%}
Lorsque l'alias de lien est activé, attendez que les comportements suivants se produisent:
1. Tous les liens reconnus dans un e-mail sont décorés d'un paramètre de requête supplémentaire `lid={{placeholder}}`, où `{{placeholder}}` est une valeur alphanumérique unique générée par Liquide. Cela se produit lorsque le client clique soit sur l'onglet **Gestion des liens** dans le compositeur, soit clique sur **Terminé** pour revenir au flux de travail des messages.
2. Les nouveaux blocs de contenu auront leurs liens modifiés en ajoutant `lid={{placeholder}}` à chaque lien, le cas échéant. La valeur `{{placeholder}}` est résolue quand elle est insérée dans une variante de message e-mail uniquement. Si le bloc de contenu HTML est utilisé dans d'autres canaux, comme les messages dans l'application, le paramètre de requête `couvercle` sera toujours ajouté.
    - Les blocs de contenu qui ont été créés avant l'activation de l'alias de lien ne seront pas reconnus par la fonctionnalité. Les clients sont encouragés à dupliquer et à créer de nouveaux blocs de contenu qui incluent les paramètres de requête d'alias de lien.
{%endraw%}

{% alert note %}
Les clients peuvent également mettre à jour leur bloc de contenu existant. Cependant, seul un maximum de 50 messages faisant référence à ce bloc de contenu sera mis à jour aux fins d'alias de lien.
{% endalert %}

## Quels sont les cas d'utilisation qui peuvent être débloqués ?

Les clients peuvent maintenant distinguer la même URL présente dans leur message e-mail en fournissant des noms d'alias de lien uniques à chacun (par exemple, "main1" et "main2", qui se dirigent tous deux vers https://www. raze.com). Les clients peuvent maintenant redimensionner des alias individuels qui sont cliqués dans la segmentation.

{% alert note %}
Il y a un maximum de 100 alias autorisés à des fins de repositionnement en ce moment.
{% endalert %}

Les clients peuvent créer des déclencheurs basés sur des actions basées sur un alias qui est cliqué car il n'y a pas de limite ici puisque l'action basée sur l'action est déclenchée "dans le moment" nous recevons un événement de clic.

La table Click dans la table Engagement sera maintenant indexée par des alias plutôt que par des paramètres de domaine ou de domaine et de requête de premier niveau. Cette vue permet une meilleure compréhension des liens en fonction de la position dans le courriel plutôt que de la performance du niveau d'URL.

## Quel impact aura-t-il sur mon flux de travail?
Un changement d'opération recommandé est de s'assurer que les clients examinent l'onglet **Gestion des liens** au moment où ils créent leur email. Cela permettra aux clients d'évaluer rapidement les liens présents dans l'e-mail, ajouter des modèles de liens, et fournir une convention de nommage qui fonctionne à des fins de segmentation et de rapport.

## Pouvez-vous me montrer à quoi ressembleront mes liens ?
Braze recherche la balise d'ancrage dans le HTML pour identifier le lien (`<a href=””> Texte du lien </a>`). Braze ajoutera alors en fonction de la présence d'un point d'interrogation(?), qui indique que les paramètres de la requête peuvent être ajoutés.

Voici quelques exemples où Braze peut ajouter en toute sécurité le paramètre de requête `lid`:

{%raw%}
| Lien dans le corps de l'e-mail                                  | Lier avec Aliasing                                                               | Logique                                                                                                                                                                                                                                              |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| https://www.braze.fr                                            | https://www.braze.com?lid=slfdldtqdhdk                                           | Braze insère un point d'interrogation (?) et ajoute le premier paramètre de requête dans l'URL.                                                                                                                                                      |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze détecte d'autres paramètres de requête et ajoute `lid=` à la fin de l'URL.                                                                                                                                                                     |
| `<a href="{{custom_attribute.{product_url}}?">`           | `<a href=”{{custom_attribute.{product_url}}?lid=ac7a548g5kl7”>`            | Braze reconnaît qu'il s'agit d'une URL et a déjà un point d'interrogation (?) présent. Ensuite, il ajoute le paramètre de requête `couvercle` après le point d'interrogation.                                                                        |
| https://www.braze.com#bookmark1?utm_source=email                | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email                | Braze attend que l'URL utilise une structure standard où les ancres (#) sont présentes après un point d'interrogation (?).  Parce que Braze lit de gauche à droite, nous ajouterons le point d'interrogation et la valeur `couvercle` avant l'ancre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{%endraw%}

## Puis-je activer ceci uniquement pour un message ou un groupe d'applications particulier ?
Actuellement, cette fonctionnalité est activée au niveau de l'entreprise. Veuillez vous assurer que votre organisation est au courant de ce changement avant que Braze n'active la fonctionnalité.

## Comment puis-je suivre ou retirer le suivi d'un lien?
Les clients peuvent suivre un lien en utilisant la case à cocher située dans la première colonne de l'onglet **Gestion des liens**. Braze permet de tracer 100 alias à tout moment.  Chaque alias est considéré unique à Braze, quel que soit le nom fourni. Cela signifie que même la même URL qui est présente dans plusieurs variantes sera considérée sur une base individuelle.

Pour dépister un lien, décochez simplement la case à cocher ou [archivez la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/archiving_campaigns/#archiving-campaigns).

## Je suis intéressé! Comment activer l'alias de lien ?
Cette fonctionnalité est toujours prise en compte en version bêta, donc Braze nécessite un accord bêta avant d'activer cette fonctionnalité. Veuillez soumettre ce [formulaire d'accusé de réception de lien Aliasing][1], et Braze activera la fonctionnalité au cours de la prochaine fenêtre de publication, qui se produit chaque semaine.

[1]: https://docs.google.com/forms/d/e/1FAIpQLSfoEXZ9hQfw61AykoKgp2wGtcWyFsjVGGltfTsF0HkNhdU1og/viewform
