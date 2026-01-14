---
nav_title: Enregistrer les brouillons pour Canvas
article_title: Enregistrer les brouillons pour Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Cet article de référence explique comment enregistrer un brouillon pour un canvas déjà lancé."
page_type: reference
tool: Canvas
---

# Enregistrer les brouillons pour Canvas

> Lorsque vous créez et lancez des canvas, vous pouvez modifier un canvas actif et l'enregistrer en tant que brouillon, ce qui vous permet de piloter vos modifications avant un nouveau lancement. 

Si vous avez un Canvas actif qui nécessite des modifications à grande échelle, vous pouvez utiliser cette fonctionnalité pour créer, enregistrer et effectuer un contrôle qualité **avant** de lancer ces modifications dans le Canvas actif. 

Comme pour tout canvas, un seul utilisateur peut modifier un brouillon à la fois, et un canvas ne peut avoir qu'un seul brouillon à la fois. Ces projets n'ont pas d'analyse/analytique car les projets de changement n'ont pas encore été lancés.

Un exemple de projet de canvas avec une bannière qui indique à l'utilisateur qu'il est en train de modifier un projet de canvas avec une option pour voir le canvas actif. Le pied de page comporte des options permettant de revenir à la vue analyse/analytique, d'enregistrer en tant que brouillon ou de lancer le brouillon.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Création d'un projet

Pour créer un brouillon :

1. Accédez à un canvas actif.
2. Sélectionnez le bouton **Enregistrer comme brouillon** dans le pied de page du canvas. 

Notez qu'il n'est pas possible de modifier le canvas actif tant qu'il existe un brouillon d'un canvas. Vous pouvez mettre à jour le canvas pour appliquer les modifications ou rejeter le projet.

## Référence au projet actif

Pour faire référence au Canvas actif, sélectionnez **Afficher le Canvas actif** dans le pied de page de la vue analytique ou dans l'en-tête du Canvas à partir du brouillon. Pour revenir à un canvas actif, sélectionnez **Modifier le brouillon** dans la vue analytique ou dans la vue du canvas actif.

Vous ne pouvez faire référence qu'à des étapes qui ont déjà été lancées avant la création du projet. Cela signifie que si vous avez créé une étape ou un canal **après la** création du projet, il ne peut pas être référencé dans votre projet.

{% alert note %}
Si un bloc de contenu est référencé dans un projet Canvas, le Canvas est listé dans le décompte d'inclusion du bloc de contenu. Toutefois, si le bloc de contenu est référencé dans un brouillon d'un canvas **actif**, ce dernier ne sera pas pris en compte dans le décompte des inclusions de blocs de contenu.
{% endalert %}

### Priorité aux messages in-app

Pour les brouillons d'un Canvas actif, la priorité des messages in-app dans le générateur de Canvas sera mise à jour immédiatement lorsqu'un utilisateur modifie la priorité. Cela signifie que la priorité des messages in-app au niveau du Canvas est appliquée immédiatement au Canvas actif, même s'il existe un brouillon. 

Toutefois, les changements de priorité des messages in-app au niveau des étapes sont enregistrés en tant que brouillon et appliqués lors de la mise à jour du Canvas. Par exemple, dans une étape Message, le trieur de priorités sera mis à jour lorsqu'un utilisateur lancera le brouillon puisque les paramètres de l'étape s'appliquent au niveau de l'étape.

