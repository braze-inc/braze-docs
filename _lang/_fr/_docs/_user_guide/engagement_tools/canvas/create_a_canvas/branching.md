---
nav_title: Branchement en cours
article_title: Branchement en cours
page_order: 2
page_type: Référence
description: "Cet article de référence couvre ce qu'est la branche, et comment il peut être utile dans vos Canvases."
tool: Toile
---

# Branchement en cours

> cet article de référence couvre ce qu'est la branche, et comment il peut être utile dans vos toiles.

## Créer une branche

Vous pouvez exploiter la puissance de la livraison basée sur l'action de Braze et de la segmentation puissante en temps réel pour offrir des expériences personnalisées à vos utilisateurs.

Pour créer une branche, cliquez sur le cercle bleu en bas d'une étape. Cliquez ensuite sur l'une des icônes ombragées pour créer une nouvelle étape.

!\[Canvas Create Branch 1\]\[1\]

Créer une autre étape, branchement depuis la première:

!\[Canvas Create Branch 2\]\[2\]

Vous pouvez configurer des filtres pour déterminer comment les utilisateurs doivent se déplacer vers les étapes suivantes.

!\[Canvas Create Branch 3\]\[3\]

Ou vous pouvez faire circuler les utilisateurs entre les branches en fonction des actions qu'ils entreprennent.

!\[Canvas Create Branch 4\]\[4\]

## Avertissements

### Filtres de chevauchement

Lorsque vous configurez votre Canvas, vous devez vous assurer que les filtres que vous utilisez pour scinder les utilisateurs de différentes branches ne se chevauchent pas. Si un utilisateur peut faire correspondre plusieurs étapes, Braze choisira une branche pour les envoyer vers le bas. Par exemple :

!\[Canvas Create Branch 5\]\[5\]

Si un utilisateur a fait un achat il y a 7 jours, il sera placé aléatoirement dans l'une des branches ci-dessus.
[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %} [2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %} [3]: {% image_buster /assets/img_archive/canvas_branch_3. ng %} [4]: {% image_buster /assets/img_archive/canvas_branch_4.png %} [5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}

