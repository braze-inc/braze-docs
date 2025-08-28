---
nav_title: Enregistrer des ébauches pour Canvas
article_title: Enregistrer des ébauches pour Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Cet article de référence explique comment enregistrer un brouillon pour une toile qui a déjà été lancée."
page_type: reference
tool: Canvas
---

# Enregistrer des ébauches pour Canvas

> Au fur et à mesure que vous créez et lancez des Canvases, vous pouvez modifier un Canvas actif et l'enregistrer en tant que brouillon, ce qui vous permet de tester vos modifications avant un autre lancement. 

Si vous avez un Canvas actif qui nécessite des modifications à grande échelle, vous pouvez utiliser cette fonctionnalité pour créer, enregistrer et effectuer un contrôle qualité **avant** de lancer ces modifications dans le Canvas actif. 

Comme pour tout canvas, un seul utilisateur peut modifier un brouillon à la fois, et un canvas ne peut avoir qu'un seul brouillon à la fois. Ces brouillons n'ont aucune analyse car les modifications du brouillon n'ont pas encore été lancées.

![Un exemple d’ébauche Canvas avec une bannière indiquant à l’utilisateur qu’il édite une ébauche Canvas avec l’option d’afficher le Canvas actif. Le pied de page comporte des options permettant de revenir à la vue d'analyse/analytique, d'enregistrer un brouillon ou de lancer un brouillon.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Création d'un projet

Pour créer un brouillon :

1. Accédez à un canvas actif.
2. Sélectionnez le bouton **Enregistrer comme brouillon** dans le pied de page du canvas. 

Prenez en compte le fait que vous ne pouvez pas modifier le Canvas actif tant qu’une ébauche existe pour un Canvas. Vous pouvez mettre à jour le Canvas pour appliquer les modifications ou abandonner le brouillon.

## Référence au projet actif

Pour référencer le Canvas actif, sélectionnez **Afficher le Canvas actif** dans le pied de page depuis la vue analytique ou l'en-tête du Canvas depuis le brouillon. Pour revenir à un Canvas actif, sélectionnez **Modifier le brouillon** depuis la vue analytique ou la vue Canvas active.

Vous ne pouvez faire référence qu'à des étapes qui ont déjà été lancées avant la création du projet. Cela signifie que si vous avez créé une étape ou un canal **après la** création du projet, il ne peut pas être référencé dans votre projet.

{% alert note %}
Si un bloc de contenu est référencé dans une ébauche de Canvas, le Canvas est listé dans le décompte d'inclusion du bloc de contenu. Toutefois, si le bloc de contenu est référencé dans un brouillon d'un canvas **actif**, ce dernier ne sera pas pris en compte dans le décompte des inclusions de blocs de contenu.
{% endalert %}

### Priorisation des messages dans l'application

Pour les brouillons d'un Canvas actif, la priorité des messages dans l'application au sein du constructeur de Canvas sera mise à jour immédiatement lorsqu'un utilisateur modifie la priorité. Cela signifie que la priorité des messages intégrés au niveau de Canvas est appliquée au Canvas actif immédiatement, même lorsqu'un brouillon existe. 

Cependant, les modifications de priorité des messages intégrés au niveau de l'étape sont enregistrées en tant que brouillon et appliquées lorsque le Canvas est mis à jour. Par exemple, dans une étape Message, le trieur de priorités sera mis à jour lorsqu'un utilisateur lancera le brouillon, étant donné que les paramètres de l'étape s'appliquent au niveau de l'étape.

