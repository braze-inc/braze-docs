---
nav_title: Branchement en cours
article_title: Branchement en cours
page_order: 2
page_type: Référence
description: "Cet article de référence définit le branchement et comment il peut être utile pour vos Canvases."
tool: Toile
---

# Création d'une branche

> Cet article de référence définit le branchement et comment il peut être utile pour vos Canvases. Vous pouvez également consulter notre [cours LAB Canvas](https://lab.braze.com/canvas-course) pour en savoir plus sur le branchement.

Vous pouvez exploiter la puissance de la livraison basée sur l'action de Braze et de la segmentation puissante en temps réel pour offrir des expériences personnalisées à vos utilisateurs. Pour créer une branche, cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus en bas de votre étape. Ensuite, sélectionnez l'un des panneaux ombragés pour créer une nouvelle étape.

!\[Créer une branche\]\[1\]

Vous pouvez également créer une branche à partir de la première étape et créer une autre étape.

!\[Créer une autre branche\]\[2\]

Vous pouvez configurer des filtres pour déterminer comment vos utilisateurs doivent s'écouler vers les étapes suivantes comme indiqué ci-dessous.

!\[Ajouter des filtres\]\[3\]

Ou vous pouvez faire circuler les utilisateurs entre les branches en fonction des actions qu'ils entreprennent. Cela aide à séparer vos utilisateurs dans leurs trajets respectifs.

!\[Exemple de Branche\]\[4\]

## Avertissements

### Filtres de chevauchement

Lorsque vous configurez votre Canvas, vous devez vous assurer que les filtres que vous utilisez pour scinder les utilisateurs de différentes branches ne se chevauchent pas. Si un utilisateur peut faire correspondre plusieurs étapes, Braze choisira une branche pour les envoyer vers le bas. Par exemple, si un utilisateur a fait un achat il y a 7 jours, il sera aléatoirement inséré dans l'une des branches ci-dessous.

!\[Exemple de filtres de chevauchement\]\[5\]
[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %} [2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %} [3]: {% image_buster /assets/img_archive/canvas_branch_3. ng %} [4]: {% image_buster /assets/img_archive/canvas_branch_4.png %} [5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}