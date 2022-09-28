---
nav_title: Création de branche
article_title: Création de branche
page_order: 2
page_type: reference
description: "Cet article de référence définit la création de branche et comment elle peut être utile pour vos Canvas."
tool: Canvas

---

# Création d’une branche

> Cet article de référence définit la création de branche et comment elle peut être utile pour vos Canvas. Vous pouvez également consulter notre [Cours d’apprentissage Braze](https://learning.braze.com/canvas-course) pour en savoir plus sur la création de branche pour Canvas.

Vous pouvez exploiter l’efficacité de la livraison par événement de Braze et de la segmentation en temps réel pour proposer des expériences personnalisées pour vos utilisateurs. Pour créer une branche, cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus à la fin de votre étape. Puis sélectionnez l’un des panneaux ombrés pour créer une étape.

![][1]

Vous pouvez également créer une branche à partir de la première étape et créer une autre étape.

![][2]

Vous pouvez configurer des filtres pour déterminer comment vos utilisateurs doivent accéder aux étapes suivantes dans votre Canvas.

![][3]

Vous pouvez également avoir un flux d’utilisateurs entre branches, en fonction des mesures prises. Ce processus permet de dissocier vos utilisateurs dans leurs parcours respectifs. 

![][4]

## Avertissements

### Chevauchement de filtres

Lorsque vous configurez votre Canvas, vous devez vous assurer que les filtres que vous utilisez pour séparer les utilisateurs des différentes branches, ne se chevauchent pas. Si un utilisateur peut associer plusieurs étapes, Braze prendra une branche pour la faire descendre. Par exemple, si un utilisateur a d’abord effectué un achat il y a 7 jours, il sera inséré de manière aléatoire à l’une des branches suivantes.

![Deux branches d’étape de délai avec chevauchement de filtres « Premier achat effectué il y a moins de 2 semaines » et « Premier achat effectué il y a moins de 3 semaines ».][5]

[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %}
[2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %}
[3]: {% image_buster /assets/img_archive/canvas_branch_3.png %}
[4]: {% image_buster /assets/img_archive/canvas_branch_4.png %}
[5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}