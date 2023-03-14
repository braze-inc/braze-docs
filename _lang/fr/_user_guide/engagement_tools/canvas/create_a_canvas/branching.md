---
nav_title: Création de branches
article_title: Création de branches
page_order: 2
page_type: reference
description: "Cet article de référence définit la création de branches et comment elle peut être utile pour vos Canvas."
tool: Canvas

---

# Création d’une branche

> Cet article de référence définit la création de branches et comment elles peuvent être utiles pour vos Canvas construits avec le flux de travail Canvas d’origine. Consultez notre [Cours d’apprentissage Braze](https://learning.braze.com/canvas-course) pour en savoir plus sur la création de branches !

{% alert important %}
À compter du 28 février 2023, vous ne pourrez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas originale. Braze recommande aux clients qui utilisent l’expérience Canvas originale de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Pour créer une branche, cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> en bas de votre composant Canvas. Puis sélectionnez l’un des panneaux ombrés pour créer une étape.

![][1]{: style="max-width:70%;"}

Vous pouvez également créer une branche à partir de la première étape et créer une autre étape.

![][2]{: style="max-width:70%;"}

Vous pouvez configurer des filtres pour déterminer comment vos utilisateurs doivent accéder aux étapes suivantes dans votre Canvas.

![][3]{: style="max-width:70%;"}

Vous pouvez également avoir un flux d’utilisateurs entre branches, en fonction des mesures prises. Ce processus permet de dissocier vos utilisateurs dans leurs parcours respectifs. 

![][4]{: style="max-width:70%;"}

## Bonnes pratiques

Même si la création de branches peut s’avérer utile pour transmettre des expériences personnalisées à vos utilisateurs, gardez à l’esprit ces bonnes pratiques lorsque vous créez votre parcours Canvas.

### Nombre important d’entrées

En général, il est préférable de garder un nombre minimum d’entrées (le nombre d’utilisateurs et d’étapes en file d’attente) pour chaque cas d’utilisation Canvas. Si vous constatez que le nombre d’entrées augmente, nous vous recommandons de dupliquer votre Canvas dans [Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) pour obtenir une gestion Canvas plus fluide.

### Chevauchement de filtres

Lorsque vous configurez votre Canvas, vous devez vous assurer que les filtres que vous utilisez pour séparer les utilisateurs des différentes branches, ne se chevauchent pas. Si un utilisateur peut associer plusieurs étapes, Braze prendra une branche pour la faire descendre. Par exemple, si un utilisateur a d’abord effectué un achat il y a sept jours, il sera inséré de manière aléatoire dabs l’une des branches suivantes.

![Deux branches d’étape de délai avec chevauchement de filtres « Premier achat effectué il y a moins de 2 semaines » et « Premier achat effectué il y a moins de 3 semaines ».][5]

[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %}
[2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %}
[3]: {% image_buster /assets/img_archive/canvas_branch_3.png %}
[4]: {% image_buster /assets/img_archive/canvas_branch_4.png %}
[5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}